CC = gcc -Wall -Werror
SHARED = -fPIC -shared
BIN = -fsanitize=address

launch: test/bin/all_tests
	test/bin/all_tests

test/bin/all_tests: \
		test/runners/all_tests.c \
		test/bin/test_array_count_sort.so
	$(CC) $(BIN) \
		test/bin/test_array_count_sort.so \
		test/runners/all_tests.c \
		-o test/bin/all_tests \
		-Wl,-rpath=./src/bin:./include/bin\
		-Lsrc/bin -l:matrix_view.so -l:array_count_sort.so -l:compare.so \
		-Linclude/bin -l:minunit.so -l:logger.so

test/bin/test_array_count_sort.so: \
		test/test/test_array_count_sort.c \
		include/bin/minunit.so \
		include/bin/logger.so \
		src/bin/matrix_view.so \
		src/bin/array_count_sort.so \
		src/bin/compare.so 
	$(CC) $(SHARED) -Isrc/headers -Iinclude \
		test/test/test_array_count_sort.c \
		include/bin/minunit.so \
		include/bin/logger.so \
		src/bin/matrix_view.so src/bin/compare.so \
		src/bin/array_count_sort.so \
		-o test/bin/test_array_count_sort.so

src/bin/matrix_view.so: src/code/matrix_view.c
	$(CC) $(SHARED) -o src/bin/matrix_view.so src/code/matrix_view.c

src/bin/array_count_sort.so: src/code/array_count_sort.c
	$(CC) $(SHARED) -o src/bin/array_count_sort.so \
		src/code/array_count_sort.c

src/bin/compare.so: src/code/compare.c
	$(CC) $(SHARED) -o src/bin/compare.so src/code/compare.c

include/bin/minunit.so: include/minunit.c include/minunit_var.c
	$(CC) $(SHARED) -o include/bin/minunit.so include/minunit.c

include/bin/logger.so: include/logger.c
	$(CC) $(SHARED) -o include/bin/logger.so include/logger.c
