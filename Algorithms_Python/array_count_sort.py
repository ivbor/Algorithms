"""
Array Counting Sort Module
==========================

Functions
---------
array_count_sort(arr: list[list[int]], key: int = 0) -> list[list[int]]
    Sort a 2-dimensional array of integers based on a key index.

"""


def array_count_sort(arr: list[list[int]], key: int = 0) -> list[list[int]]:
    """
        This function performs counting sort on the 2-dimensional array
        of whole numbers.

        This algorithm uses count sort to sort rows inside matrix
        by ascending order. It works only with integer numbers,
        so if your matrix contains floats - do not use this algorithm.
        Time to work: O(number of rows in the array) or
        O(difference between the biggest and the lowest value
        in the key index) depending on what is more.

        Parameters
        ----------
        array : list[list[int]]
            2-dimensional array which will be sorted

        key : int
            Shows by which index to sort, works even in situations
            when there are blank spaces with this index in the rows.
            In this case puts those rows higher than those with
            filled spaces.
            Default value: 0

        Returns
        -------
        list[list[int]]
            Sorted array

    """

    # Helper function for stable counting sort based on a specific key
    max_value = max([row[key] for row in arr if row[key] != float('-inf')])
    min_value = min([row[key] for row in arr if row[key] != float('-inf')])
    count = [0] * (max_value - min_value + 2)

    # Count occurrences of each key
    for row in arr:
        if row[key] != float('-inf'):
            count[row[key] - min_value] += 1
        else:
            count[max_value - min_value + 1] += 1

    # Calculate cumulative count
    for i in range(1, len(count)):
        count[i] += count[i - 1]

    # Build the sorted array
    result = [0] * len(arr)
    for row in reversed(arr):
        if row[key] != float('-inf'):
            count[row[key] - min_value] -= 1
            result[count[row[key] - min_value]] = row
        else:
            count[max_value - min_value + 1] -= 1
            result[count[max_value - min_value + 1]] = row

    # Update the original array with the sorted values
    for i in range(len(arr)):
        arr[i] = result[i]

    return arr
