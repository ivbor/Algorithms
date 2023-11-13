"""
Counting Sort Module
====================

This module provides an implementation of the counting sort algorithm
for sorting an array of whole numbers.

The counting sort algorithm counts the occurrences of each whole number
in the input array and uses this information to create a sorted array.
It is particularly efficient when the range of values is small compared
to the array size.

Functions
---------
count_sort(array: list[int]) -> list[int]
    Sorts an array of whole numbers using the counting sort algorithm.

"""


def count_sort(array: list[int]) -> list[int]:
    """
        This function implements counting sort on the array of whole numbers.

        The algorithm of counting sort employs the basic counting
        of the whole numbers inside array. It creates another array with
        (max - min + 1) size, and counts, how many elements with each number
        were inside the array to be sorted.
        Time to work: O(size of array + difference between the biggest and
        the smallest elements)

        Parameters
        ----------
        array: list[int]
            array to be sorted consisting of whole numbers

        Returns
        -------
        list[int]
            sorted array
    """
    lenght_of_array = len(array)
    min_of_array = min(array)
    max_of_array = max(array)
    array_of_counters = [0 for _ in range(max_of_array + 1 - min_of_array)]
    for i in range(lenght_of_array):
        array_of_counters[array[i] - min_of_array] += 1

    i = 0
    new_array = array.copy()
    for j in range(max_of_array + 1 - min_of_array):
        while (array_of_counters[j] > 0):
            new_array[i] = j + min_of_array
            i += 1
            array_of_counters[j] -= 1
    return new_array
