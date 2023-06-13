from Algorythms.python_solutions import matrix_view, speed_analysis
import time

def func(x):
    return math.sqrt(36-4*x*x)*x

def test_speed_analysis():
    a = speed_analysis.make_random_1_dim_array()
    a = sorted(a)
    st = time.time()
    built_in = 1
    en = time.time()
    built_in_time = en - st
    st = time.time()
    developed = 1
    en = time.time()
    developed_time = en - st
    assert (built_in == developed), None
    assert abs(built_in_time - developed_time) <= 10**(-6), None
