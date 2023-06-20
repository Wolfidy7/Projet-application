#include "mini_lib.h"

#include <stdio.h>

#define BUFSIZE 512

char buf1[BUFSIZE + 1];
char buf2[BUFSIZE + 1];

int main(int argc, char **argv) {
    if (argc != 3) {
        mini_printf("2 argument necessary\n");
        return 1;
    }

    MYFILE *f = mini_fopen(argv[1], 'r');
    if (f == NULL) {
        mini_printf("error\n");
        return 1;
    }

    MYFILE *g = mini_fopen(argv[2], 'r');
    if (g == NULL) {
        mini_printf("error\n");
        return 1;
    }


    while(mini_getline(f, buf1, BUFSIZE) > 0) {
        if(mini_getline(g, buf2, BUFSIZE) < 0) {
            break;
        }
        if(mini_strcmp(buf1, buf2) != 0) {
            mini_printf(buf1);
            mini_printf("\n");
        }
    }

    mini_exit();
}
