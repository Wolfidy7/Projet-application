TP 1: Mini-GLIBC, commandes système et SHELL

Nom : BINTI MOHAMAD Nurdini
Groupe : 3A STI – TP1

1 Mini-GLIBC : Bibliothèque
1.1 Gestion de la mémoire

Exercice 5
On initialise le buffer à \0 pour montrer qu’il a été alloué.

Exercice 6
La fonction free libère un bloc de mémoire alloué dynamiquement dans le tas, via un appel à la fonction malloc(), calloc(), realloc(). Il est probablement le cas qu’il pointe toujours vers la même mémoire. La seule chose ayant disparu est la variable de pointeur qu’on ait pointant sur la mémoire allouée.

1.2 Gestion des chaînes de caractères

Exercice 17
On constate que s’il n’y a pas saut de ligne, la caractères suivant sera passé en même ligne. Cela est normal ce qui fait le printf.


Exercice 20
Pour la fonction mini_scanf, si le nombre saisis est égal à la taille de buffer, on va repasser 

Exercice 22
En terme de sécurité, la chaîne passé en paramètre n’est pas sécurisé. C’est mieux de le mettre en tant qu’un constant.



