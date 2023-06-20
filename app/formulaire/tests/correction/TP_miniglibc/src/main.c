#include "mini_lib.h"

// pour les tests avant d'avoir mini_printf()
#include <stdio.h>

/*
// on a pas encore mini_printf() donc on utilise printf() pour les test
int main (int argc, char **argv) {
    int *test1 = mini_calloc(sizeof(int), 10);
    if (test1 == NULL) {
        return 1;
    }

    int *test2 = mini_calloc(sizeof(int), 5);
    if (test2 == NULL) {
        return 1;
    }

    printf("test1 : %p\n", test1);
    printf("test2 : %p\n", test2);

    mini_free(test1);
    mini_free(test2);

    int *test3 = mini_calloc(sizeof(int), 11); // should use a new address
    int *test4 = mini_calloc(sizeof(int), 7); // should reuse test1 memory
    int *test5 = mini_calloc(sizeof(int), 3); // should reuse test2 memory

    if (test3 == NULL) {
        return 1;
    }

    if (test4 == NULL) {
        return 1;
    }

    if (test5 == NULL) {
        return 1;
    }

    printf("test3 : %p\n", test3);
    printf("test4 : %p\n", test4);
    printf("test5 : %p\n", test5);
    mini_exit();
}
*/

/*
int main(int arg, char **argv) {
    char *buf;
    buf = mini_calloc(sizeof(char), 10);
    mini_scanf(buf, 10);
    mini_printf(buf);
    mini_exit();
}
*/

/*
int main(int argc, char **argv) {
    printf("6 = %i\n", mini_strlen("azerty"));
    char a[5] = "baba";
    char b[5];
    mini_strcpy(a, b);
    printf("baba = %s\n", b);
    printf("0 = %i\n", mini_strcmp(a, b));
    mini_exit();
}
*/

int main (int argc, char **argv) {
    MYFILE *f = mini_fopen("/home/ocisra/README.md", 'r');
    char buf[10]; 
    mini_fread(buf, 1, 10, f);
    mini_printf(buf);

    char buf2[10] = "testbabar";
    MYFILE *g = mini_fopen("/home/ocisra/buuuf", 'w');
    mini_fwrite(buf2, 1, 10, g);

    char c = mini_fgetc(f);
    char buf3[2];
    buf3[0] = c;
    buf3[1] = '\0';
    mini_printf(buf3);

    mini_fputc(g, 'p');

    mini_exit();
}
