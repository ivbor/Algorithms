#include <stdlib.h>
#include <stdio.h>

#include "../headers/matrix_view.h"

#ifndef Mystrcat
#include "../../include/mystrcat.c"
#endif

#ifndef logger
#include "../../include/logger.h"
#endif

void printMatrix(int **matrix, int rows, int columns, int indexes) {
    //2**14 = 16384  

    char* to_print = (char*)malloc(16384);
    char* to_print_copy = to_print;
    to_print[0] = '\0';
    char one_element[32];
    // Printing column indexes
    if (indexes) {
        for (int i = 0; i <= columns; i++) {
            int required_length = snprintf(NULL, 0, "%5d ", i);
            if (required_length - 32 < 0) {
            snprintf(one_element, 32, "%5d ", i);
            to_print = mystrcat(to_print, one_element); }
            else { 
                log_message(LOG_FATAL, 
                    "Allocated wrong amount of memory for one_element, \
                    difference (required - allocated) = ");
                char char_length[(int)sizeof(int)];
                snprintf(char_length, 3 * sizeof(int), "%d", 
                    required_length - 32);
                log_message(LOG_FATAL, char_length);
                exit(EXIT_FAILURE);
            }
        }
        to_print = mystrcat(to_print, "\n");
    }

    // Printing matrix with optional row indexes
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j <= columns; j++) {
            if (indexes && j == 0) {
                snprintf(one_element, 32, "%5d ", i);
                to_print = mystrcat(to_print, one_element);
            }
            if (j < columns) {
                snprintf(one_element, 32, "%5d ", matrix[i][j]);
                to_print = mystrcat(to_print, one_element);
            }
        }
        to_print = mystrcat(to_print, "\n\n");
    }
    to_print = mystrcat(to_print, "\n");
    log_message(LOG_DEBUG, to_print_copy);   
    free(to_print_copy);
} 
