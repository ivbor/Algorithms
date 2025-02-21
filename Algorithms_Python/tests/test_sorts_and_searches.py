# import math for calculations
import math
import logging
import pytest
import random
# import better view function for 2dim arrays
from Algorithms_Python.matrix_view import Matrix2dim
# import sorting algorithms
from Algorithms_Python.array_count_sort import array_count_sort
from Algorithms_Python.count_sort import count_sort
from Algorithms_Python.insert_sort \
    import insert_sort, insert_sort_opt
from Algorithms_Python.merge_sort \
    import merge_sort, merge_sort_parallel
from Algorithms_Python.quick_sort import quick_sort
from Algorithms_Python.digit_sort import digit_sort, digit_sort_opt
from Algorithms_Python.two_dim_array_count_sort \
    import two_dim_array_count_sort
# import searching algorithms
from Algorithms_Python.bin_search import bin_search
from Algorithms_Python.real_bin_search import real_bin_search
from Algorithms_Python.ternary_search_extremum \
    import tern_search_max, tern_search_min
# import searching for bounds
from Algorithms_Python.bounds import lower_bound, upper_bound
# and for split find test
from Algorithms_Python.split_find import split_find


def random_1_dim_array(elts_range=(-100, 100),
                       size_of_1_dim_range=(100, 1000)):
    return [random.uniform(*elts_range)
            for _ in range(random.randint(*size_of_1_dim_range))]


def whole_1_dim_array(elts_range=(-100, 100),
                      size_of_1_dim_range=(100, 1000)):
    return [random.randint(*elts_range)
            for _ in range(random.randint(*size_of_1_dim_range))]


def whole_2_dim_array(elts_range=(-10, 10), size_of_1_dim_range=(1, 10),
                      size_of_2_dim_range=(10, 100)):
    return [[random.randint(*elts_range)
             for _ in range(random.randint(*size_of_1_dim_range))]
            for _ in range(random.randint(*size_of_2_dim_range))]


# fixed here, but can be changed manually inside parametrize for each
# particular function
# test_size_range: range of number of elements inside array
test_size_range = (10, 100)
# num_range: tuple with the first number being start of the range
# of elements generation and the second - the end of this range
num_range = (-10, 10)


@pytest.mark.parametrize('function, array, params, sorted_params',
                         [
                          (array_count_sort,
                           whole_2_dim_array(
                             elts_range=num_range,
                             size_of_1_dim_range=test_size_range,
                             size_of_2_dim_range=test_size_range),
                           {}, {'key': lambda a: a[0]}),

                          (insert_sort,
                           random_1_dim_array(
                             elts_range=num_range,
                             size_of_1_dim_range=test_size_range),
                           {}, {}),

                          (insert_sort_opt,
                           random_1_dim_array(
                             elts_range=num_range,
                             size_of_1_dim_range=test_size_range),
                           {}, {}),

                          (merge_sort,
                           random_1_dim_array(
                             elts_range=num_range,
                             size_of_1_dim_range=test_size_range),
                           {'opt': False}, {}),

                          (merge_sort,
                           random_1_dim_array(
                             elts_range=num_range,
                             size_of_1_dim_range=(1, 1)),
                           {'opt': False}, {}),

                          (merge_sort_parallel,
                           random_1_dim_array(
                             elts_range=num_range,
                             size_of_1_dim_range=(32, 100)),
                           {}, {}),

                          (merge_sort_parallel, [0], {}, {}),

                          (merge_sort,
                           random_1_dim_array(
                             elts_range=num_range,
                             size_of_1_dim_range=(101, 1000)),
                           {}, {}),

                          (merge_sort,
                           random_1_dim_array(
                             elts_range=num_range,
                             size_of_1_dim_range=(10, 60)),
                           {}, {}),

                          (quick_sort,
                           random_1_dim_array(
                             elts_range=num_range,
                             size_of_1_dim_range=test_size_range),
                           {}, {}),

                          (quick_sort,
                           random_1_dim_array(
                             elts_range=num_range,
                             size_of_1_dim_range=test_size_range),
                           {'no_recursion': True}, {}),

                          (quick_sort,
                           random_1_dim_array(
                             elts_range=num_range,
                             size_of_1_dim_range=test_size_range),
                           {'pivot_str': 'clst_avg',
                            'no_recursion': True}, {}),

                          (quick_sort,
                           random_1_dim_array(
                             elts_range=num_range,
                             size_of_1_dim_range=test_size_range),
                           {'pivot_str': 'm3',
                            'no_recursion': True}, {}),
                          (quick_sort, [0], {}, {}),

                          (quick_sort,
                           random_1_dim_array(
                             elts_range=num_range,
                             size_of_1_dim_range=test_size_range),
                           {'pivot_str': 'clst_avg'}, {}),

                          (quick_sort,
                           random_1_dim_array(
                             elts_range=num_range,
                             size_of_1_dim_range=test_size_range),
                           {'pivot_str': 'm3'}, {}),

                          (quick_sort, [1000] +
                           random_1_dim_array(
                                elts_range=num_range,
                                size_of_1_dim_range=test_size_range) +
                           [-1000],
                           {'pivot_str': 'm3'}, {}),


                          (quick_sort,
                           random_1_dim_array(
                             elts_range=num_range,
                             size_of_1_dim_range=test_size_range),
                           {'pivot_str': 'mm'}, {}),

                          (quick_sort, [], {}, {}),

                          (two_dim_array_count_sort,
                           whole_2_dim_array(
                             elts_range=num_range,
                             size_of_1_dim_range=test_size_range,
                             size_of_2_dim_range=test_size_range),
                           {}, {}),

                          (two_dim_array_count_sort,
                           whole_2_dim_array(
                             elts_range=num_range,
                             size_of_1_dim_range=test_size_range,
                             size_of_2_dim_range=test_size_range),
                           {'keys': [0, 1, 2]},
                           {'key': lambda x: (x[0], x[1], x[2])}),

                          (two_dim_array_count_sort,
                           whole_2_dim_array(
                             elts_range=num_range,
                             size_of_1_dim_range=test_size_range,
                             size_of_2_dim_range=test_size_range),
                           {'keys': 2}, {'key': lambda x: x[2]}),

                          (count_sort,
                           whole_1_dim_array(
                             elts_range=num_range,
                             size_of_1_dim_range=test_size_range),
                           {}, {}),

                          (digit_sort,
                           whole_1_dim_array(
                             elts_range=num_range,
                             size_of_1_dim_range=test_size_range),
                           {'base': 16}, {}),

                          (digit_sort_opt,
                           whole_1_dim_array(
                             elts_range=num_range,
                             size_of_1_dim_range=test_size_range),
                           {'base': 16}, {})
                         ])
