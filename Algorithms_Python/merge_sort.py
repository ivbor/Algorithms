"""
Merge Sort Module
=================

A module containing Merge Sort algorithms and a helper function for merging
arrays. This module specializes in various implementations of the Merge Sort
algorithm and a helper function for merging two sorted arrays into a single
sorted array.

Functions
---------
merge(array: list[float], part_one: list[float], part_two: list[float])
    -> None
    Merge two sorted arrays into a single sorted array.

merge_sort(array: list[float], opt: bool = True, batch_size: int = 3)
    -> list[float]
    Sort a list of elements using the Merge Sort algorithm.
    Optimised version (opt=True) calls Insertion Sort for small arrays.

merge_sort_parallel(array: list[float], batch_size=None, depth=0)
    -> list[float]
    Sort a list of elements with multiprocessing using the Merge Sort
    algorithm.

parallel_merge_sort(arr: list[float], batch_size=None, depth=0)
    -> list[float]
    Function-helper for merge_sort_parallel which handles recursion
    and multiprocessing.

Constants
---------
MERGE_OPT: bool
    Determines whether the merge sort will utilize insertion sort at all
    or not. Assumes a value automatically based on whether it is possible
    to import insertion sort function.

MAX_DEPTH: int
    Recursion control constant. Determines the depth after which parallel
    merge sort implementation will not call recursion any longer.
    Default is set to cpu_count.

"""

import logging


from multiprocessing import cpu_count
from concurrent.futures import ProcessPoolExecutor as Pool


try:
    from Algorithms_Python.insert_sort import insert_sort_opt
    MERGE_OPT = True
except ImportError:
    logging.info('insert_sort_opt function cannot be imported, ' +
                 'defaulting to the slower version of merge_sort with ' +
                 'opt=False parameter')
    MERGE_OPT = False

MAX_DEPTH = cpu_count()


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

    if part_one[-1] < part_two[0]:
        array[:len(part_one)] = part_one
        array[len(part_one):] = part_two
        return

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


def merge_sort(array: list[float], opt: bool = MERGE_OPT,
               batch_size=3) -> list[float]:
    '''
    Merge Sort

    This function implements the Merge Sort algorithm
    to sort a list of elements.

    The Merge Sort algorithm works by dividing the input list into
    two halves, recursively sorting each half, and then merging the
    two sorted halves into one sorted list.
    Time Complexity is O(n*log(n)), space complexity - O(n).
    Space is used for storing divided subarrays during sorting.

    Parameters
    ----------
    array: list[float]
        The input list to be sorted.

    opt: bool
        A switch between faster version using Insertion Sort
        on small arrays and slower version without it. Default is True.

    batch_size: int
        A threshold for switching between further dividing the input and
        binary search optimized insertion sort, if opt is True.
        Default, tuned for the best performance, value is 3.

    Returns
    -------
    list[float]
        A new list containing the elements of the input list
        in sorted order.
    '''
    length_array = len(array)

    if (length_array == 1):
        return array

    if opt and length_array <= batch_size:
        return insert_sort_opt(array)

    mid = len(array) // 2
    left_part_of_array = array[:mid]
    right_part_of_array = array[mid:]

    left_part_of_array = merge_sort(left_part_of_array)
    right_part_of_array = merge_sort(right_part_of_array)

    merge(array, left_part_of_array, right_part_of_array)

    return array


def parallel_merge_sort(arr: list[float],
                        batch_size=None, depth=0) -> list[float]:

    batch_size = batch_size if batch_size is not None \
        else (len(arr) // 100) + 1
    length = len(arr)
    if length <= 1:
        return arr
    elif length <= batch_size:
        return merge_sort(arr)
    else:
        mid = length // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        # for recursion depth control
        if depth < MAX_DEPTH:
            # Use a dynamic ProcessPoolExecutor for parallel sorting
            with Pool(max_workers=cpu_count()) as pool:
                left_sorted = pool.submit(
                    parallel_merge_sort, left_half,
                    batch_size, depth + 1)
                right_sorted = pool.submit(
                    parallel_merge_sort, right_half,
                    batch_size, depth + 1)

                left_sorted = left_sorted.result()
                right_sorted = right_sorted.result()

                merge(arr, left_sorted, right_sorted)
        else:
            merge(arr, parallel_merge_sort(left_half, batch_size, depth+1),
                  parallel_merge_sort(right_half, batch_size, depth+1))

        return arr


def merge_sort_parallel(array: list[float],
                        batch_size=None, depth=0) -> list[float]:
    '''
    Parallel Merge Sort using dynamic ThreadPoolExecutor

    This function implements the Merge Sort algorithm in parallel
    to sort a list of elements.

    Parameters
    ----------
    array: list[float]
        The input list to be sorted.

    batch_size: int
        A threshold to switch from parallel algorithm to the usual one
        once the part to be sorted will become as small as a batch_size.
        Default is None, which would later translate to
        (len(array) // 100) + 1

    depth: int
        Recursion depth control parameter, used for avoiding overheading.
        Default is 4. If set to None will translate to the number of cores.

    Returns
    -------
    list[float]
        A new list containing the elements of the input list in sorted order.

    '''
    return parallel_merge_sort(array, batch_size=batch_size, depth=depth)
