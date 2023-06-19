#include <stdio.h> 
#include <unistd.h>
#include <strings.h>
#include <stdlib.h>
#include <stdio.h>
#include "mini_lib.h"

malloc_element *malloc_list = NULL;

void* mini_calloc(int size_element, int number_element){
   if(size_element < 0){
      puts("error : ");
      return NULL;
   }

   malloc_element *pointeur_element = malloc_list;

   if(malloc_list != NULL){
      /* parcours malloc_list pour ajouter le nouveau malloc_element à la fin*/
      while(pointeur_element->next_calloc != NULL){
         /* réutiliser la zone libérée, si la taille demandée est plus petite ou égale à la taille d’une zone libérée */
         if(pointeur_element->taille <= size_element*number_element && pointeur_element->status == 0){
            /* initialise le buffer avec des ’ \0 ’  */
            printf("%d\n", pointeur_element->status);
            bzero(pointeur_element->zone_alloue, size_element*number_element);
            pointeur_element->status = 1;
            return pointeur_element->zone_alloue;
         }
         else{
            pointeur_element = pointeur_element->next_calloc;
         }

      }
   }
   
   malloc_element *element = sbrk(sizeof(malloc_element));

   if((element->zone_alloue = sbrk(size_element*number_element)) == (void*)(-1)){
      puts("error : ");
      return NULL;
   }
   element->taille =  size_element*number_element;

   /* initialise le buffer avec des ’ \0 ’  */
   bzero(element->zone_alloue, size_element*number_element);
   element->status = 1;
   element->next_calloc = NULL;

   /* ajouter la zone allouée à la liste malloc_list. */
   if(malloc_list == NULL) {
      malloc_list = element;
   }
   else{
      pointeur_element->next_calloc = element;
   }

   return element->zone_alloue;

}

void mini_free(void* ptr){

   malloc_element *current_element = malloc_list;
   
   //cherche l'élément à libérer dans le malloc_list
   while(current_element->zone_alloue != ptr && current_element->next_calloc != NULL){
   	current_element = current_element->next_calloc;
   }

   if(current_element->zone_alloue != NULL && current_element->status == 1){
   	current_element->status = 0;
   }
   
   /* Vérification de fonction */
   // printf("La zone mémoire de %d a été liberée at %p\n", current_element->taille, current_element);
   // puts("done mini_free");
}

void mini_exit(){
   mini_exitString();
   _exit(0);
}
