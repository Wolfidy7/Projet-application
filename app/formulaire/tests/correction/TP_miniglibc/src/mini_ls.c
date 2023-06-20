#include "mini_lib.h"

#include <dirent.h>
#include <errno.h>
#include <grp.h>
#include <pwd.h>
#include <stdio.h>
#include <sys/stat.h>
#include <time.h>
#include <unistd.h>

typedef struct {
    char **files;
    int size;
    int max;
} todo_files;

char cwd[100];

/*char *base_dir(char *src) {*/
/*char *ret = malloc(sizeof(char) * 101);  // max 100 characters*/
/*int l     = strlen(src);*/
/*int i;*/
/*for (i = l - 1; i >= 0; i--) {*/
/*if (src[i] == '\\') {*/
/*strncpy(ret, src, i + 1);*/
/*}*/
/*}*/
/*ret[i + 1] = '\0';*/
/*return ret;*/
/*}*/

void add_end_slash(char *dest) {
    int l = mini_strlen(dest);
    for (int i = 0; i < l; i++) {
        if (dest[i] == '\0') {
            if (i == 0) {
                return;
            }
            if (dest[i - 1] != '/') {
                dest[i]     = '/';
                dest[i + 1] = '\0';
            }
        }
    }
}

/*void to_human(char *human_size, int size) {*/
/*char *suffixes[6] = {"", "K", "M", "G", "T"};*/
/*int i = 0;*/
/*int last_decimal = 0;*/
/*while(size > 1024) {*/
/*last_decimal = size % 1024 / 100;*/
/*size /= 1024;*/
/*i++;*/
/*[>printf("%d %d %s\n", i, size, human_size);<]*/
/*}*/
/*if(last_decimal != 0) {*/
/*snprintf(human_size, 5, "%d.%d%s", size, last_decimal, suffixes[i]);*/
/*} else {*/
/*snprintf(human_size, 5, "%d%s", size, suffixes[i]);*/
/*}*/
/*}*/

int ls_file(struct stat stats, char *path, todo_files *todo, char *parent, int recursive) {
    unsigned int link_count = stats.st_nlink;
    unsigned int size       = stats.st_size;
    unsigned int uid        = stats.st_uid;
    unsigned int gid        = stats.st_gid;
    mode_t mode             = stats.st_mode;
    char dir[2];
    switch (mode & S_IFMT) {
    case S_IFDIR: dir[0] = 'd'; break;
    case S_IFLNK: dir[0] = 'l'; break;
    default: dir[0] = '-';
    }
    dir[1] = '\0';
    char perm[10];
    perm[0] = (mode & S_IRUSR) ? 'r' : '-';
    perm[1] = (mode & S_IWUSR) ? 'w' : '-';
    perm[2] = (mode & S_IXUSR) ? 'x' : '-';
    perm[3] = (mode & S_IRGRP) ? 'r' : '-';
    perm[4] = (mode & S_IWGRP) ? 'w' : '-';
    perm[5] = (mode & S_IXGRP) ? 'x' : '-';
    perm[6] = (mode & S_IROTH) ? 'r' : '-';
    perm[7] = (mode & S_IWOTH) ? 'w' : '-';
    perm[8] = (mode & S_IXOTH) ? 'x' : '-';
    perm[9] = '\0';

    /*char human_size[6];*/
    /*to_human(human_size, size);*/
    /*human_size[5] = '\0';*/

    struct tm *modified;
    if ((modified = localtime(&stats.st_mtim.tv_sec)) == NULL) {
        mini_printf("error: gmtime");
        return -1;
    }


    struct passwd *pwd;
    if ((pwd = getpwuid(uid)) == NULL) {
        mini_printf("error: getpwuid");
        return -1;
    }

    struct group *grp;
    if ((grp = getgrgid(gid)) == NULL) {
        mini_printf("error: getgrgid");
        return -1;
    }

    char modtm[20];
    strftime(modtm, 20, "%b %2d %R", modified);

    char *link_count_s = mini_itoa(link_count);
    char *size_s       = mini_itoa(size);
    mini_printf(dir);
    mini_printf(perm);
    mini_printf(" ");
    mini_printf(link_count_s);
    mini_printf(" ");
    mini_printf(pwd->pw_name);
    mini_printf(" ");
    mini_printf(grp->gr_name);
    mini_printf(" ");
    mini_printf(size_s);
    mini_printf(" ");
    mini_printf(modtm);
    mini_printf(" ");
    mini_printf(path);
    /*mini_printf("\n");*/
    /*printf("%s%s %s %s %s %s %s %s", dir, perm, link_count_s, pwd->pw_name,*/
    /*grp->gr_name, size_s, modtm, path);*/

    if ((mode & S_IFMT) == S_IFLNK) {
        /*printf("\n%o %o %o\n", mode, mode & S_IFLNK, S_IFLNK);*/
        char buf[30];
        /*printf("(%s : %s : %i)", path, buf, 30);*/
        if (-1 == readlink(path, buf, 30)) {
            /*printf("%s %s %i\n", path, buf, 30);*/
            mini_printf("error: readlink");
            return -1;
        }
        /*printf(" -> %s", buf);*/
        mini_printf(" -> ");
        mini_printf(buf);
    } else if ((mode & S_IFMT) == S_IFDIR && todo->size < todo->max && recursive) {
        todo->files[todo->size] = mini_calloc(sizeof(char), 101);  // 100 char
                                                                   // max path

        /*printf("parent: %s\n", parent);*/
        /*printf("child: %s\n", path);*/
        mini_strncpy(todo->files[todo->size], parent, 100);
        mini_strncat(todo->files[todo->size], path, 100 - mini_strlen(parent));
        todo->files[todo->size][100] = '\0';
        /*printf("(%s %s)", todo->files[todo->size], path);*/
        todo->size++;
    }

    mini_printf("\n");
    return 0;
}

