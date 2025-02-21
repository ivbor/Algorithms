#ifndef NO_STARS
#include "../../include/macros.h"
#endif

#ifndef minunit
#include "../../include/minunit.h"
#endif

#ifndef logger
#include "../../include/logger.h"
#endif

#include "../../src/headers/array_count_sort.h"
#include "../../src/headers/matrix_view.h"
#include "../../src/headers/compare.h"
#include <stdlib.h>
#include <stdio.h>
#include <time.h>

int key = 0;

int comp_func(const void* a, const void* b) {
    if (deref((int**)a)[key] > deref((int**)b)[key]) 
      return 1;
    else if (deref((int**)a) < deref((int**)b))
      return -1;
    else return 0;
};

char* test_array_count_sort_case_one_elt_with_huge_variation() {
    int rows = 10;
    int cols = 10;
    int** array_with_1_dim = (int**)malloc(rows * sizeof(int*));
    int* ptrs[rows];

    // Populate array with random integers
    srand(time(NULL)); // Seed random number generator
    for (int i = 0; i < rows; i++) {
        array_with_1_dim[i] = (int*)malloc(cols * sizeof(int));
        for (int j = 0; j < cols; j++) 
            // Random int between -10000 and 10000
            array_with_1_dim[i][j] = rand() % 20001 - 10000; 
        ptrs[i] = array_with_1_dim[i];
    };

    // Sort the array using array_count_sort
    log_message(LOG_DEBUG, "array before sort: \n");
    printMatrix(array_with_1_dim, rows, cols, 1);
    array_count_sort(array_with_1_dim, rows, cols, 0);
    log_message(LOG_DEBUG, "array after sort: \n");
    printMatrix(array_with_1_dim, rows, cols, 1);

    // We need a method to sort the array
    log_message(LOG_DEBUG, "copied array before sort: \n");
    printMatrix(ptrs, rows, cols, 1);
    qsort(ptrs, rows, sizeof(int*), comp_func);
    log_message(LOG_DEBUG, "copied array after sort: \n");
    printMatrix(ptrs, rows, cols, 1);
    

    run_assert("Array should be sorted.",
        compare2dimArraysint(array_with_1_dim, ptrs, rows, cols));

    for (int i = 0; i < rows; i++) {
      free(ptrs[i]);
    };
    free(array_with_1_dim);
    return 0;
};
