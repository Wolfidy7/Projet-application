#include <stdio.h>
#include "mini_lib.h"

void mini_cat(char *argv) {
    MYFILE* file = (MYFILE*)mini_calloc(sizeof(MYFILE), 1);

    char* buff = (char*)mini_calloc(1, IOBUFFER_SIZE);
    file = mini_fopen(argv[0], 'r');
    int r = mini_fread(buff, 1, IOBUFFER_SIZE, file);
    mini_printf(buff);
    
    mini_exit();
}