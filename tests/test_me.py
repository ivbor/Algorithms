from Algorythms.python_solutions.matrix_view import matrix_view_2dim
from Algorythms.python_solutions.speed_analysis \
    import make_random_whole_1_dim_array, make_random_whole_2_dim_array, \
    speed_analysis, make_random_1_dim_array
from Algorythms.python_solutions.array_count_sort import array_count_sort
from Algorythms.python_solutions.count_sort import count_sort
from Algorythms.python_solutions.insert_sort import insert_sort
from Algorythms.python_solutions.merge_sort import merge_sort
from Algorythms.python_solutions.quick_sort import quick_sort
from Algorythms.python_solutions.two_dim_array_count_sort \
    import two_dim_array_count_sort
import math


def func(x):
    return math.sqrt(36-4*x*x)*x


def test_sort_speed_analysis(test_size_range=(10, 100),
                             num_range=(-10, 10)):
    '''
        Function for sorts speed testing
        can create 2dim arrays using speed_analysis module
        can change number of dimensions in array to sort,
        restriction for fractions inside array and
        how big array to sort would be
        All of these can be changed by:

        dim: number of dimensions, currently available only 1 or 2
        if more is necessary - write an additional function
        to the module mentioned before

        whole: whether numbers in array are only whole (True) or
        fractions are allowed (False)

        test_size: exact number of elements in the array

        num_range: tuple with the first number being start of the range
        of elements generation and the second - the end of this range
    '''

    # TODO add multidim sort
    # and create n-dim arrays using for

    # make a list of 1dim array and 2dim array
    one_dim_array = make_random_1_dim_array()
    whole_one_dim_array = make_random_whole_1_dim_array(
            elts_range=num_range, size_of_1_dim_range=test_size_range)
    whole_two_dim_array = make_random_whole_2_dim_array(
            elts_range=num_range, size_of_1_dim_range=test_size_range,
            size_of_2_dim_range=test_size_range)
    a = [one_dim_array, whole_one_dim_array,
         whole_two_dim_array]

    # make dict with sorts and functions
    sorts = {'array_count_sort': array_count_sort,
             'insert_sort': insert_sort,
             'merge_sort': merge_sort,
             'quick_sort': quick_sort,
             'two_dim_array_count_sort': two_dim_array_count_sort,
             'count_sort': count_sort}

    # and sort them using written sorts and built-in
    for i in sorts.items():

        # register time to sort for developed functions
        developed_time, developed = speed_analysis(

            # function name
            i[1],

            # choose array to sort (2dim for 2dim sorts, 1dim respectively)
            a[2].copy() if i[0] in (
                'array_count_sort',
                'two_dim_array_count_sort') \

            else a[1].copy() if i[0] == 'count_sort' \

            else a[0].copy(),

            # no need for params here
            {})

        # register time to sort for built_in function
        built_in_time, built_in = speed_analysis(

            sorted,

            a[2].copy() if i[0] in (
                'array_count_sort',
                'two_dim_array_count_sort') \

            else a[1].copy() if i[0] == 'count_sort' \

            else a[0].copy(),

            # since sorted sorts by all indexes by default, which written
            # array_count_sort does not, change parameter from default
            # to special lambda
            {} if i[0] != 'array_count_sort' else {'key': lambda a: a[0]})

        # and compare result
        assert (built_in == developed), (matrix_view_2dim(built_in),
                                         matrix_view_2dim(developed)) \
            if type(built_in[1]) == list else (print(built_in),
                                               print(developed))
        # and print times:
        print(f'{i[0]:25}: {developed_time:.10f}, \
              sorted: {built_in_time:.10f}\n')
