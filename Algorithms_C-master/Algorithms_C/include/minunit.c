#include "minunit.h"

void pass() {
    tests_passed++;
}

void fail(const char* message, const char* file, int line) {
    tests_failed++;
    printf("%s:%d: error: %s\n", file, line, message);
}

void summary() {
    printf("\nTest Summary:\n");
    printf("Tests Discovered: %d\n", tests_run);
    printf("Tests Passed: %d\n", tests_passed);
    printf("Tests Failed: %d\n", tests_failed);
    printf("Tests Missed: %d\n", tests_missed);
}
