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

    int lines = 0;
    int size;
    while (BUFSIZE - 2 == (size = mini_fread(buf, sizeof(char), BUFSIZE - 1, g))) {
        for (int i = 0; i < size + 1; i++) {
            if(buf[i] == '\n') {
                lines++;
            }
        }
    }

    /// itos
    // get the number of caracters
    int length = 1;
    int i = lines;
    while((i /= 10) > 0) {
        length++;
    }

    char *str = mini_calloc(sizeof(char), length + 1);
    str[length] = '\0';

    for(i = 0; i < length; i++) {
        str[length - i - 1] = (lines % 10) + '0';
        lines /= 10; 
    }
    mini_printf(str);

    mini_exit();
}
