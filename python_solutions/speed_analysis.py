import time, random
from Algorythms.python_solutions import matrix_view

def speed_analysis(func, array, params, tests_num = 10, check = False):

    sum = 0
    b = array.copy()
    for i in range(tests_num):
        st = time.time()
        c = func(b, **params)
        et = time.time()
        if check:
            matrix_view.matrix_view_2dim(c, True)
            del c
        b = array.copy()
        sum += et - st
    return sum / tests_num

def make_random_2_dim_array(elts_val_min = -10, elts_val_max = 10, size_of_1_dim_min = 1, size_of_1_dim_max = 10, size_of_2_dim_min = 10, size_of_2_dim_max = 100):
    return [[random.randint(elts_val_min, elts_val_max) \
        for i in range(random.randint(size_of_1_dim_min, size_of_1_dim_max))] \
        for i in range(random.randint(size_of_2_dim_min, size_of_2_dim_max))]

def make_random_1_dim_array(elts_val_min = -100, elts_val_max = 100, size_of_1_dim_min = 100, size_of_1_dim_max = 1000):
    return [random.randint(elts_val_min, elts_val_max) \
        for i in range(random.randint(size_of_1_dim_min, size_of_1_dim_max))]
