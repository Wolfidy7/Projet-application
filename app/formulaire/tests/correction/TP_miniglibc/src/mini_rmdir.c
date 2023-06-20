#include "mini_lib.h"

#include <sys/stat.h>
#include <unistd.h>

#define BUFSIZE 512

char buf[BUFSIZE];


int main(int argc, char **argv) {
    if (argc != 2) {
        mini_printf("1 argument necessary\n");
        return 1;
    }

    struct stat stats;
    if (stat(argv[1], &stats) < 0) {
        mini_printf("error\n");
        return -1;
    }

    if (!(stats.st_mode & S_IFDIR)) {
        mini_printf("not a directory\n");
        return -1;
    }

    if (rmdir(argv[1]) < 0) {
        mini_printf("error\n");
        return -1;
    }

    mini_exit();
}
