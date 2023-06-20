#include <stdio.h>
#include "fonction.h"

int main() {
    // Exécution des fonctions
    int sum = addition(3, 5);
    int fact = factoriel(5);
    float div = division(10.0, 3.0);

    // Écriture des résultats dans un fichier
    FILE *file = fopen("../../result/resultats_etudiant.txt", "w");
    if (file != NULL) {
        fprintf(file, "Résultat de l'addition : %d\n", sum);
        fprintf(file, "Factoriel de 5 : %d\n", fact);
        fprintf(file, "Résultat de la division : %f\n", div);
        fclose(file);
        printf("Les résultats ont été écrits dans le fichier 'resultats_etudiant.txt'.\n");
    } else {
        printf("Erreur lors de l'ouverture du fichier.\n");
    }


    return 0;
}
