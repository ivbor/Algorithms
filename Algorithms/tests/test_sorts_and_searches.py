# import better view function for 2dim arrays
import time
# import some helpers for creating arrays and time checking
from Algorithms.python_solutions.speed_analysis \
    import make_random_whole_1_dim_array, make_random_whole_2_dim_array, \
    speed_analysis, make_random_1_dim_array
# import sorting algorythms
from Algorithms.python_solutions.array_count_sort import array_count_sort
from Algorithms.python_solutions.count_sort import count_sort
from Algorithms.python_solutions.insert_sort import insert_sort
from Algorithms.python_solutions.merge_sort import merge_sort
from Algorithms.python_solutions.merge_sort import merge_sort_parallel
from Algorithms.python_solutions.quick_sort import quick_sort
from Algorithms.python_solutions.digit_sort import digit_sort
from Algorithms.python_solutions.two_dim_array_count_sort \
    import two_dim_array_count_sort
# import searching algorythms
from Algorithms.python_solutions.bin_search import bin_search
from Algorithms.python_solutions.real_bin_search import real_bin_search
from Algorithms.python_solutions.ternary_search_extremum \
    import tern_search_max, tern_search_min
# import searching for bounds
from Algorithms.python_solutions.bounds import lower_bound, upper_bound
# and for split find test
from Algorithms.python_solutions.split_find import split_find
# import math for calculations
import math


def test_sort_speed_analysis(test_size_range=(10, 100),
                             num_range=(-10, 10)):
    '''
        Function for sorts speed testing
        Parameters:

        test_size_range: range of number of elements inside array

        num_range: tuple with the first number being start of the range
        of elements generation and the second - the end of this range
    '''

    # TODO add multidim sort
    # and create n-dim arrays using for cycle

    # make a list of 1dim array and 2dim array
    one_dim_array = make_random_1_dim_array(
            elts_range=num_range, size_of_1_dim_range=test_size_range)
    whole_one_dim_array = make_random_whole_1_dim_array(
            elts_range=num_range, size_of_1_dim_range=test_size_range)
    whole_two_dim_array = make_random_whole_2_dim_array(
            elts_range=num_range, size_of_1_dim_range=test_size_range,
            size_of_2_dim_range=test_size_range)
    arrays = [one_dim_array, whole_one_dim_array,
              whole_two_dim_array]

    # make dict with sorts and functions
    sorts = {'array_count_sort': array_count_sort,
             'insert_sort': insert_sort,
             'merge_sort': merge_sort,
             'merge_sort_parallel': merge_sort_parallel,
             'quick_sort': quick_sort,
             'two_dim_array_count_sort': two_dim_array_count_sort,
             'count_sort': count_sort,
             'digit_sort': digit_sort}

    # and sort them using written sorts and built-in
    for i in sorts.items():

        # register time to sort for developed functions
        developed_time, developed = speed_analysis(

            # function name
            i[1],

            # choose array to sort (2dim for 2dim sorts, 1dim respectively)
            arrays[2].copy() if i[0] in (
                'array_count_sort',
                'two_dim_array_count_sort') \

            else arrays[1].copy() if i[0] in ['count_sort', 'digit_sort'] \

            else arrays[0].copy(),

            # no need for params here
            params={} if i[0] != 'digit_sort' else {'base': 16})

        # register time to sort for built_in function
        built_in_time, built_in = speed_analysis(

            sorted,

            arrays[2].copy() if i[0] in (
                'array_count_sort',
                'two_dim_array_count_sort')

            else arrays[1].copy() if i[0] in ['count_sort', 'digit_sort']

            else arrays[0].copy(),

            # since sorted does sorts by all indexes by default, which written
            # array_count_sort does not, change parameter from default inside
            # sorted to special lambda-defined key making it perform the
            # same sort as array_count_sort
            {} if i[0] != 'array_count_sort' else {'key': lambda a: a[0]})

        # and compare result
        assert (built_in == developed), i[0]

        # and print times:
        print(f'{i[0]:25}: {developed_time:.10f}, \
              sorted: {built_in_time:.10f}\n')


# if in array searched value is absent
# .index() throws ValueError
# this wrapper handles exception so that
# absence of the element can be handled
# by speed_analysis function


def index_search(a):
    try:
        return a.index(3)
    except ValueError:
        return 'No'


