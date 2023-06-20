#include "mini_lib.h"

#include <fcntl.h>
#include <unistd.h>

#define IOBUFFER_SIZE 2048

MYFILE *myfile_list = NULL;

MYFILE *mini_fopen(char *file, char mode) {
    int flag;
    mode_t m = S_IWUSR | S_IRUSR;
    switch (mode) {
    case 'a': flag = O_APPEND | O_CREAT | O_RDONLY; break;
    case 'b': flag = O_RDWR | O_CREAT; break;
    case 'r': flag = O_RDONLY; break;
    case 'w': flag = O_WRONLY | O_CREAT | O_TRUNC; break;
    }
    int fd = open(file, flag, m);
    if (fd == -1) {
        mini_printf("error : fopen\n");
        return NULL;
    }

    MYFILE *myfile = mini_calloc(sizeof(MYFILE), 1);
    if (myfile == NULL) {
        mini_printf("error : fopen\n");
        return NULL;
    }
    myfile->fd           = fd;
    myfile->buffer_read  = NULL;
    myfile->buffer_write = NULL;
    myfile->ind_read     = -1;
    myfile->ind_write    = -1;

    myfile->next = myfile_list;
    myfile_list  = myfile;

    return myfile;
}

int mini_fread(void *buffer, int size_element, int number_element, MYFILE *file) {
    if (file->ind_read == -1) {
        file->buffer_read = mini_calloc(1, IOBUFFER_SIZE);
        if (file->buffer_read == NULL) {
            mini_printf("error : fread\n");
            return -1;
        }
        int ret = read(file->fd, file->buffer_read, IOBUFFER_SIZE);
        if (ret == -1) {
            mini_printf("error : fread\n");
            return -1;
        }
        file->ind_read = 0;
    }

    char *buf = buffer;
    int i;
    for (i = 0; i < size_element * number_element - 1; i++) {
        buf[i] = ((char *)file->buffer_read)[file->ind_read];
        file->ind_read++;
        if (file->ind_read == IOBUFFER_SIZE) {
            int ret = read(file->fd, file->buffer_read, IOBUFFER_SIZE);
            if (ret == -1) {
                mini_printf("error : fread\n");
                return -1;
            }
            if (ret < IOBUFFER_SIZE - 1) {
                // eof
                return i;
            }
            file->ind_read = 0;
        }
    }
    return i;
}

int mini_fwrite(void *buffer, int size_element, int number_element, MYFILE *file) {
    if (file->ind_write == -1) {
        file->buffer_write = mini_calloc(1, IOBUFFER_SIZE);
        if (file->buffer_write == NULL) {
            mini_printf("error : fwrite\n");
            return -1;
        }
        file->ind_write = 0;
    }

    char *buf = file->buffer_write;
    int i;
    for (i = 0; i < size_element * number_element; i++) {
        buf[file->ind_write] = ((char *)buffer)[i];
        file->ind_write++;
        if (file->ind_write == IOBUFFER_SIZE) {
            int ret = write(file->fd, file->buffer_write, IOBUFFER_SIZE);
            if (ret == -1) {
                mini_printf("error : fwrite\n");
                return -1;
            }
            file->ind_write = 0;
        }
    }
    return i;
}

int mini_fflush(MYFILE *file) {
    if (file->buffer_write == NULL) {
        return -1;
    }
    int ret = write(file->fd, file->buffer_write, file->ind_write + 1);
    if (ret == -1) {
        mini_printf("error : fflush\n");
        return -1;
    }
    file->ind_write = 0;
    return ret;
}

int mini_fclose(MYFILE *file) {
    mini_fflush(file);
    int ret = close(file->fd);
    if (ret == -1) {
        mini_printf("error: fclose\n");
        return -1;
    }

    // remove from file list
    if (myfile_list == file) {
        myfile_list = myfile_list->next;
    } else {
        MYFILE *file_list_iterator = myfile_list;
        while (file_list_iterator != NULL) {
            if (file_list_iterator->next == file) {
                file_list_iterator->next = file->next;
            }
        }
    }
    mini_free(file);
    return 0;
}


int mini_fgetc(MYFILE *file) {
    if (file->ind_read == -1) {
        file->buffer_read = mini_calloc(1, IOBUFFER_SIZE);
        if (file->buffer_read == NULL) {
            mini_printf("error : fread\n");
            return -1;
        }
        int ret = read(file->fd, file->buffer_read, IOBUFFER_SIZE);
        if (ret == -1) {
            mini_printf("error : fread\n");
            return -1;
        }
        file->ind_read = 0;
    }

    char c = ((char *)file->buffer_read)[file->ind_read];
    file->ind_read++;
    if (file->ind_read == IOBUFFER_SIZE) {
        int ret = read(file->fd, file->buffer_read, IOBUFFER_SIZE);
        if (ret == -1) {
            mini_printf("error : fread\n");
            return -1;
        }
        file->ind_read = 0;
    }

    return c;
}

int mini_fputc(MYFILE *file, char c) {
    if (file->ind_write == -1) {
        file->buffer_write = mini_calloc(1, IOBUFFER_SIZE);
        if (file->buffer_write == NULL) {
            mini_printf("error : fwrite\n");
            return -1;
        }
        file->ind_write = 0;
    }

    char *buf            = file->buffer_write;
    buf[file->ind_write] = c;
    file->ind_write++;
    if (file->ind_write == IOBUFFER_SIZE) {
        int ret = write(file->fd, file->buffer_write, IOBUFFER_SIZE);
        if (ret == -1) {
            mini_printf("error : fwrite\n");
            return -1;
        }
        file->ind_write = 0;
    }
    return 0;
}

int mini_getline(MYFILE *file, char *buf, int BUFSIZE) {
    char bufc;
    int index = 0;
    while ((bufc = mini_fgetc(file)) > 0) {
        if (bufc == '\n') {
            buf[index] = '\0';
            return index;
        } else
            buf[index] = bufc;
        index++;
        if (index >= BUFSIZE)
            return index;
    }
    return -1;
}
