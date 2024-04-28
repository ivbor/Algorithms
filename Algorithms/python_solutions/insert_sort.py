"""
Insertion Sort
==============

A module with Insertion Sort algorithm to sort a list of elements.

Insertion Sort is a simple sorting algorithm that works by iterating through
the input list and, for each element, comparing it with the elements to its
left and inserting it into its correct position within the already sorted
portion of the list. This process continues until the entire list is sorted.

Functions
---------
insert_sort(array: list[float]) -> list[float]
    Sorts a list of elements using the Insertion Sort algorithm.

insert_sort_opt(array: list[float]) -> list[float]
    Sorts a list of elements using the optimized Insertion Sort algorithm.
    This version uses binary search to find the correct position for each
    element, reducing the number of comparisons and improving efficiency.

"""


def insert_sort(array: list[float]) -> list[float]:
    """
    This function implements the Insertion Sort algorithm
    to sort a list of elements in-place.

    The Insertion Sort algorithm works by iterating through the input list,
    and for each element, it compares it with the elements
    to its left and inserts it into its correct position within
    the already sorted portion of the list.
    This process continues until the entire list is sorted.
    Worst and average cases time complexity - O(n^2).
    Space complexity - O(1) as sorting is done in-place.

    Parameters
    ----------
    array : list
        The input list to be sorted.

    Returns
    -------
    list
        A list containing the elements of the input list in sorted order.

    """

    for i in range(len(array)):
        k = i
        while (k > 0 and array[k - 1] > array[k]):
            array[k - 1], array[k] = array[k], array[k - 1]
            k -= 1
    return array


def bin_search_fl(array: list[float], value: float,
                  start: int, end: int) -> int:
    '''
    A binary search in the array slice consisting of floats.

    It searches for the place where to put the value
    while preserving an ascending order.

    Parameters
    ----------
    array: list[float]
        An array to search in.

    value: float
        A value to search a place for.

    start: int
        An index pointing at the slice's left border inclusively.

    end: int
        An index pointing at the slice's right border inclusively.

    Returns
    -------
    int
        An index pointing to the place where the value should land.

    '''

    while start < end:
        mid = (start + end) // 2
        if array[mid] < value:
            start = mid + 1
        else:
            end = mid
    return start


def insert_sort_opt(array: list[float]) -> list[float]:
    """
    This function implements the in-place Insertion sort algorithm
    enhanced by binary search.

    Sorts a list of elements using the optimized Insertion Sort algorithm.
    This version uses binary search to find the correct position for each
    element, reducing the number of comparisons and improving efficiency.

    Parameters
    ----------
    array : list
        The input list to be sorted.

    Returns
    -------
    list
        A list containing the elements of the input list in sorted order.

    """

    for i in range(1, len(array)):
        current_element = array[i]
        correct_pos = bin_search_fl(array, current_element, 0, i)

        # Shift elements to make space for the current_element
        array[correct_pos + 1:i + 1] = array[correct_pos:i]

        array[correct_pos] = current_element

    return array
