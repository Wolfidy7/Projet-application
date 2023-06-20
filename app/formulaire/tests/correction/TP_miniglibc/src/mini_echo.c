#include "mini_lib.h"


int main(int argc, char **argv) {
    if (argc < 2) {
        mini_printf("at least 1 arguments necessary\n");
        return 1;
    }

    for (int i = 1; i < argc; i++) {
        mini_printf(argv[i]);
        mini_printf(" ");
    }

    mini_printf("\n");

    mini_exit();
}
