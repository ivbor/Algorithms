import random
from Algorithms.python_solutions.speed_analysis \
    import make_random_1_dim_array
from Algorithms.python_solutions.speed_analysis \
    import make_random_whole_1_dim_array
from Algorithms.python_solutions.speed_analysis \
    import make_random_whole_2_dim_array


def test_make_random_1_dim_array_runs():
    array = make_random_1_dim_array()
    assert isinstance(array, list), 'function should make a list but does not'


def test_make_random_1_dim_array_default():
    array = make_random_1_dim_array()
    for i in array:
        assert (-100 < i and i < 100), \
            'there are elements not in the default array range'
        assert isinstance(i, float), 'not all elements are float'
    len_array = len(array)
    assert (100 < len_array and len_array < 1000), \
        'wrong range for the length of array'


def test_make_random_1_dim_array_not_default():
    elts_range = (random.randint(-1000, -100), random.randint(100, 1000))
    size_of_1_dim_range = (random.randint(10, 100),
                           random.randint(100, 1000))
    array = make_random_1_dim_array(elts_range=elts_range,
                                    size_of_1_dim_range=size_of_1_dim_range)
    for i in array:
        assert (elts_range[0] < i and i < elts_range[1]), \
            'there are elements not in the default array range'
        assert isinstance(i, float), 'not all elements are float'
    len_array = len(array)
    assert (size_of_1_dim_range[0] < len_array
            and len_array < size_of_1_dim_range[1]), \
        'wrong range for the length of array'


def test_make_random_whole_1_dim_array_runs():
    array = make_random_whole_1_dim_array()
    assert isinstance(array, list), 'function should make a list but does not'


def test_make_random_whole_1_dim_array_default():
    array = make_random_whole_1_dim_array()
    for i in array:
        assert (-100 <= i and i <= 100), \
            'there are elements not in the default array range'
        assert isinstance(i, int), 'not all elements are int'
    len_array = len(array)
    assert (100 < len_array and len_array < 1000), \
        'wrong range for the length of array'


def test_make_random_whole_1_dim_array_not_default():
    elts_range = (random.randint(-1000, -100), random.randint(100, 1000))
    size_of_1_dim_range = (random.randint(10, 100),
                           random.randint(100, 1000))
    array = make_random_whole_1_dim_array(
        elts_range=elts_range,
        size_of_1_dim_range=size_of_1_dim_range)
    for i in array:
        assert (elts_range[0] <= i and i <= elts_range[1]), \
            'there are elements not in the default array range'
        assert isinstance(i, int), 'not all elements are float'
    len_array = len(array)
    assert (size_of_1_dim_range[0] < len_array
            and len_array < size_of_1_dim_range[1]), \
        'wrong range for the length of array'


def test_make_random_whole_2_dim_array_runs():
    array = make_random_whole_2_dim_array()
    assert isinstance(array, list), 'function should make a list but does not'


def test_make_random_whole_2_dim_array_default():
    array = make_random_whole_2_dim_array()
    for row in array:
        for i in row:
            assert (-10 <= i and i <= 10), \
                'there are elements not in the default array range'
            assert isinstance(i, int), 'not all elements are int'
        len_row = len(row)
        assert (1 <= len_row <= 10), \
            'wrong range for the length of first dim ofarray'
    len_array = len(array)
    assert (10 <= len_array and len_array <= 100), \
        'wrong range for the length of second dim of array'


def test_make_random_whole_2_dim_array_not_default():
    elts_range = (random.randint(-1000, -100), random.randint(100, 1000))
    size_of_1_dim_range = (random.randint(10, 100),
                           random.randint(100, 1000))
    size_of_2_dim_range = (random.randint(1, 10),
                           random.randint(10, 100))
    array = make_random_whole_2_dim_array(
        elts_range=elts_range,
        size_of_1_dim_range=size_of_1_dim_range,
        size_of_2_dim_range=size_of_2_dim_range)
    for row in array:
        for i in row:
            assert (elts_range[0] <= i and i <= elts_range[1]), \
                'there are elements not in the default array range'
            assert isinstance(i, int), 'not all elements are float'
        len_row = len(row)
        assert (size_of_1_dim_range[0] <= len_row
                and len_row <= size_of_1_dim_range[1]), \
            'wrong range for the length of array'
    len_array = len(array)
    assert (size_of_2_dim_range[0] <= len_array
            and len_array <= size_of_2_dim_range[1])
