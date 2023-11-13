"""
Merge Sort Module
=================

A module containing Merge Sort algorithms and a helper function for merging
arrays.

This module specializes in various implementations of the Merge Sort
algorithm and a helper function for merging two sorted arrays into a single
sorted array.

Functions
---------
merge_sort(array: list[float], opt: bool = True) -> list[float]
    Sort a list of elements using the Merge Sort algorithm.
    If optimised version is called uses Insertion Sort for small arrays.

merge_sort_parallel(array: list[float]) -> list[float]
    Sort a list of elements with multiprocessing using the Merge Sort
    algorithm.

merge(array: list[float], part_one: list[float], part_two: list[float])
    -> None
    Merge two sorted arrays into a single sorted array.

"""

from multiprocessing import cpu_count
from concurrent.futures import ThreadPoolExecutor as Pool

from Algorithms.python_solutions.insert_sort import insert_sort_opt


def merge(array: list[float], part_one: list[float],
          part_two: list[float]) -> None:
    """
    Merge Two Sorted Arrays

    This function merges two sorted arrays, `part_one` and `part_two`, into
    a single sorted array. This is a helper for the Merge Sort function.
    Both space and time complexities are O(n), where n - the number of
    elements inside two arrays combined.

    Parameters
    ----------
    array: list[float]
        The resulting array

    part_one: list[float]
        The first sorted array to be merged.

    part_two: list[float]
        The second sorted array to be merged.

    Returns
    -------
    None

    """

    length_part_one = len(part_one)
    length_part_two = len(part_two)
    index_for_part_one = 0
    index_for_part_two = 0
    index_for_array = 0

    while (index_for_part_one < length_part_one and
           index_for_part_two < length_part_two):

        if (part_one[index_for_part_one] <
                part_two[index_for_part_two]):

            array[index_for_array] = part_one[index_for_part_one]
            index_for_part_one += 1

        else:

            array[index_for_array] = part_two[index_for_part_two]
            index_for_part_two += 1
        index_for_array += 1

    while index_for_part_one < length_part_one:
        array[index_for_array] = part_one[index_for_part_one]
        index_for_part_one += 1
        index_for_array += 1

    while index_for_part_two < length_part_two:
        array[index_for_array] = part_two[index_for_part_two]
        index_for_part_two += 1
        index_for_array += 1


def merge_sort(array: list[float], opt: bool = True) -> list[float]:
    '''
    Merge Sort

    This function implements the Merge Sort algorithm
    to sort a list of elements.

    The Merge Sort algorithm works by dividing the input list into two halves,
    recursively sorting each half, and then merging the two sorted halves into
    one sorted list.
    Time Complexity is O(n*log(n)), space complexity - O(n). Space is used for
    storing divided subarrays during sorting.

    Parameters
    ----------
    array: list[float]
        The input list to be sorted.

    opt: bool
        A switch between faster version using Insertion Sort on small arrays
        and slower version without it. Default is True.

    Returns
    -------
    list[float]
        A new list containing the elements of the input list in sorted order.
    '''
    length_array = len(array)

    if (length_array == 1):
        return array

    if opt and length_array <= 70:
        return insert_sort_opt(array)

    mid = len(array) // 2
    left_part_of_array = array[:mid]
    right_part_of_array = array[mid:]

    left_part_of_array = merge_sort(left_part_of_array)
    right_part_of_array = merge_sort(right_part_of_array)

    merge(array, left_part_of_array, right_part_of_array)

    return array


def merge_sort_parallel(array: list[float]) -> list[float]:
    '''
    Parallel Merge Sort using dynamic ThreadPoolExecutor

    This function implements the Merge Sort algorithm in parallel
    to sort a list of elements.

    Parameters
    ----------
    array: list[float]
        The input list to be sorted.

    Returns
    -------
    list[float]
        A new list containing the elements of the input list in sorted order.
    '''

    def parallel_merge_sort(arr: list[float],
                            executor: Pool = Pool) -> list[float]:

        length = len(arr)
        if length <= 1:
            return arr
        elif length <= 32:
            return merge_sort(arr)
        else:
            mid = length // 2
            left_half = arr[:mid]
            right_half = arr[mid:]

            # Use a dynamic ThreadPoolExecutor for parallel sorting
            with executor(max_workers=cpu_count()) as pool:
                left_sorted = pool.submit(
                    parallel_merge_sort, left_half, executor)
                right_sorted = pool.submit(
                    parallel_merge_sort, right_half, executor)

                left_sorted = left_sorted.result()
                right_sorted = right_sorted.result()

            merge(arr, left_sorted, right_sorted)
            return arr
    return parallel_merge_sort(array)
