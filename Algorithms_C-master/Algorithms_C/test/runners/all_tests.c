#ifndef minunit
#include "../../include/minunit.h"
#endif

#include "../test/test_array_count_sort.c"

int main(void) {
    run_test(test_array_count_sort_case_one_elt_with_huge_variation);
    summary();
    return tests_failed ? 1 : 0;    
}
