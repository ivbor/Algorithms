import pytest
from Algorithms_Python.real_bin_search import real_bin_search


def test_real_bin_search_desc():
    def func(x): return -x
    assert abs(9 - real_bin_search(func, -9, -100, 100)) < 1e-6, \
        'real bin search works wrong for descending function'


def test_real_bin_search_asc():
    def func(x): return x
    assert abs(6 - real_bin_search(func, 6, -100, 100)) < 1e-6, \
        'real bin search works wrong for ascending function'


def test_search_with_check():
    def func(x): return x*x
    assert abs(4 - real_bin_search(func, 16, 0, 100, check=True)) < 1e-6, \
        'check is not working in the search function'


def test_search_raises_error_when_result_behind_edges_when_check_enabled():
    def func(x): return x*x
    with pytest.raises(Exception):
        real_bin_search(func, 16, -3, 3, check=True)
