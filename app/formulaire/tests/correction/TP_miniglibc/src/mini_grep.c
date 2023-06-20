#include "mini_lib.h"

#define BUFSIZE 512

char buf[BUFSIZE];


int find_in(char *s, char *query) {
    int len = mini_strlen(query);

    for (int i = 0; s[i] != '\0'; i++) {
        for (int j = 0; j < len; j++) {
            if (s[i + j] != query[j]) {
                break;
            }
            if (j == len - 1) {
                return 1;
            }
            if(s[i + j] == '\0') {
                return 0;
            }
        }
    }
    return 0;
}

int main(int argc, char **argv) {
    if (argc != 3) {
        mini_printf("2 argument necessary\n");
        return 1;
    }

    MYFILE *g = mini_fopen(argv[2], 'r');
    if (g == NULL) {
        mini_printf("error\n");
        return 1;
    }

    int linebuf_size = 128;
    char *linebuf    = mini_calloc(sizeof(char), linebuf_size);
    int line_index   = 0;

    char c;
    while ((c = mini_fgetc(g)) != '\0') {
        linebuf[line_index] = c;
        line_index++;
        if (line_index == linebuf_size) {
            linebuf_size *= 2;  // if buffer is full, increase it's size
            char *linebufbuf = mini_calloc(sizeof(char), linebuf_size);
            mini_strcpy(linebuf, linebufbuf);
            mini_free(linebuf);
            linebuf = linebufbuf;
        }
        if (c == '\n') {
            linebuf[line_index] = '\0';
            if (find_in(linebuf, argv[1])) {
                mini_printf(linebuf);
            }
            line_index = 0;
        }
    }

    mini_exit();
}
