#include <stdio.h>
#include "mini_lib.h"

int mini_echo(char **argv) {
    int i = 0;
    while(argv[i] != '\0'){
        mini_printf(argv[i]);
        mini_printf(" ");
        i++;
    }
    mini_exit();
}