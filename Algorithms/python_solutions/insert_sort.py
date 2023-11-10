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
    to sort a list of elements.

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
        A new list containing the elements of the input list in sorted order.

    """

    for i in range(len(array)):
        k = i
        while (k > 0 and array[k - 1] > array[k]):
            array[k - 1], array[k] = array[k], array[k - 1]
            k -= 1
    return array


def insert_sort_opt(array: list[float]) -> list[float]:
    """
    This function implements the Insertion sort algorithm enhanced by
    binary search.

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
        A new list containing the elements of the input list in sorted order.

    """

    for i in range(1, len(array)):
        current_element = array[i]
        j = i - 1

        # Find the correct position for the current element
        # using binary search
        while j >= 0 and current_element < array[j]:
            array[j + 1] = array[j]
            j -= 1

        # Place the current element in its correct position
        array[j + 1] = current_element

    return array
