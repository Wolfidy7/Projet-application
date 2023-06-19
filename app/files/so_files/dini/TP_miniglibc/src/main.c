#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
#include "mini_lib.h"

#define IOBUFFER_SIZE 2048

int main(int agrc, char **agrv){
    puts("main\n");

    /* L'implémentation pour tester la fonction mini_calloc et mini_free*/
    int *buffer = (int *) mini_calloc(sizeof(int), 4);

    if (buffer != NULL)
        printf("Allocated 4 long integer at %p\n\n", buffer);
    else
        printf("Cannot allocated memory\n\n");

    /* Exercice 17: L'implémentation de fonction mini_printf */
    mini_printf("Testing mini_printf without line break");

    mini_printf("Testing mini_printf with line break\n");

    /* Exercice 19: L'implémentation de fonction mini_scanf */
    char *firstName = (char *) mini_calloc(sizeof(char), 15);
    char *fitName = (char *) mini_calloc(sizeof(char), 15);
    char *fstName = (char *) mini_calloc(sizeof(char), 15);
    char *lastName = (char *) mini_calloc(sizeof(char), 15);
    int fullSize;

    mini_printf("Please enter your first name :\n");
    mini_scanf(firstName, 5);

    mini_printf("Please enter your last name :\n");
    mini_scanf(lastName, 15);
    //mini_scanf(lastName, 15);

    /* The last +1 is for the last nul ASCII code for the string */
    fullSize = mini_strlen( firstName ) + 1 +  mini_strlen( lastName ) + 1;

    /* Memory allocation and copy */
    char *fullName = (char *) mini_calloc(sizeof(char), fullSize);

    printf( "Full name is: %s%s\n\n", firstName, lastName);
    int compare = mini_strcmp( firstName, lastName );
    printf( "Compare value before mini_strcpy: %d\n\n", compare);

    mini_strcpy( firstName, lastName );
    compare = mini_strcmp( firstName, lastName );
    printf( "Compare value after mini_strcpy: %d\n\n", compare);
    

    /* Exercice 29: L'implémentation de fonction mini_fopen ett mini_fread */ 
    MYFILE *inputFile = mini_fopen( "../README.txt", 'r');

    if(inputFile == NULL){
        printf("fopen() ERROR\n");
    }

    char buff[100];
    mini_fread(buff, 1, 500, inputFile);
    printf("\nThe bytes read are :\n[\n%s\n]\n",buff);

    /* Exercice 31: L'implémentation de fonction mini_fwrite */ 
    char buffe[ 100 ];
    int returnCode;
    int index;

    FILE * stream = fopen( "../test_file/fileToWrite.txt", "w" );
    if ( stream == NULL ) {
        printf("Cannot open file for writing\n" );
        exit( -1 );
    }

    for( index=0; index<1000; index++ ) {
        if ( 1 != fwrite( buffe, 10, 1, stream ) ) {
            fprintf( stderr, "Cannot write block in file\n" );
        }
    }

    mini_free(buffer);
    mini_free(firstName);
    mini_free(lastName);
    mini_free(fullName);
    mini_exit();

}