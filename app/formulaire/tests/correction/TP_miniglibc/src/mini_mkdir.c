#include "mini_lib.h"

#include <sys/stat.h>
#include <unistd.h>


int main(int argc, char *argv[]) {
    if (argc < 2) {
        mini_printf("1 arguments required\n");
        return -1;
    }
    if (mkdir(argv[1], 0755) < 0) {
        mini_printf("error\n");
        return -1;
    }
}
