#ifndef MINI_LIB
#define MINI_LIB

#define IOBUFFER_SIZE 2048

typedef struct malloc_element{
   
   void * zone_alloue;
   int taille;
   int status;
   struct malloc_element * next_calloc;

} malloc_element;

typedef struct MYFILE
{
    /* data */
    int fd;
    void * buffer_read;
    void * buffer_write;
    int ind_read;
    int ind_write;

} MYFILE;

/* Les prototypes des fonctions de mini_memory.c */
void* mini_calloc(int, int);

void mini_free(void*);

void mini_exit();

/* Les prototypes des fonctions de mini_string.c */
void mini_printf(char *) ;

int mini_scanf( char *, int);

int mini_strlen(char *);

int mini_strcpy(char *, char *);

int mini_strcmp(char*, char*);

void mini_exitString();

/* Les protypes des fonctions de mini_io.c */
MYFILE* mini_fopen(char*, char);

int mini_fread(void*,int, int, MYFILE*);

int mini_fwrite(void*,int, int, MYFILE*);

int mini_fflush(MYFILE*);

int mini_fgetc(MYFILE*);

int mini_fputc(MYFILE*, char);

#endif
