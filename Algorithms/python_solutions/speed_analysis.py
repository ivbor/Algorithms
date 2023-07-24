import time
import random


def timeit(func, times=10):
    '''
        to time a func many (or not) times
    '''
    def inner(*args, **kwargs):
        times_list = []
        for _ in range(times):
            st = time.time()
            func(*args, **kwargs)
            et = time.time()
            times_list.append(et-st)
        return f'Average: {sum(times_list)/times: 5.0f} ' + \
               f'Min: {min(times_list): 5.0f}' + \
               f'Max: {max(times_list): 5.0f}'
    return inner


def speed_analysis(func, array, params, tests_num=10, check=True):
    '''
        Main function to register time to sort
        Takes function, its params, array to test on and
        number of tests
        also gives option to return result (check)
    '''
    sum = 0
    c = list()
    for i in range(tests_num):
        b = array.copy()
        st = time.time()
        c = func(b, **params)
        et = time.time()
        sum += et - st
    return sum / tests_num, c


def make_random_whole_2_dim_array(
        elts_range=(-10, 10), size_of_1_dim_range=(1, 10),
        size_of_2_dim_range=(10, 100)):
    return [[random.randint(*elts_range)
             for i in range(random.randint(*size_of_1_dim_range))]
            for i in range(random.randint(*size_of_2_dim_range))]


def make_random_whole_1_dim_array(
        elts_range=(-100, 100), size_of_1_dim_range=(100, 1000)):
    return [random.randint(*elts_range)
            for i in range(random.randint(*size_of_1_dim_range))]


def make_random_1_dim_array(
        elts_range=(-100, 100), size_of_1_dim_range=(100, 1000)):
    return [random.uniform(*elts_range)
            for i in range(random.randint(*size_of_1_dim_range))]


@timeit
def make_it():
    make_random_1_dim_array()


print(make_it())
