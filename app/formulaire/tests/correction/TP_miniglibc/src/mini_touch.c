#include "mini_lib.h"

int main(int argc, char **argv) {
    if(argc != 2) {
        mini_printf("1 argument needed\n");
        return 1;
    }

    MYFILE *f = mini_fopen(argv[1], 'a');
    if (f == NULL) {
        mini_printf("error\n");
        return 1;
    }


    mini_exit();
}
