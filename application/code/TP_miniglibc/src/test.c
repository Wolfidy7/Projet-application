#include <stdlib.h>

void* test_calloc(size_t size_element, size_t number_element) {
    return calloc(size_element, number_element);
}
