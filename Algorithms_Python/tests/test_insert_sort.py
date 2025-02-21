import random

from mock import patch


def test_import_error_for_quick():
    with patch.dict('sys.modules',
                    {'Algorithms_Python.insert_sort': None}):
        from importlib import reload
        import Algorithms_Python.quick_sort as quick_sort
        reload(quick_sort)
        assert quick_sort.QUICK_OPT is False
        array = [random.uniform(-1000, 1000) for i in range(1000)]
        array_copy = array.copy()
        quick_sorted_array = quick_sort.quick_sort(array, 'mm')
        assert sorted(array_copy) == quick_sorted_array


def test_quick_sort_median_of_medians():
    from importlib import reload
    import Algorithms_Python.quick_sort as quick_sort
    reload(quick_sort)
    assert quick_sort.QUICK_OPT is True

    array = [random.uniform(-1000, 1000) for i in range(1000)]
    array_copy = array.copy()
    quick_sorted_array = quick_sort.quick_sort(array, 'mm')
    assert sorted(array_copy) == quick_sorted_array
