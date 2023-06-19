#include <sys/stat.h>
#include <stdio.h>
#include <fcntl.h>
#include <stddef.h>
#include "mini_lib.h"

/* Pour verifier si c'est un répertoire */
int isDirectory(const char *path) {
   struct stat statbuf;
   if (stat(path, &statbuf) != 0)
       return 0;
       /* This macro returns non-zero if the file is a directory.  */
   return S_ISDIR(statbuf.st_mode);
}

int main(int argc, char** argv) {

    if (argc < 3) {
        mini_printf("mini_cp: missing file operand");
        mini_exit();
    }  else if (argc > 3) {
        mini_printf("mini_cp: too many target");
        mini_exit();
    }


    MYFILE* src = mini_fopen(argv[1], 'r');

    if( src == NULL ){
        printf("mini_cp: cannot stat '%s': No such file or directory\n", argv[1]);
        mini_exit();
    }

    /* Si la deuxième argument est un répertoire */
    /* On va créer un fichier avec le même nom */
    if(isDirectory(argv[2]) != 0){
        // const char *fileSource = argv[1];
        // printf("test : %s\n", &fileSource[-2]);
        // char* buffer = (char *)mini_calloc(sizeof(char), mini_strlen(argv[1]));
        // char* newFile;
        // int ind = 0;
        // for(int i=0;i<mini_strlen(fileSource);i++){
        //     printf("%s\n", &argv[1][i]);
        //     buffer[ind] = fileSource[i];
        //     ind++;
        //     if(fileSource[i]=='/'){
        //         printf("for :%s", buffer);
        //         ind = 0;
        //         newFile = buffer;
        //         mini_free(buffer);
        //     }
        // }
        char* file = "testCopy.txt";
        char* buffer = argv[2]+ file;

        open(buffer, O_CREAT);
    }

    printf("test\n");
    MYFILE* dst = mini_fopen(argv[2], 'w');
    
    if( dst != NULL ){
        printf("mini_cp: cannot stat '%s': No such file or directory", argv[2]);
        mini_exit();
    }
    printf("test\n");

    char* buffer = (char*)mini_calloc(1, IOBUFFER_SIZE);
    
    int read = mini_fread(buffer, 1, IOBUFFER_SIZE, src);
    
    printf("%d\n", dst->ind_write);
    
    mini_fwrite(buffer, 1, read, dst);

    mini_exit();

}