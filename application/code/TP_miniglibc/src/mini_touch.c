#include <stdio.h>
#include <fcntl.h>

int mini_touch(char** argv) {
    for (int i=0; i<1; ++i) {
        open(argv[0], O_CREAT);
    }
}