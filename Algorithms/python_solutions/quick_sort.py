"""
Quick Sort Module
=================

This module provides Quick Sort implementations for efficiently sorting
a list of elements. Quick Sort is a divide-and-conquer algorithm that selects
a pivot value, divides the input array, and sorts the resulting parts.

Functions
---------
quick_sort(array: list[float], pivot_str: str = 'random') -> list[float]
    Sorts a list of elements using the Quick Sort algorithm.

split(a: list[float], pivot: float, left_edge: int, right_edge: int) ->
    tuple
    Divides the input array into two parts relative to the pivot value.

avg(a: list[float], left_edge: int, right_edge: int) -> float
    Calculates the average value of elements in a specified range.

clst_avg(a: list[float], avg: float, left_edge: int, right_edge: int) ->
    float
    Finds the element closest to the average value in a specified range.

_quick_sort(array: list[float], left_edge: int, right_edge: int,
    pivot_str: str = 'random') -> list[float]
    Performs the Quick Sort algorithm on a given array within specified
    indices.

median_of_medians(array: list[float], left: int, right: int) -> int
    Finds the index of median of medians for a given array within specified
    indices.

partition_small(array: list[float], left: int, right: int) -> int
    Sorts a small portion of the array using a bubble sort to find a
    median inside this array portion.

median_of_three(array: list[float], left: int, right: int) -> float
    Finds the median of three elements in a given array within specified
    indices.

"""


import random


def split(a: list[float], pivot: float, left_edge: int, right_edge: int) \
        -> tuple[int, int]:
    """
    Split Function

    Divide the input array  into two parts relative to the pivot value.
    Elements less than pivot are moved to the left,
    and elements greater or equal are moved to the right.

    Parameters
    ----------
    a: list[float]
        The input list to be split.

    pivot: float
        The pivot value used for splitting the array.

    left_edge: int
        The starting index for the split operation.

    right_edge: int
        The ending index (exclusive) for the split operation.

    Returns
    -------
    tuple
        A tuple containing two indices that represent the
        new boundaries for the split parts.

    """
    middle = left_edge
    for i in range(left_edge, right_edge):
        if a[i] < pivot:
            a[i], a[middle] = a[middle], a[i]
            middle += 1
    new_left_edge = middle
    for i in range(new_left_edge, right_edge):
        if a[i] == pivot:
            a[i], a[middle] = a[middle], a[i]
            middle += 1
    new_right_edge = middle
    return new_left_edge, new_right_edge


def clst_avg(a: list[float], left_edge: int, right_edge: int) -> float:
    '''
    Calculate the average value of elements in a specified range.

    Parameters
    ----------
    a: list[float]
        The input list.

    left_edge: int
        The starting index for the range.

    right_edge: int
        The ending index (exclusive) for the range.

    Returns
    -------
    float
        The average value of elements in the specified range.
    '''

    avg = sum(a[left_edge:right_edge]) / len(a[left_edge:right_edge])
    dist = abs(a[left_edge] - avg)
    idx = left_edge
    for i in range(left_edge, right_edge):
        if abs(a[i] - avg) < dist:
            dist = abs(a[i] - avg)
            idx = i
    return a[idx]


def partition_small(array: list[float], left: int, right: int) -> int:
    '''
    Partition a small portion of the array using a bubble sort algorithm.

    Parameters
    ----------
    array: list[float]
        The input array.

    left: int
        The starting index for the range.

    right: int
        The ending index (exclusive) for the range.

    Returns
    -------
    int
        The index representing the partitioned element.
    '''

    for i in range(left, right):
        for j in range(i, right):
            if array[j] < array[i]:
                array[i], array[j] = array[j], array[i]
    return (left + right) // 2


def median_of_medians(array: list[float], left: int, right: int) -> int:
    '''
    Find the median of medians for a given array within specified indices.

    Parameters
    ----------
    array: list[float]
        The input array.

    left: int
        The starting index for the range.

    right: int
        The ending index (exclusive) for the range.

    Returns
    -------
    int
        The median of medians.

    '''

    if right - left < 5:
        return partition_small(array, left, right)

    submedians = []
    for i in range(left, right, 5):
        submedians.append(partition_small(array, i, min(i + 5, right)))

    return median_of_medians(submedians, 0, len(submedians) - 1)


