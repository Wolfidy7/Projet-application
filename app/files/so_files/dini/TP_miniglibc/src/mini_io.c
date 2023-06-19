#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <errno.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>

#include "mini_lib.h"
#define IOBUFFER_SIZE 2048

MYFILE* mini_fopen(char* file, char mode){

    MYFILE *fichier = (MYFILE *)mini_calloc(sizeof(MYFILE), IOBUFFER_SIZE);
    switch (mode)
    {
        case 'r':
            fichier->fd = open(file, O_RDONLY);
            break;
        case 'w':
            fichier->fd = open(file, O_WRONLY);
            break;
        case 'a':
            fichier->fd = open(file, O_APPEND);
            break;
        case 'b':
            fichier->fd = open(file, O_RDWR);
            break;
        default:
            puts("Mode non supporté");
            break;
    }
    
    if(fichier->fd == -1) return NULL;
    else return fichier;

}

int mini_fread(void* buffer,int size_element, int number_element, MYFILE* file){

    file->ind_read = 0;
    file->buffer_read = mini_calloc(sizeof(char), IOBUFFER_SIZE);
    
    if(read(file->fd, file->buffer_read, IOBUFFER_SIZE)==-1)
        return -1;

    for(int i=0; i<size_element*number_element; i++){
        ((char*)buffer)[i] = ((char *)file->buffer_read)[i];
        file->ind_read++;
    }
    
    return mini_strlen(file->buffer_read);
    
}

int mini_fwrite(void* buffer,int size_element, int number_element, MYFILE* file){
    printf("test fwite\n");
    file->ind_write = 0;
    printf("test fwite\n");
    file->buffer_write = mini_calloc(sizeof(char), IOBUFFER_SIZE);
    printf("test fwite\n");
    for(int i=0; i<size_element*number_element; i++){
        ((char*)buffer)[i] = ((char *)file->buffer_write)[i] ;
        file->ind_write++;
    }

    printf("test fwite\n");
    if(mini_strlen(buffer) == IOBUFFER_SIZE){
        if(write(file->fd, file->buffer_write, IOBUFFER_SIZE)==-1)
            return -1;
    }
    
    return mini_strlen(file->buffer_write);

}

int mini_fflush(MYFILE* file) {
    int toWrite;

    toWrite = write(file->fd, file->buffer_write, file->ind_write);
    file->ind_write = 0;
    return toWrite;
}

int mini_fgetc(MYFILE* file) {
    char* buffer = (char *)mini_calloc(1, 2);

    buffer[1] = '\0';
    if (mini_fread(buffer,1, 1, file) != 1) {
        return -1;
    } else {
        return buffer[0];
    }
}

int mini_fputc(MYFILE * file, char c) {
    char* buffer = (char*)mini_calloc(1, 2);
    buffer[0] = c;
    buffer[1] = '\0';
    if (mini_fwrite(buffer, 1, 1, file) != 1) {
        return -1;
    } else {
        return c;
    }
}