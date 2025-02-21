"""
Real Binary Search Module

This module provides a binary search function for finding an approximate
input value (x) for which a given function func(x) is close to func_value
within a specified epsilon. The binary search algorithm is suitable for
monotonic functions.

Functions
---------
real_bin_search(func, func_value, left_edge,
    right_edge, eps=1e-6, check=False)
    Performs a binary search among real numbers to find an x
    where func(x) is approximately equal to func_value.

"""


def real_bin_search(func, func_value, left_edge,
                    right_edge, eps=1e-6, check=False):
    """
    This function performs a binary search among real numbers to find an x
    where func(x) is approximately equal to func_value.

    It works only for monotonic functions and
    has a time complexity of O(log2(n)),
    where n is the number of epsilon intervals that can fit in the
    absolute difference between right_edge and left_edge.

    Parameters
    ----------
    func: callable
        The function for which we are searching for an input value.

    func_value: float
        The target value we want to find an input value for.

    left_edge: float
        The left edge of the search interval.
        The function is assumed to exist within this interval.

    right_edge: float
        The right edge of the search interval.
        The function is assumed to exist within this interval.

    eps: float, optional
        The epsilon value that determines the desired accuracy of the result.
        The search will stop when the interval size
        becomes smaller than this epsilon. Default is 1e-6.

    check: bool, optional
        If True, the function will perform a check to ensure that
        the func_value is reachable within the given edges. Default is False.

    Returns
    -------
    float
        The approximate input value (x) for which func(x) is close to
        func_value within the specified epsilon.

    Raises
    ------
    KeyError
        Is raised if the check parameter is set to True and the func_value is
        unreachable within the given edges.
    """

    # this algo requires O(log2(n))
    # operations where n is the amount of
    # the smallest cuts we consider (epsilons)
    # that can fit in abs(r-l)

    if check:
        result = real_bin_search(
            func,
            func_value,
            left_edge - 1,
            right_edge + 1)
        if (result < left_edge or right_edge < result):
            raise KeyError('func_value is unreachable within given edges')

    # determine whether function is
    # ascending or descending

    # l+eps and r-eps we use
    # so that search can work
    # even if function does not
    # exist in l or r
    is_ascending = (func(left_edge + eps) < func(right_edge - eps))

    # we can use while to ensure accuracy
    # is no less than eps
    while (abs(right_edge - left_edge) >= eps):

        # find the middle of the cut
        middle = (left_edge + right_edge)/2

        if is_ascending:

            # if function is ascending
            # and function is less than y
            # this means y is somewhere
            # in bigger x's (righer)
            # so move left border of the
            # current cut to the middle
            if func(middle) < func_value:
                left_edge = middle

            # if ascending and function
            # is more than y - this means
            # y is lesser x's (lefter)
            # so move right border of the
            # current cut to the middle
            else:
                right_edge = middle

        # for descending - everything
        # works accordingly with the
        # change of sign in if clause
        else:
            if func(middle) > func_value:
                left_edge = middle
            else:
                right_edge = middle

    # for even more accuracy
    # as an answer give the middle
    # of the accurate enough cut
    return (left_edge + right_edge)/2
