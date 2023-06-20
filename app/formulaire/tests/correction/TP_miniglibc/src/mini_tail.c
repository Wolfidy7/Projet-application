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
    int max_lines = 1; // 1 more for the rotation
    for (int i = 0; i < length; i++) {
        int tmp = 1;
        for (int j = 0; j < length - i - 1; j++) {
            tmp *= 10;
        }
        tmp *= argv[2][i] - '0';
        max_lines += tmp;
    }


    /// buffer keeping the index of the first char of the last 'max_lines' lines
    int *line_buf = mini_calloc(sizeof(int), max_lines);
    int index     = 0;

    /// first pass to determine from where to print
    int size;
    int lines = 0;
    int i = 0;
    int old_i = 0;
    while (BUFSIZE - 2 == (size = mini_fread(buf, sizeof(char), BUFSIZE - 1, g))) {
        old_i += i;
        for (i = 0; i < size + 1; i++) {
            if (buf[i] == '\n') {
                int line        = i + old_i;
                line_buf[index] = line;
                index++;
                if (index == max_lines) {
                    // overwrite the first line that we now know is unwanted
                    index = 0;
                }
                lines++;
            }
        }
    }

    // close and reopen to be at the beginning of the file again 
    // will break if file is modified between the fopens
    mini_fclose(g);
    g = mini_fopen(argv[3], 'r');
    if (g == NULL) {
        mini_printf("error\n");
        return 1;
    }


    /// second pass to print from the deterined index onward
    old_i = 0;
    while (BUFSIZE - 2 == (size = mini_fread(buf, sizeof(char), BUFSIZE - 1, g))) {
        if(old_i + size < line_buf[index]) {
            old_i += size;
            continue;
        }
        mini_printf(buf + line_buf[index] - old_i);
        old_i = line_buf[index];
    }


    mini_exit();
}
