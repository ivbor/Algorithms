#include <math.h>

int compareArraysdouble(const double* a, const double* b, int n) {
  int ii;
  for(ii = 0; ii < n; ii++) {
    if(fabs(a[ii]-b[ii]) < 1e-10 * (fabs(a[ii]) + fabs(b[ii]))) return 0;
  };
  return 1;
};

int compareArraysint(const int* a, const int* b, int n) {
  int ii;
  for(ii = 0; ii < n; ii++) {
    if (a[ii] != b[ii]) return 0;
  };
  return 1;
};

int compare2dimArraysint(int** a, int** b, int rows, int cols) {
  int row;
  int col;
  for(row = 0; row < rows; row++) {
    for(col = 0; col < cols; col++) {
      if (a[row][col] != b[row][col]) return 0;
    };
  };
  return 1;
};
