#include "mini_lib.h"

#include <sys/stat.h>


int main(int argc, char *argv[]) {
    if (argc < 3) {
        mini_printf("2 arguments required\n");
        return -1;
    }
    int perm = mini_atoi(argv[1], 8);
    if (chmod(argv[2], perm) < 0) {
        mini_printf("error\n");
        return -1;
    }
}
