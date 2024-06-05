#include "./unity/src/unity.h"
#include "../include/array_count_sort.h"
#include "../include/matrix_view.h"
#include <stdlib.h>
#include <stdio.h>
#include <time.h>


int key;

int comp_func(const void* a, const void* b) {
    a += key * sizeof(int);
    printf("Address of a = %d, dereferenced value = %d\n", (int)a, *(int*)a);
    b += key * sizeof(int);
    printf("Address of b = %d, dereferenced value = %d\n", (int)b, *(int*)b);
    if (*(int*)a > *(int*)b) 
      return 1;
    else if (*(int*)a < *(int*)b)
      return -1;
    else return 0;
};

void setUp(void) {
    // This is run before EACH test
};

void tearDown(void) {
    // This is run after EACH test
};

void test_array_count_sort_case_one_elt_with_huge_variation() {
    int rows = 10;
    int cols = 10;
    int** array_with_1_dim = (int**)malloc(rows * sizeof(int*));
    int** copied_array = (int**)malloc(rows * sizeof(int*));

    // Populate array with random integers
    srand(time(NULL)); // Seed random number generator
    for (int i = 0; i < rows; i++) {
        copied_array[i] = (int*)malloc(cols * sizeof(int));
        array_with_1_dim[i] = (int*)malloc(cols * sizeof(int));
        for (int j = 0; j < cols; j++) {
            array_with_1_dim[i][j] = rand() % 20001 - 10000; // Random int between -10000 and 10000
            copied_array[i][j] = array_with_1_dim[i][j];
        }
    }

    // Sort the array using array_count_sort
    printf("array before sort: ");
    printMatrix(array_with_1_dim, rows, cols, 1);
    array_count_sort(array_with_1_dim, rows, cols, 0);
    printf("array after sort: ");
    printMatrix(array_with_1_dim, rows, cols, 1);

    // We need a method to sort the array
    printf("copied array before sort: ");
    printMatrix(copied_array, rows, cols, 1);
    qsort(copied_array, rows, sizeof(int*), comp_func);
    printf("copied array after sort: ");
    printMatrix(copied_array, rows, cols, 1);
    

    TEST_ASSERT_TRUE_MESSAGE(
        array_with_1_dim == copied_array,
        "Array should be sorted.");

    free(array_with_1_dim);
};

int main(void) {
    UNITY_BEGIN();
    RUN_TEST(test_array_count_sort_case_one_elt_with_huge_variation);
    // Add other RUN_TEST calls for other test functions
    return UNITY_END();
}
