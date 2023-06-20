#ifndef MINI_LIB_H
#define MINI_LIB_H

#include <stddef.h>
#include <errno.h>

struct MYFILE {
    int fd;
    void *buffer_read;
    void *buffer_write;
    int ind_read;
    int ind_write;
    struct MYFILE *next;
};

typedef struct MYFILE MYFILE;

extern MYFILE *myfile_list;

void* mini_calloc(int size_element, int number_element);
void mini_free(void* ptr);
void mini_exit();

void mini_printf(char *str);
int mini_scanf(char* buffer, int size_buffer);
int mini_strlen(char* s);
int mini_strcpy(char* s, char *d);
int mini_strncpy(char* d, char *s, int n);
int mini_strncat(char *d, char *s, int n);
int mini_strcmp(char* s1, char* s2);
int mini_strncmp(char *s1, char *s2, int n);
char *mini_itoa(int lines);
int mini_atoi(char *lines, int base);
int find_str(char *buf, char c);

MYFILE* mini_fopen(char* file, char mode);
int mini_fread(void* buffer,int size_element, int number_element, MYFILE* file);
int mini_fwrite(void* buffer,int size_element, int number_element, MYFILE* file);
int mini_fflush(MYFILE* file);
int mini_fclose(MYFILE *file);
int mini_fgetc(MYFILE* file);
int mini_fputc(MYFILE* file, char c);
int mini_getline(MYFILE *file, char *buf, int BUFSIZE);

extern char *buffer;
extern int ind;

#endif  // MINI_LIB_H