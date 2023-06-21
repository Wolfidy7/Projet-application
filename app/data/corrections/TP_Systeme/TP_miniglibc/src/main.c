#include <stdio.h>
#include "fonction.h"

int main() {
    // Exécution des fonctions
    int sum = addition(3, 5);
    int fact = factoriel(5);
    float div = division(10.0, 3.0);
    printf("%d",sum);

    return 0;
}
