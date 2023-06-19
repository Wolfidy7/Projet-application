#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <errno.h>
#include <sys/types.h>
#include <fcntl.h> 
#include <unistd.h>
#include <unistd.h>
#include <sys/syscall.h>

#include "mini_lib.h"
#define BUF_SIZE 1024

char *buffer;
int ind = -1; // -1 specifie que le buffer n'a pas encore été instancié

void mini_printf(char *msg){

	if(ind == -1) {
        buffer = mini_calloc(sizeof(char), BUF_SIZE - 8);
        if(buffer == NULL){
            printf("ERROR");
            exit(EXIT_FAILURE);
        }
        ind=0;
    }

    for(int i=0; msg[i] != '\0'; i++){
        buffer[ind] = msg[i];
        ind++;
        if( msg[i] == '\n' || ind == BUF_SIZE) {
            if(write(STDOUT_FILENO, buffer, ind) == -1) {
                printf("ERROR printf");  
            }
			ind = 0;
        }
     
    }
    

}

int mini_scanf(char *buffer, int size_buffer){

	if (read(0, buffer, size_buffer)==-1){
		puts ("Erreur lors de la lecture");
		return -1;
	}

}

int mini_strlen(char *s){
 
	int counter = 0;
	for(int i=0; s[i]!='\0'; i++){
		counter++;
	}
	return counter;

}

int mini_strcpy(char *s, char *d){
    while( (*(d++) = *(s++)) != '\0');
	return mini_strlen(d);
}

int mini_strcmp(char* s1, char* s2){

	if(mini_strlen(s1) != mini_strlen(s2)) 
		return -1; 
	
	for(int i=0; i< mini_strlen (s1); i++)
		if (s1[i] != s2[i])
			return -1;

	return 0;

}	

void mini_exitString(){
    /* forcer l'execution de buffer */
    if(ind > 0){
        if(write(STDOUT_FILENO, buffer, ind) == -1) 
            printf("ERROR printf");  
    }
    mini_free(buffer);
}