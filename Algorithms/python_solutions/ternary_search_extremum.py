"""
Ternary Search Module

This module provides two functions, `tern_search_min` and `tern_search_max`,
for finding the minimum and maximum values of a function within a specified
range, respectively. These search algorithms are suitable for cases where
the function has only one minimum or maximum value within the given range.

Functions
---------
tern_search_min(func, start, end, eps=1e-6)
    Find the minimum value of a function within a specified range.

tern_search_max(func, start, end, eps=1e-6)
    Find the maximum value of a function within a specified range.

"""


def tern_search_min(func, start, end, eps=1e-6):
    '''
    Ternary search for finding the minimum value of a function
    within a specified range.

    This search algorithm is suitable for cases where the function has
    only one minimum value within the given range [start, end].
    This ternary search algorithm works with a time complexity of O(log2(n)),
    where n is the number of times the epsilon (eps) can fit in the absolute
    difference between the start and end positions.
    It determines the local minimum by comparing the function's values
    at two points within the search interval.

    Parameters
    ----------
    func: callable
        The function for which to find the minimum value.

    start: float
        The start of the range for the search.

    end: float
        The end of the range for the search.

    eps: float, optional
        The epsilon parameter controlling the accuracy
        of search. Default is 1e-6.

    Returns
    -------
    float
        The approximate x-coordinate of the minimum value of the function
        within the specified range.
    '''
    left_edge = start
    right_edge = end
    while (abs(right_edge - left_edge) >= eps):
        middle_left = left_edge + (right_edge - left_edge)/3
        middle_right = left_edge + 2 * (right_edge - left_edge)/3
        if func(middle_right) < func(middle_left):
            left_edge = middle_left
        else:
            right_edge = middle_right
    return (middle_left + middle_right)/2


def tern_search_max(func, start, end, eps=1e-6):
    '''
    Ternary search for finding the maximum value of a function
    within a specified range.

    This search algorithm is suitable for cases where the function has
    only one maximum value within the given range [start, end].
    This ternary search algorithm works with a time complexity of O(log2(n)),
    where n is the number of times the epsilon (eps) can fit in the absolute
    difference between the start and end positions.
    It determines the local minimum by comparing the function's values
    at two points within the search interval.

    Parameters
    ----------
    func: callable
        The function for which to find the maximum value.

    start: float
        The start of the range for the search.

    end: float
        The end of the range for the search.

    eps: float, optional
        The epsilon parameter controlling the accuracy of the search.
        Default is 1e-6.

    Returns
    -------
    float
        The approximate x-coordinate of the maximum value of the function
        within the specified range.

    '''
    left_edge = start
    right_edge = end
    while (abs(right_edge - left_edge) >= eps):
        middle_left = left_edge + (right_edge - left_edge)/3
        middle_right = left_edge + 2 * (right_edge - left_edge)/3
        if func(middle_right) > func(middle_left):
            left_edge = middle_left
        else:
            right_edge = middle_right
    return (middle_left + middle_right)/2
