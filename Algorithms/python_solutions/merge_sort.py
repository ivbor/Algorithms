from multiprocessing import cpu_count
from concurrent.futures import ThreadPoolExecutor as Pool


def merge(array_one, array_two):
    """
    Merge Two Sorted Arrays

    This function merges two sorted arrays, `array_one` and `array_two`, into
    a single sorted array. This is a helper for the Merge Sort function.
    Both space and time complexities are O(n), where n - the number of
    elements inside two arrays combined.

    Parameters
    ----------
    array_one: list
        The first sorted array to be merged.

    array_two: list
        The second sorted array to be merged.

    Returns
    -------
    list
        A new sorted array containing elements from both input arrays.

    """
    length_array_one = len(array_one)
    length_array_two = len(array_two)
    index_for_array_one = 0
    index_for_array_two = 0
    merged_array = \
        [0 for _ in range(len(array_one) + len(array_two))]

    # end for both is not reached
    while (index_for_array_one + index_for_array_two <
           length_array_one + length_array_two):

        # move forward in the array one if

        # end for the second is reached or
        # we can (end for the first is not reached)
        # and need to move forward inside array one
        # (i-th element from the first
        # less than j-th element from the second)
        if (index_for_array_two == length_array_two or
           (index_for_array_one < length_array_one and
                array_one[index_for_array_one] <
                array_two[index_for_array_two])):

            # append to c an element from the first
            merged_array[index_for_array_one + index_for_array_two] = \
                array_one[index_for_array_one]
            index_for_array_one += 1

        # end for the first is reached but not for the second
        # or bpth ends are not reached and element from array two
        # less than element from array one
        else:

            # append to c an element from the second
            merged_array[index_for_array_one + index_for_array_two] = \
                array_two[index_for_array_two]
            index_for_array_two += 1
    del array_one
    del array_two
    return merged_array


def merge_sort(array):
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
    array: list
        The input list to be sorted.

    Returns
    -------
    list
        A new list containing the elements of the input list in sorted order.
    '''
    length_array = len(array)
    if (length_array == 1):
        return array
    left_part_of_array = array[:round(length_array / 2)]
    right_part_of_array = array[round(length_array / 2):length_array]
    left_part_of_array = merge_sort(left_part_of_array)
    right_part_of_array = merge_sort(right_part_of_array)
    return merge(left_part_of_array, right_part_of_array)


# Merge sort employing parallelism and written by ChatGPT
def merge_sort_parallel(array):
    '''
    Parallel Merge Sort using dynamic ThreadPoolExecutor

    This function implements the Merge Sort algorithm in parallel
    to sort a list of elements.

    Parameters
    ----------
    array: list
        The input list to be sorted.

    Returns
    -------
    list
        A new list containing the elements of the input list in sorted order.
    '''
    def parallel_merge_sort(arr, executor):
        if len(arr) <= 1:
            return arr
        else:
            mid = len(arr) // 2
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

            return merge(left_sorted, right_sorted)

    return parallel_merge_sort(array, Pool)
