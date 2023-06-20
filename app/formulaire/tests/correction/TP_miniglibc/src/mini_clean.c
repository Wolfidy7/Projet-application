#include "mini_lib.h"

int main(int argc, char **argv) {
    if (argc != 2) {
        mini_printf("1 arguments necessary\n");
        return 1;
    }

    MYFILE *g = mini_fopen(argv[1], 'w');
    if (g == NULL) {
        mini_printf("error\n");
        return 1;
    }
    
    mini_exit();
}
