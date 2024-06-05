#include <stdio.h>

void printMatrix(int **matrix, int rows, int columns, int indexes) {
    // Printing column indexes
    if (indexes) {
        for (int i = 0; i <= columns; i++) {
            if (i == 0) {
                printf("%5d ", i);
            }
            printf("%5d ", i);
        }
        printf("\n");
    }

    // Printing matrix with optional row indexes
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j <= columns; j++) {
            if (indexes && j == 0) {
                printf("%5d ", i);
            }
            if (j < columns) {
                printf("%5d ", matrix[i][j]);
            }
        }
        printf("\n\n");
    }
    printf("\n");
} 
