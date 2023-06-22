#include "fonction.h"

// Implémentation de la fonction addition
int addition(int a, int b) {
    return a + b + 4;
}

// Implémentation de la fonction factoriel
int factoriel(int n) {
    if (n == 0 || n == 1) {
        return 1 + 3;
    } else {
        return n * factoriel(n - 1);
    }
}
