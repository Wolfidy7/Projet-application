#include "mini_lib.h"

#include <stdio.h>
#include <unistd.h>

#define BUF_SIZE 1024

char *buffer;
int ind = -1;

char *mini_itoa(int lines) {
    /// itoa
    int length = 1;
    int i      = lines;
    while ((i /= 10) > 0) {
        length++;
    }

    char *str   = mini_calloc(sizeof(char), length + 1);
    str[length] = '\0';

    for (i = 0; i < length; i++) {
        str[length - i - 1] = (lines % 10) + '0';
        lines /= 10;
    }
    return str;
}

int mini_atoi(char *lines, int base) {
    int length    = mini_strlen(lines);
    int max_lines = 0;
    for (int i = 0; i < length; i++) {
        int tmp = 1;
        for (int j = 0; j < length - i - 1; j++) {
            tmp *= base;
        }
        tmp *= lines[i] - '0';
        max_lines += tmp;
    }
    return max_lines;
}

void mini_printf(char *str) {
    if (ind < 0) {
        ind = 0;
        if ((buffer = mini_calloc(sizeof(char), BUF_SIZE)) == NULL) {
            mini_printf("empty buffer\n");
            return;
        }
    }
    int i;
    for (i = 0; str[i] != '\0'; i++) {
        buffer[ind] = str[i];
        if (str[i] == '\n' || ind + 1 == BUF_SIZE) {
            if (write(STDOUT_FILENO, buffer, ind + 1) == -1) {
                mini_printf("write1\n");
                return;
            }
            ind = 0;
        } else
            ind++;
    }
    buffer[ind] = str[i];
    if (write(STDOUT_FILENO, buffer, ind + 1) == -1) {
        mini_printf("write1\n");
        return;
    }
    ind = 0;
}

int mini_scanf(char *buffer, int size_buffer) {
    if (size_buffer <= 0 || buffer == NULL) {
        return 0;
    }

    for (int count = 0; count < size_buffer - 1; count++) {
        read(STDIN_FILENO, buffer + count, 1);
        if (buffer[count] == '\n') {
            buffer[count + 1] = '\0';
            return count + 1;
        }
    }

    buffer[size_buffer] = '\0';
    return size_buffer;
}

int mini_strlen(char *s) {
    int i = 0;
    while (s[i] != '\0') {
        i++;
    }
    return i;
}

int mini_strcpy(char *s, char *d) {
    int i = 0;
    while (s[i] != '\0') {
        d[i] = s[i];
        i++;
    }
    return i;
}

int mini_strncpy(char *d, char *s, int n) {
    int i = 0;
    while (s[i] != '\0') {
        d[i] = s[i];
        i++;
        if (i >= n)
            return i;
    }
    return i;
}

int mini_strncat(char *d, char *s, int n) {
    d += mini_strlen(d);
    return mini_strncpy(d, s, n);
}


int mini_strcmp(char *s1, char *s2) {
    int i;
    for (i = 0; s1[i] != '\0' && s2[i] != '\0'; i++) {
        if (s1[i] > s2[i])
            return 1;
        else if (s1[i] < s2[i])
            return -1;
    }
    if (s1[i] == s2[i])
        return 0;
    else if (s1[i] == '\0')
        return -1;
    else
        return 1;
}

int mini_strncmp(char *s1, char *s2, int n) {
    int i;
    for (i = 0; s1[i] != '\0' && s2[i] != '\0'; i++) {
        if (i >= n)
            return 0;
        if (s1[i] > s2[i])
            return 1;
        else if (s1[i] < s2[i])
            return -1;
    }
    if (i >= n)
        return 0;
    if (s1[i] == s2[i])
        return 0;
    else if (s1[i] == '\0')
        return -1;
    else
        return 1;
}

int find_str(char *buf, char c) {
    int i = 0;
    while(*buf != '\0') {
        if(*buf == c) {
            return i;
        }
        i++;
        buf++;
    }
    return -1;
}