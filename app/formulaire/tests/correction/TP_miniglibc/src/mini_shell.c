#include "mini_lib.h"

#include <stdio.h>
#include <sys/wait.h>
#include <unistd.h>

// one cmmand cannot be more than 512 caracters
#define BUFSIZE 512

char buf[BUFSIZE];

extern char **environ;


int start_with(char *s, char *query) {
    int i = 0;
    while (s[i] == query[i]) {
        if (query[i] == '\0' || s[i] == '\0') {
            break;
        }
        i++;
    }
    if (query[i] == '\0') {
        return 1;
    }
    return 0;
}

char **parse_args(char *s) {
    char **res;

    int arg_num = 0;
    int i       = 0;
    while (s[i] != '\0') {
        if ((s[i] == '\n' || s[i] == ' ') && i > 0 && s[i - 1] != ' ' && s[i - 1] != '\n') {
            arg_num++;
        }
        i++;
    }
    if (i != 0 && s[i - 1] != '\n' && s[i - 1] != ' ')
        arg_num++;  // ending NULL
    res = mini_calloc(sizeof(char *), arg_num + 1);
    if (res == NULL) {
        mini_printf("error: calloc");
        return NULL;
    }

    int current_arg = 0;
    i               = 0;
    int arg_start   = 0;
    while (s[i] != '\0') {
        if (s[i] == '\n' || s[i] == ' ') {
            s[i]             = '\0';
            res[current_arg] = mini_calloc(sizeof(char), i - arg_start + 1);
            if (res[current_arg] == NULL) {
                mini_printf("error: calloc");
                return NULL;
            }
            mini_strcpy(s + arg_start, res[current_arg]);
            current_arg++;
            arg_start = i + 1;
        }
        i++;
    }

    s[i]             = '\0';
    res[current_arg] = mini_calloc(sizeof(char), i - arg_start + 1);
    if (res[current_arg] == NULL) {
        mini_printf("error: calloc");
        return NULL;
    }
    mini_strcpy(s + arg_start, res[current_arg]);
    res[arg_num] = NULL;
    return res;
}

void exec_line(char *buf) {
    pid_t pid = fork();
    if (pid == -1) {
        mini_printf("error: fork");
        mini_exit();
    }
    if (pid == 0) {
        char **args = parse_args(buf);
        /*printf("%s\n", args[0]);*/
        /*printf("%s\n", args[1]);*/
        if (mini_strlen(args[0]) == 0) {
            return;
        } else if (mini_strcmp(args[0], "cat") == 0) {
            execve("./bin/mini_cat", args, environ);
        } else if (mini_strcmp(args[0], "clean") == 0) {
            execve("./bin/mini_clean", args, environ);
        } else if (mini_strcmp(args[0], "cp") == 0) {
            execve("./bin/mini_cp", args, environ);
        } else if (mini_strcmp(args[0], "echo") == 0) {
            execve("./bin/mini_echo", args, environ);
        } else if (mini_strcmp(args[0], "grep") == 0) {
            execve("./bin/mini_grep", args, environ);
        } else if (mini_strcmp(args[0], "head") == 0) {
            execve("./bin/mini_head", args, environ);
        } else if (mini_strcmp(args[0], "tail") == 0) {
            execve("./bin/mini_tail", args, environ);
        } else if (mini_strcmp(args[0], "touch") == 0) {
            execve("./bin/mini_touch", args, environ);
        } else if (mini_strcmp(args[0], "wc") == 0) {
            execve("./bin/mini_wc", args, environ);
        } else if (mini_strcmp(args[0], "chmod") == 0) {
            execve("./bin/mini_chmod", args, environ);
        } else if (mini_strcmp(args[0], "ln") == 0) {
            execve("./bin/mini_ln", args, environ);
        } else if (mini_strcmp(args[0], "ls") == 0) {
            execve("./bin/mini_ls", args, environ);
        } else if (mini_strcmp(args[0], "mkdir") == 0) {
            execve("./bin/mini_mkdir", args, environ);
        } else if (mini_strcmp(args[0], "mv") == 0) {
            execve("./bin/mini_mv", args, environ);
        } else if (mini_strcmp(args[0], "quickdiff") == 0) {
            execve("./bin/mini_quickdiff", args, environ);
        } else if (mini_strcmp(args[0], "rm") == 0) {
            execve("./bin/mini_rm", args, environ);
        } else if (mini_strcmp(args[0], "rmdir") == 0) {
            execve("./bin/mini_rmdir", args, environ);
        } else {
            mini_printf("not a command: ");
            mini_printf(args[0]);
            mini_printf("\n\n");
            mini_exit();
        }
    } else {
        wait(NULL);
    }
    mini_printf("\n");
}

void print_env() {
    int i = 0;
    while (environ[i]) {
        mini_printf(environ[i]);
        mini_printf("\n");
        i++;
    }
    mini_printf("\n");
}

void print_getenv(char *var) {
    if (var != NULL) {
        int i = 0;
        while (environ[i]) {
            if (mini_strncmp(environ[i], var, mini_strlen(var)) == 0) {
                mini_printf(environ[i]);
                mini_printf("\n\n");
                return;
            }
            i++;
        }
    }
    mini_printf("Not in the environment\n\n");
}

void setenv(char *var) {
    if (var != NULL) {
        int equal_pos = find_str(var, '=');
        if(equal_pos < 0) {
            mini_printf("No environment variable provided\n\n");
            return;
        }
        int i         = 0;
        while (environ[i]) {
            if (mini_strncmp(environ[i], var, equal_pos + 1) == 0
                && environ[i][equal_pos] == '=') {
                mini_strcpy(var, environ[i]);
                mini_printf("\n");
                return;
            }
            i++;
        }
        environ[i] = mini_calloc(BUFSIZE, 1);
        environ[i + 1] = NULL;
        mini_strcpy(var, environ[i]);
    } else {
        mini_printf("No variable provided\n");
    }
    mini_printf("\n");
}

int main(int argc, char **argv) {
    MYFILE *g = mini_fopen("/home/ocisra/.mini_bashrc", 'r');
    if (g != NULL) {
        while (mini_getline(g, buf, BUFSIZE) >= 0) {
            exec_line(buf);
        }
    }

    while (1) {
        mini_scanf(buf, BUFSIZE);
        if (start_with(buf, "exit")) {
            mini_exit();
        }
        if (start_with(buf, "env")) {
            print_env();
            continue;
        }
        if (start_with(buf, "getenv")) {
            char **args = parse_args(buf);
            print_getenv(args[1]);
            continue;
        }
        if (start_with(buf, "export")) {
            char **args = parse_args(buf);
            setenv(args[1]);
            continue;
        }
        exec_line(buf);
    }
}
