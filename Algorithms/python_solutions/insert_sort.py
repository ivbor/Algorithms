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
insert_sort(array)
    Sorts a list of elements using the Insertion Sort algorithm.
"""


def insert_sort(array):
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
