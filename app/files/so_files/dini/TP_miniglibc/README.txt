TP 1: Mini-GLIBC, commandes syst�me et SHELL

Nom�: BINTI MOHAMAD Nurdini
Groupe�: 3A STI � TP1

1 Mini-GLIBC : Biblioth�que
1.1 Gestion de la m�moire

Exercice 5
On initialise le buffer � \0 pour montrer qu�il a �t� allou�.

Exercice 6
La fonction free lib�re un bloc de m�moire allou� dynamiquement dans le tas, via un appel � la fonction malloc(), calloc(), realloc(). Il est probablement le cas qu�il pointe toujours vers la m�me m�moire. La seule chose ayant disparu est la variable de pointeur qu�on ait pointant sur la m�moire allou�e.

1.2 Gestion des cha�nes de caract�res

Exercice 17
On constate que s�il n�y a pas saut de ligne, la caract�res suivant sera pass� en m�me ligne. Cela est normal ce qui fait le printf.


Exercice 20
Pour la fonction mini_scanf, si le nombre saisis est �gal � la taille de buffer, on va repasser 

Exercice 22
En terme de s�curit�, la cha�ne pass� en param�tre n�est pas s�curis�. C�est mieux de le mettre en tant qu�un constant.



