import random
from Algorithms.python_solutions.array_count_sort import array_count_sort


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
                         for i in range(100)]
                        for _ in range(100)]
    assert array_count_sort(array_with_2_dim) == \
        sorted(array_with_2_dim, key=lambda x: x[0]), \
        'array_count_sort does not sort 2 dim arrays'


def test_array_count_sort_case_many_elts_no_key_some_empty():
    array_with_2_dim = [[random.choice((
        (random.randint(-100, 100),))) for i in range(100)]
        for _ in range(100)]
    assert array_count_sort(array_with_2_dim) == \
        sorted(array_with_2_dim, key=lambda x: x[0]), \
        'array_count_sort does not sort 2 dim arrays with free places'


def test_array_count_sort_case_many_elts_with_key_some_empty():
    array_with_2_dim = [[random.choice((
        (random.randint(-100, 100),))) for i in range(100)]
        for _ in range(100)]
    assert array_count_sort(array_with_2_dim, key=9) == \
        sorted(array_with_2_dim, key=lambda x: x[9]), \
        'array_count_sort does not sort 2 dim arrays with free places'


def test_array_count_sort_case_many_elts_with_key_and_positions():
    array_with_2_dim = [[random.randint(-100, 100)
                         for i in range(100)]
                        for _ in range(100)]
    positions = list()
    sorted_array = sorted(array_with_2_dim, key=lambda x: x[9])
    for i in range(len(array_with_2_dim)):
        positions.append(array_with_2_dim.index(sorted_array[i]))
    result = array_count_sort(array_with_2_dim, key=9, position=True)
    positions_calculated = list()
    for i in result[1]:
        positions_calculated.extend(i)
    assert result[0] == sorted_array, \
        'array_count_sort does not sort 2 dim arrays'
    assert positions_calculated == positions, \
        'positions for further sort are calculated wrong'
