"""
Two-Dimensional Array Count Sort Module
========================================

This module provides a function, `two_dim_array_count_sort`, for sorting a
2-dimensional array consisting of whole numbers. The function can sort the
1-dimensional arrays inside a 2-dimensional array in ascending order by all
indexes (by default) or by exact indexes in the order they are presented.

Functions
---------
two_dim_array_count_sort(a: list[list[int]], keys: str | list | int = 'all')
    Sorts a 2-dimensional array consisting of whole numbers.

"""


from Algorithms_Python.array_count_sort import array_count_sort


def two_dim_array_count_sort(
        a: list[list[int]],
        keys: str | list[int] | int = 'all') -> list[list[int]]:
    """
    Sorts a 2-dimensional array consisting of whole numbers.

    This function sorts the 1-dimensional arrays inside a 2-dimensional array
    in ascending order by all indexes (by default) or by exact indexes
    in the order they are presented. Be mindful that this sort populates
    an array with absent places in each row's key position with sentinel
    values (-inf). In this case the ascending sort will always lead to rows
    with absent values being put higher than ones without them.

    Parameters
    ----------
    a : list[list[int]]
        The 2-dimensional array to be sorted.

    keys : 'all', list of int, or int, optional
        Specifies the indexes to sort by. If 'all', it sorts by all indexes
        (default). If a list of integers is provided, it sorts by the exact
        indexes in the specified order. If an integer is provided,
        it sorts by a single index.

    Returns
    -------
    list[list[int]]
        The sorted 2-dimensional array.

    Raises
    ------
    TypeError
        Raised if the 'keys' argument is of an unsupported type.

    """
    if keys == 'all' or isinstance(keys, list):
        max_len = max(len(row) for row in a)
        keys = list(range(max_len)) if keys == 'all' else keys

        # Here the sentinel values are introduced into array
        # If you want them to be under all rows with present values -
        # you can change -inf to inf
        a_padded = [row + [float('-inf')] * (max_len - len(row)) for row in a]

        # Sort the padded array
        for key in reversed(keys):
            a_padded = array_count_sort(a_padded, key=key)

        a_sorted_padded = a_padded

        # Remove the padded zeros
        a = [list(filter(lambda x: x != float('-inf'), row))
             for row in a_sorted_padded]

    elif isinstance(keys, int):
        a = array_count_sort(a, key=keys)
    else:
        raise TypeError('Cannot parse keys')
    return a
