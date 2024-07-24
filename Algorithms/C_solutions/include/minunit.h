/* 
 * JTN002 - MinUnit -- a minimal unit testing framework for C
 * Jera Design LLC
 * https://jera.com/techinfo/jtns/jtn002
 */

#ifndef minunit
#define minunit

#include <stdio.h>
#include "minunit_var.c"

#define run_assert(message, test) \
  do { \
    if (!(test)) { \
      fail(message, __FILE__, __LINE__); \
    } else { \
      pass(); \
    } \
    tests_run++; } \
  while (0)
#define run_test(test) \
  do { \
    printf("Running test: %s\n", #test); \
    test(); } \
  while (0)

void pass();
void fail(const char* message, const char* file, int line);
void summary();

#endif
