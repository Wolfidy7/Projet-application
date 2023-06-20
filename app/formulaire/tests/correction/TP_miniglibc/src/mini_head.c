#include "mini_lib.h"

#define BUFSIZE 512

char buf[BUFSIZE];


int main(int argc, char **argv) {
    if (argc != 4) {
        mini_printf("3 arguments necessary\n");
        return 1;
    }

    if (mini_strcmp(argv[1], "-n")) {
        mini_printf("-n flag only is supported\n");
        return 1;
    }

    MYFILE *g = mini_fopen(argv[3], 'r');
    if (g == NULL) {
        mini_printf("error\n");
        return 1;
    }

    /// stoi
    int length    = mini_strlen(argv[2]);
    int max_lines = 0;
    for (int i = 0; i < length; i++) {
        int tmp = 1;
        for (int j = 0; j < length - i - 1; j++) {
            tmp *= 10;
        }
        tmp *= argv[2][i] - '0';
        max_lines += tmp;
    }

    int size;
    int lines = 0;
    while (BUFSIZE - 2 == (size = mini_fread(buf, sizeof(char), BUFSIZE - 1, g))) {
        for (int i = 0; i < size + 1; i++) {
            if (buf[i] == '\n') {
                lines++;
            }
            if (lines >= max_lines) {
                buf[i] = '\0';
                mini_printf(buf);
                mini_exit();
            }
        }
        mini_printf(buf);
    }

    mini_exit();
}
