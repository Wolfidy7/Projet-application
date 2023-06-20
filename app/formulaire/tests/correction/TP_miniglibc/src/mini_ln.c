#include "mini_lib.h"

#include <sys/stat.h>
#include <unistd.h>


int main(int argc, char *argv[]) {
    if (argc < 3) {
        mini_printf("2 arguments required\n");
        return -1;
    }
    if (symlink(argv[1], argv[2]) < 0) {
        mini_printf("error\n");
        return -1;
    }
}
