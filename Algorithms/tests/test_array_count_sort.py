import random

from Algorithms.python_solutions.array_count_sort import array_count_sort


def test_array_count_sort_case_one_elt_with_huge_variation():
    array_with_1_dim = [[random.randint(-10000, 10000) for _ in range(100)]]
    assert array_count_sort(array_with_1_dim) == \
        sorted(array_with_1_dim), \
        'optimization works wrong'


def test_array_count_sort_case_one_elt_in_2_dim():
    array_with_1_dim = [[random.randint(-100, 100)]
                        for _ in range(100)]
    assert array_count_sort(array_with_1_dim) == \
        sorted(array_with_1_dim), \
        'array_count_sort does not sort 1 dim arrays'


def test_array_count_sort_case_one_elt_in_2_dim_some_empty():
    array_with_1_dim = [[random.choice(
        (random.randint(-100, 100),))] for _ in range(100)]
    assert array_count_sort(array_with_1_dim) == \
        sorted(array_with_1_dim), \
        'array_count_sort does not sort 1 dim arrays with free places'


def test_array_count_sort_case_many_elts_no_key():
    array_with_2_dim = [[random.randint(-100, 100)
                         for _ in range(100)]
                        for _ in range(100)]
    assert array_count_sort(array_with_2_dim) == \
        sorted(array_with_2_dim, key=lambda x: x[0]), \
        'array_count_sort does not sort 2 dim arrays'


def test_array_count_sort_case_many_elts_no_key_some_empty():
    array_with_2_dim = [[random.choice((
        (random.randint(-100, 100),))) for _ in range(100)]
        for _ in range(100)]
    assert array_count_sort(array_with_2_dim) == \
        sorted(array_with_2_dim, key=lambda x: x[0]), \
        'array_count_sort does not sort 2 dim arrays with free places'


def test_array_count_sort_case_many_elts_with_key_some_empty():
    array_with_2_dim = [[random.choice((
        (random.randint(-100, 100),))) for _ in range(100)]
        for _ in range(100)]
    assert array_count_sort(array_with_2_dim, key=9) == \
        sorted(array_with_2_dim, key=lambda x: x[9]), \
        'array_count_sort does not sort 2 dim arrays with free places'
