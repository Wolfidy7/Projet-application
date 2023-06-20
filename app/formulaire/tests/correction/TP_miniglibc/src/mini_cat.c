#include "mini_lib.h"

#define BUFSIZE 512

char buf[BUFSIZE];


int main(int argc, char **argv) {
    if(argc != 2) {
        mini_printf("1 argument necessary\n");
        return 1;
    }

    MYFILE *g = mini_fopen(argv[1], 'r');
    if (g == NULL) {
        mini_printf("error\n");
        return 1;
    }

    int size;
    while (BUFSIZE - 2 == (size = mini_fread(buf, sizeof(char), BUFSIZE - 1, g))) {
        mini_printf(buf);
    }

    mini_exit();
}
