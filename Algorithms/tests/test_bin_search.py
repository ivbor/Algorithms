import random

from Algorithms.python_solutions.bin_search import bin_search


def test_bin_search_no_rec():
    array = [random.randint(-100, 100) for i in range(random.randint(10, 100))]
    array = sorted(array)
    for i in range(-100, 100):
        assert bin_search(array, i) == (i in array), \
            f'existence of {i} inside array is determined wrong'


def test_bin_search_with_rec():
    array = [random.randint(-100, 100) for i in range(random.randint(10, 100))]
    array = sorted(array)
    for i in range(-100, 100):
        assert bin_search(array, i, True) == (i in array), \
            f'existence of {i} inside array is determined wrong'
