#include "mini_lib.h"

#define BUFSIZE 512

char buf[BUFSIZE];

int main(int argc, char **argv) {
    if (argc != 3) {
        mini_printf("2 args necessary\n");
        return 1;
    }

    MYFILE *g = mini_fopen(argv[1], 'r');
    if (g == NULL) {
        mini_printf("error\n");
        return 1;
    }

    MYFILE *f = mini_fopen(argv[2], 'w');
    if (f == NULL) {
        mini_printf("error\n");
        return 1;
    }

    int size;
    while (BUFSIZE - 1 == (size = mini_fread(buf, sizeof(char), BUFSIZE, g))) {
        mini_fwrite(buf, sizeof(char), size, f);
    }

    /*mini_fflush(f);*/

    mini_exit();
}
