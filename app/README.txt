1/Gestion de la mémoire:
Exo5: Dans la mémoire il y a des données indéfinies, donc il faut l'initialiser la zone mémoire à '\0'
qu'on veut utiliser pour etre sur que les données qu'on va mettre dans cette zone soient propres.

Exo6: la fonction free libère un bloc précédemment alloué par malloc ou calloc, mais elle ne mettant pas à NULL les pointeurs 
par contre elle indique que la zone de la mémoire est disponible pour pouvoir l'utiliser.

2/Gestion des chaînes de caractère:
Exo17:  si la chaine de caractère ne contient pas de saute de ligne il faut vérifier s'il est la fin de la chaine et quiter.

Exo20: si le nombre de caractères saisis est égal à la taille du buffer ,on ne pourrai pasindiquer la fin du buffer donc il faut lire la chaine saisie jusqu'à (size_buffer-1) pour laisser le 1 pour '\0'

Exo22: le problème des fonctions
mini_strcpy :  Cette fonction s'effectue sans vérifier que la taille du buffer ne soit pas dépassée. 
solution: on copie la chaine de source jusqu'à la taille de la chaine de destination.

 