def test_bin_search_speed_analysis(
        test_size_range=(10, 100),
        num_range=(-10, 10)):
    '''
        Function to test the speed of search
        Parameters:

        test_size_range: range of number of elements inside array

        num_range: tuple with the first number being start of the range
        of elements generation and the second - the end of this range
    '''

    # make sorted array
    a = make_random_1_dim_array(
            elts_range=num_range,
            size_of_1_dim_range=test_size_range)
    # a.append(3)
    a = sorted(a)

    # find an element inside it using developed functions while registering
    # time spent
    built_in_time, built_in = speed_analysis(
        index_search, a, {})

    developed_no_rec_time, developed_no_rec = speed_analysis(
        lambda x: bin_search(x, 3), a, {})

    developed_rec_time, developed_rec = speed_analysis(
        lambda x: bin_search(x, 3, True), a, {})

    assert (type(built_in) == int) == developed_no_rec, print(a)
    assert developed_no_rec == developed_rec, print(a)
    print('Without desired element')
    print(f'developed_no_rec: {developed_no_rec_time:.10f}, \
            developed_rec: {developed_rec_time:.10f}, \
            index: {built_in_time:.10f}\n')

    a = make_random_1_dim_array(
            elts_range=num_range,
            size_of_1_dim_range=test_size_range)
    a.append(3)  # manually append desired element
    a = sorted(a)

    built_in_time, built_in = speed_analysis(
        index_search, a, {})

    developed_no_rec_time, developed_no_rec = speed_analysis(
        lambda x: bin_search(x, 3), a, {})

    developed_rec_time, developed_rec = speed_analysis(
        lambda x: bin_search(x, 3, True), a, {})

    # and print times:
    print('With desired element')
    print(f'developed_no_rec: {developed_no_rec_time:.10f}, \
            developed_rec: {developed_rec_time:.10f}, \
            index: {built_in_time:.10f}\n')


def func(x):
    return math.sqrt(36-4*x*x)*x


def test_real_bin_search():
    st = time.time()
    res = real_bin_search(func, -6, -2, 2)
    et = time.time()
    # func(-6) = -1.070
    assert abs(res + 1.07) <= 5*10**(-4), res
    print(f'real_bin_search_time: {(et-st):.10f}')


def test_min_max_tern_search():
    st = time.time()
    res = tern_search_min(func, -3, 0)
    et = time.time()
    # min there is -2.121
    assert abs(res + 2.121) <= 5*10**(-4), res
    print(f'tern_search_min_time, one min: {(et-st):.10f}')

    st = time.time()
    res = tern_search_min(func, 0, 3)
    et = time.time()
    # min there is 0 or 3
    assert (abs(res) <= 5*10**(-4) or abs(res - 3) <= 5*10**(-4)), res
    print(f'tern_search_min_time, two mins: {(et-st):.10f}')

    st = time.time()
    res = tern_search_max(func, -3, 0)
    et = time.time()
    # max there is 0 or -3
    assert (abs(res) <= 5*10**(-4) or abs(res + 3) <= 5*10**(-4)), res
    print(f'tern_search_max_time, two maxes: {(et-st):.10f}')

    st = time.time()
    res = tern_search_max(func, 0, 3)
    et = time.time()
    # max there is 2.121
    assert abs(res - 2.121) <= 5*10**(-4), res
    print(f'tern_search_max_time, one max: {(et-st):.10f}')


def test_bounds():
    a = make_random_whole_1_dim_array(
        size_of_1_dim_range=(1000, 2000))
    a = sorted(a)

    st = time.time()
    built_in = a.index(3) if 3 in a else False
    et = time.time()
    built_in_time = et - st

    st = time.time()
    developed = lower_bound(a, 3) if 3 in a else False
    et = time.time()
    developed_time = et - st

    assert built_in == developed, (built_in, developed)
    print('lower bound')
    print(f'built_in_time: {built_in_time:.10f}, \
           developed_time: {developed_time:.10f}')

    st = time.time()
    built_in = a.index(4) - 1 if 4 in a else False
    et = time.time()
    built_in_time = et - st

    st = time.time()
    developed = upper_bound(a, 3) if 4 in a else False
    et = time.time()
    developed_time = et - st

    assert built_in == developed, (built_in, developed)
    print('upper bound')
    print(f'built_in_time: {built_in_time:.10f}, \
           developed_time: {developed_time:.10f}')


def test_split_search():
    a = make_random_whole_1_dim_array(elts_range=(-10, 10))
    b = a.copy()
    a = sorted(a)

    st = time.time()
    developed = split_find(b, 36)
    et = time.time()
    developed_time = et - st

    assert a[36] == developed, (a[36], developed)
    print(f'split search time: {developed_time:.10f}')
