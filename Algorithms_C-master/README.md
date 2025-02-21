# Algorithms and Data Structures on C

All folders' and files' places are given as if you are in Algorithms_C folder.

The repository has the  following structure:

- `include` folder contains files with helper functions and macros, such as
minimal testing framework, logger and some macros for increased code
readability;
- `src` folder contains `headers` folder with defines, typedefs and
declarations for everything in my source code, `code` folder with the source
code and `bin` folder where compiled source code is stored as a binary or a
shared library;
- `test` folder contains `test` folder with test functions, `setup` folder with
setup functions, `teardown` folder with appropriate similar objective and
`runners` folder where runners for all tests are written.
  - `runners` folder contains folders `code` with code for runners and `bin`
  where there are compiled binaries for those runners

Also there is a Makefile in this folder where you can find everything you need
to know about the compilation process for this repo.

All tests are run by `make` command in this directory.

## TODOs

- setup CI/CD
  - clang-tidy
  - clang-format
  - markdownlint
  - python scripts to parse setup.cfg into appropriate configs
- continue writing test cases
  - translate tests for array_count_sort from python to C
