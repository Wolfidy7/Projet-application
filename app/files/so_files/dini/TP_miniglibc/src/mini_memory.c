#include "mini_lib.h"

#include <stdio.h>
#include <unistd.h>

struct malloc_element {
    void *mem;
    int size;
    int state;
    struct malloc_element *next;
};

typedef struct malloc_element malloc_element;


malloc_element *malloc_list = NULL;

void *mini_calloc(int size_element, int number_element) {
    if (size_element <= 0 || number_element <= 0) {
        return NULL;
    }

    // reuse freed memory if possible
    malloc_element *element = malloc_list;
    while (element != NULL) {
        if (element->state == 0 && element->size >= size_element * number_element) {
            element->state = 1;
            char *ptrc     = (char *)element->mem;
            for (int i = 0; i < size_element * number_element; i++) {
                ptrc[i] = '\0';
            }
            return element->mem;
        }

        element = element->next;
    }


    void *ptr = sbrk(size_element * number_element);
    if (ptr == (void *)-1) {
        mini_printf("sbrk error\n");
        return NULL;
    }
    char *ptrc = (char *)ptr;
    for (int i = 0; i < size_element * number_element; i++) {
        ptrc[i] = '\0';
    }

    element = sbrk(sizeof(malloc_element));
    if ((void *)element == (void *)-1) {
        mini_printf("sbrk error\n");
        sbrk(-size_element * number_element);  // free allocated memory
        return NULL;
    }
    element->mem   = ptr;
    element->size  = size_element * number_element;
    element->state = 1;
    element->next  = malloc_list;

    malloc_list = element;

    return ptr;
}

void mini_free(void *ptr) {
    malloc_element *element = malloc_list;

    while (element->mem != ptr) {
        element = element->next;
        if (element == NULL) {
            return;
        }
    }
    element->state = 0;
    return;
}

void mini_exit() {
    if (write(STDOUT_FILENO, buffer, ind) == -1) {
        /*mini_printf("write2\n");*/
        /*return;*/
    }
    MYFILE *file = myfile_list;
    MYFILE *next_file;
    while(file != NULL) {
        next_file = file->next;
        mini_fclose(file);
        file = next_file;
    }

    _exit(0);
}