def test_sorts(function, array, params, sorted_params):
    array_copy = array.copy()
    developed = function(array_copy, **params)
    built_in = sorted(array, **sorted_params)
    assert built_in == developed

    # print to the log file
    if isinstance(built_in, list) and len(built_in) > 0:
        if isinstance(built_in[0], list):
            built_in = Matrix2dim(data=built_in)
            developed = Matrix2dim(data=developed)
            logging.debug(f'{function} \n built_in: \n' +
                          f'{Matrix2dim.__repr__(built_in, indexes=True)}' +
                          '\n developed: \n' +
                          f'{Matrix2dim.__repr__(developed, indexes=True)}')
        else:
            logging.debug(f'{function} \n built_in: \n' +
                          f'{built_in} \n developed: \n' +
                          f'{developed}')


@pytest.mark.parametrize('function, array, params',
                         [(two_dim_array_count_sort,
                          whole_2_dim_array(
                             elts_range=num_range,
                             size_of_1_dim_range=test_size_range,
                             size_of_2_dim_range=test_size_range),
                          {'keys': ''}),

                          (quick_sort,
                           random_1_dim_array(
                             elts_range=num_range,
                             size_of_1_dim_range=test_size_range),
                           {'pivot_str': 'mm',
                            'no_recursion': True}),

                          (quick_sort,
                          random_1_dim_array(
                             elts_range=num_range,
                             size_of_1_dim_range=test_size_range),
                          {'pivot_str': 'cool'})
                          ])
def test_errors_in_sorts(function, array, params):
    with pytest.raises(Exception):
        function(array, **params)


@pytest.mark.parametrize('array',
                         [random_1_dim_array(
                            elts_range=num_range,
                            size_of_1_dim_range=test_size_range),
                          random_1_dim_array(
                            elts_range=num_range,
                            size_of_1_dim_range=test_size_range),
                          ])
def test_bin_search(array):

    array = sorted(array)

    for i in range(-100, 100):
        assert bin_search(array, i) == (i in array), \
            f'existence of {i} inside array is determined wrong'
        assert bin_search(array, i, True) == (i in array), \
            f'existence of {i} inside array is determined wrong'


def func(x):
    return math.sqrt(36-4*x*x)*x


def test_real_bin_search():
    res = real_bin_search(func, -6, -2, 2)
    # func(-6) = -1.070
    assert abs(res + 1.07) <= 5*10**(-4), res


def test_min_max_tern_search():
    res = tern_search_min(func, -3, 0)
    # min there is -2.121
    assert abs(res + 2.121) <= 5*10**(-4), res

    res = tern_search_min(func, 0, 3)
    # min there is 0 or 3
    assert (abs(res) <= 5*10**(-4) or abs(res - 3) <= 5*10**(-4)), res

    res = tern_search_max(func, -3, 0)
    # max there is 0 or -3
    assert (abs(res) <= 5*10**(-4) or abs(res + 3) <= 5*10**(-4)), res

    res = tern_search_max(func, 0, 3)
    # max there is 2.121
    assert abs(res - 2.121) <= 5*10**(-4), res


@pytest.mark.parametrize('array', [whole_1_dim_array(
                                    size_of_1_dim_range=(1000, 2000)),
                                   whole_1_dim_array(
                                    size_of_1_dim_range=(100, 2000))])
def test_bounds(array):
    array = sorted(array)

    built_in = \
        array.index(3) if 3 in array else False
    developed = \
        lower_bound(array, 3) if 3 in array else False
    assert built_in == developed

    built_in = \
        array.index(4) - 1 if 4 in array else False
    developed = \
        upper_bound(array, 3) if 4 in array else False
    assert built_in == developed


@pytest.mark.parametrize('array', [whole_1_dim_array(
                                    elts_range=(-10, 10)),
                                   whole_1_dim_array(
                                    elts_range=(-10, 10))])
def test_split_search(array):
    array_copy = array.copy()
    array = sorted(array)
    developed = split_find(array_copy, 36)
    assert array[36] == developed