int ls(char *path, todo_files *todo, int recursive) {
    struct stat stats;
    if (lstat(path, &stats) == -1) {
        mini_printf(path);
        mini_printf("\nerror: path does not exists\n");
        return -1;
    }

    mode_t mode = stats.st_mode;

    if (mode & S_IFDIR) {
        DIR *dir;
        if ((dir = opendir(path)) == NULL) {
            mini_printf("error: opendir");
            return -1;
        }

        errno = 0;
        chdir(path);
        while (1) {
            struct dirent *dirent = readdir(dir);
            if (dirent == NULL) {
                if (errno == 0)
                    break;
                else {
                    mini_printf("error: readdir");
                    return -1;
                }
            }
            if (lstat(dirent->d_name, &stats) == -1) {
                mini_printf("error: stat");
                return -1;
            }
            char d_name[102];
            mini_strncpy(d_name, path, 100);
            /*strncat(d_name, dirent->d_name, 100 - strlen(path));*/
            /*add_end_slash(d_name);*/
            if (d_name[mini_strlen(path)] != '/') {
                mini_strncat(d_name, "/", 2);
            }
            d_name[101] = '\0';
            if (mini_strcmp(dirent->d_name, ".") != 0
                && mini_strcmp(dirent->d_name, "..") != 0) {
                ls_file(stats, dirent->d_name, todo, d_name, recursive);
            }
        }
        /*printf("%s %s))", path, base_dir(path));*/
        /*chdir("..");*/
        closedir(dir);
    } else {
        if (ls_file(stats, path, todo, path, recursive) == -1) {
            return -1;
        }
    }

    return 0;
}

int main(int argc, char **argv) {
    char start_path[100];
    if (getcwd(cwd, sizeof(cwd)) == NULL) {
        mini_printf("error: getcwd");
        return 1;
    }

    int recursive = 0;

    if (argc < 2) {
        /*mini_strncpy(start_path, cwd, 99);*/
        /*start_path[99] = '\0';*/
        mini_printf("1 argument required\n");
        return 0;
    } else {
        if (mini_strcmp("-r", argv[1]) == 0 && argc > 2) {
            mini_strncpy(start_path, argv[2], 99);
            start_path[99] = '\0';
            recursive      = 1;
        } else {
            mini_strncpy(start_path, argv[1], 99);
            start_path[99] = '\0';
        }
    }

    int ret          = 0;
    todo_files *todo = mini_calloc(sizeof(todo_files), 1);
    todo->files      = mini_calloc(sizeof(char *), 100);  // 100 subdirs max
    todo->size       = 1;
    todo->max        = 100;

    mini_printf(start_path);
    mini_printf(":\n");
    ret = ls(start_path, todo, recursive);
    if (ret != 0)
        return 1;

    todo->files[0] = mini_calloc(sizeof(char), 101);  // 100 char max path
    mini_strncpy(todo->files[0], start_path, 100);
    todo->files[0][100] = '\0';
    /*printf("(%s %s)", todo->files[todo->size], path);*/

    for (int i = 1; i < todo->size; i++) {
        /*printf("\n%s:\n", todo->files[i]);*/
        mini_printf("\n");
        mini_printf(todo->files[i]);
        mini_printf(":\n");
        chdir(cwd);
        ret = ls(todo->files[i], todo, recursive);
        if (ret != 0)
            return 1;
        chdir(cwd);
    }

    return ret;
}
