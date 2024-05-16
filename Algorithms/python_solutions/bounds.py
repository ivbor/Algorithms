"""
Binary Boundaries Search Module
===============================

This module provides implementations of lower_bound and upper_bound
search algorithms for finding the first and last occurrences of a given
whole-numbered value in a sorted array. The lower_bound algorithm returns
the index of the first encounter of the value, while the upper_bound algorithm
returns the index of the last encounter.

Functions
---------
_lower_bound(array: list[int], left_edge: int, right_edge: int,
        value_to_search: int) -> int:
    This is lower bound search helper.

lower_bound(array: list[int], value_to_search: int) -> int
    Determines the index of the first encounter of the whole-numbered value
    in a sorted array.

upper_bound(array: list[int], value_to_search: int) -> int
    Determines the index of the last encounter of the whole-numbered value
    in a sorted array.

"""


def _lower_bound(array: list[int], left_edge: int, right_edge: int,
                 value_to_search: int) -> int:
    '''
        This is lower bound search helper.

        Lower bound search works on the cut,
        so edges of the cut inside the array have to be provided.
        Array has to be sorted already, time and complexity equal
        to the binary search with recursion.

        Parameters
        ----------
        array: list[int]
            one-dimensional array consisting of whole numbers

        left_edge: int
            index inside the array meaning left edge of indexes
            inside array (itself included) where search will be performed

        right_edge: int
            index inside the array meaning right edge of indexes
            inside array (itself included) where search will be performed

        value_to_search: int
            value to be searched among the given indexes slice inside array

        Returns
        -------
        int
            index there the lower bound with required value is located
    '''

    # determine the position of the middle element
    middle = int((left_edge + right_edge) / 2)

    # if the length of the array is 1
    # then it is lower_bound of value_to_search
    # and we return it immediately
    if left_edge == right_edge - 1:
        return right_edge

    # if the length of the current cut
    # is more than 1 - it is because
    # there are many values_to_search or they
    # are polluted by non-values_to_search

    # either way we need to clean them up
    # until one element (the leftest
    # among all values_to_search) is left
    if value_to_search <= array[middle]:
        return _lower_bound(array, left_edge, middle, value_to_search)
    else:
        return _lower_bound(array, middle, right_edge, value_to_search)


def lower_bound(array: list[int], value_to_search: int) -> int:
    '''
        This function determines where is first encounter of the whole-
        numbered value.

        This function utilizes algorithm working on the cut, hence the
        searching job is delegated to the function-helper. The algorithm
        itself is similar to the binary search without any additional
        calculation complexity.
        Array where is the value to be searched for has to be already sorted.
        Function assumes by-default the presence of the value to be searched.

        Parameters
        ----------
        array: list[int]
            Sorted array where to find the first encounter of the
            searched value.

        value_to_search: int
            Searched value which first encounter is to be found by the
            function.

        Returns
        -------
        int
            index of the first encounter of the searched value
    '''
    return _lower_bound(
        array, left_edge=0, right_edge=len(array) - 1,
        value_to_search=value_to_search)


def upper_bound(array: list[int], value_to_search: int) -> int:
    '''
        This function determines where is the last encounter of the whole-
        numbered value.

        This function is very similar to the lower_bound() except for it
        searches for the last encounter. Generally, it is done via
        lower_bound of the next (+1) whole value and subtraction 1 from the
        returned index.

        Parameters
        ----------
        array: list[int]
            Sorted array where to find the last encounter of the
            searched value.

        value_to_search: int
            Searched value which last encounter is to be found by the
            function.

        Returns
        -------
        int
            index of the last encounter of the searched value

    '''
    return _lower_bound(array, left_edge=0, right_edge=len(array) - 1,
                        value_to_search=value_to_search + 1) - 1
