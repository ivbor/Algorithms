from mock import patch


def test_import_error_for_merge():
    with patch.dict('sys.modules',
                    {'Algorithms.python_solutions.insert_sort': None}):
        from importlib import reload
        import Algorithms.python_solutions.merge_sort as merge_sort
        reload(merge_sort)
        assert merge_sort.MERGE_OPT is False


def test_merge_sort_easy_merge():
    from importlib import reload
    import Algorithms.python_solutions.merge_sort as merge_sort
    reload(merge_sort)
    assert merge_sort.MERGE_OPT is True

    array = [i for i in range(1000)]
    array_copy = array.copy()
    merge_sorted_array = merge_sort.merge_sort(array)
    assert sorted(array_copy) == merge_sorted_array
