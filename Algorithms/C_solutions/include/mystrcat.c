#ifndef Mystrcat
#define Mystrcat
char *mystrcat(char *dest, char *src) {
    while (*dest) dest++;
    while ((*dest++ = *src++));
    return --dest;
} 
#endif