def median_of_three(array: list[float], left: int, right: int) -> float:
    '''
    Find the median of three elements in a given array within specified
    indices.

    Parameters
    ----------
    array: list[float]
        The input array.

    left: int
        The starting index for the range.

    right: int
        The ending index (exclusive) for the range.

    Returns
    -------
    float
        The median of three elements.

    '''

    mid = (left + right) // 2
    if array[left] > array[mid]:
        array[left], array[mid] = array[mid], array[left]
    if array[left] > array[right]:
        array[left], array[right] = array[right], array[left]
    if array[mid] > array[right]:
        array[mid], array[right] = array[right], array[mid]
    return array[mid]


def _quick_sort(array: list[float], left_edge: int, right_edge: int,
                pivot_str: str = 'random') -> list[float]:
    """
    Quick Sort Function

    Sort the input array using the Quick Sort algorithm. This function
    performs a divide-and-conquer approach by selecting a pivot value and
    splitting the array into two parts: elements less than the pivot and
    elements greater or equal to the pivot.

    Parameters
    ----------
    array: list
        The input list to be sorted.

    left_edge: int
        The starting index for the sort operation.

    right_edge: int
        The ending index (exclusive) for the sort operation.

    pivot_str: 'random', 'clst_avg', 'm3' or 'mm'
        A strategy to choose pivot element.

        'random' for random selection among the elements, works well for
        random or uniformly distributed data.

        'clst_avg' for selection of element close to the average of the
        array,  works well for data with known distribution.

        'm3' or median of three provides some resistance against worst
        cases, works well on data with some outliers or some degree of
        ordering but not fully sorted.

        'mm' of median of medians or introselect performs well consistently
        regardless of the input data

    Returns
    -------
    list
        The sorted array.

    """

    if len(array[left_edge:right_edge]) <= 1:
        return array[left_edge:right_edge]
    if pivot_str == 'random':
        pivot = array[random.randint(left_edge + 1, right_edge - 1)]
    elif pivot_str == 'clst_avg':
        pivot = clst_avg(array, left_edge, right_edge)
    elif pivot_str == 'm3':
        pivot = median_of_three(array, left_edge, right_edge - 1)
    elif pivot_str == 'mm':
        pivot = array[median_of_medians(array, left_edge, right_edge)]
    else:
        raise AttributeError('Cannot parse pivot option')
    new_left_edge, new_right_edge, = \
        split(array, pivot, left_edge, right_edge)
    _quick_sort(array, left_edge, new_left_edge)
    _quick_sort(array, new_right_edge, right_edge)
    return array[left_edge:right_edge]


def quick_sort(array: list[float], pivot_str: str = 'random') -> list[float]:
    """
    Quick Sort Function (Wrapper)

    Sort the input list using the Quick Sort algorithm. This function is a
    wrapper for the `_quick_sort` function and sets initial values for the
    sorting process. A wide selection of pivot strategies is available.
    Average and worst space complexities:
        - random: O(log n), O(n)
        - closest to the average: O(log n), O(n)
        - median of three: O(log n), O(log n)
        - median of medians: O(log n), O(log n)
    Average and worst time complexities:
        - random: O(n * log n), O(n ** 2)
        - closest to the average: O(n * log n), O(n * log n)
        - median of three: O(n * log n), O(n * log n)
        - median of medians: O(n * log n), O(n * log n)
    Important considerations:
        O(n ** 2) performance is so extremely rare, it has no implications in
        practical usage. Median of medians pivot calculation suffers from
        big constant factor, which makes it impractical for small arrays.
    It is worth noting that quick sort is unstable.

    Parameters
    ----------
    array: list
        The input list to be sorted.

    pivot_str: 'random', 'clst_avg', 'm3' or 'mm'
        A strategy to choose pivot element.

        'random' for random selection among the elements, works well for
        random or uniformly distributed data.

        'clst_avg' for selection of element close to the average of the
        array,  works well for data with known distribution.

        'm3' or median of three provides some resistance against worst
        cases, works well on data with some outliers or some degree of
        ordering but not fully sorted.

        'mm' of median of medians or introselect performs well consistently
        regardless of the input data

    Returns
    -------
    list
        The sorted list.

    """
    return _quick_sort(array, left_edge=0, right_edge=len(array),
                       pivot_str=pivot_str)
