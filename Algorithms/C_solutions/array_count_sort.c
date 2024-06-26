#include <stdio.h>
#include <stdlib.h>
#include <limits.h>


// Function to find the maximum and minimum values in a 2D array 
// based on a specific key index
void find_min_max(int **arr, int rows, int key, int *min, int *max) {
    *min = INT_MAX;
    *max = INT_MIN;
    for (int i = 0; i < rows; i++) {
      if (arr[i][key] != INT_MIN) {
            if (arr[i][key] < *min) *min = arr[i][key];
            if (arr[i][key] > *max) *max = arr[i][key];
            }
      }
}

// Function to perform Counting Sort on a 2D array 
// based on a specific key index
void array_count_sort(int **arr, int rows, int cols, int key) {
   
    // Initialize and calculate min and max in the array 
    int min, max;
    find_min_max(arr, rows, key, &min, &max);

    // Initialize range of the array's elements
    int range = max - min + 2;

    // Initialize arrays for counting and for storing the result
    int *count = (int*)calloc(range, sizeof(int));
    int **result = (int**)malloc(rows * sizeof(int*));
    
    // Count occurrences of each key
    for (int i = 0; i < rows; i++) {
        result[i] = (int*)calloc(cols, sizeof(int));
        if (arr[i][key] != INT_MIN) {
            count[arr[i][key] - min]++;
        } else {
            count[range - 1]++;
        }
    }

    // Calculate cumulative count
    for (int i = 1; i < range; i++) {
        count[i] += count[i - 1];
    }

    // Build sorted array
    for (int i = rows - 1; i >= 0; i--) {
        if (arr[i][key] != INT_MIN) {
            count[arr[i][key] - min]--;
            for (int j = 0; j < cols; j++) {
                result[count[arr[i][key] - min]][j] = arr[i][j];
            }
        } else {
            count[range - 1]--;
            for (int j = 0; j < cols; j++) {
                result[count[range - 1]][j] = arr[i][j];
            }
        }
    }
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            arr[i][j] = result[i][j];
        }
        free(result[i]);
    }
    free(result);
    free(count);
}

// Example of usage
int main() {
    int rows = 4;
    int cols = 3;
    int key = 0;
    int **arr = (int**)malloc(rows * sizeof(int*));
    for (int i = 0; i < rows; i++) {
        arr[i] = (int*)malloc(cols * sizeof(int));
        // Example initialization, replace with actual data
        for (int j = 0; j < cols; j++) {
            arr[i][j] = i * cols + j; // Replace with actual data
        }
    }
    // Assume arr is initialized with your data before sorting
    array_count_sort(arr, rows, cols, key);
    // Print sorted array
    for (int i = 0; i < rows; i++) {
        for (int j = 0; j < cols; j++) {
            printf("%d ", arr[i][j]);
        }
        printf("\n");
        free(arr[i]);
    }
    free(arr);
    return 0;
}
 
