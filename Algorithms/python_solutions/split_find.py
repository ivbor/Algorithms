import random


def split(array, pivot, left_edge, right_edge):
    """
    Splits an array into two parts based on a pivot value.

    This function partitions the input array into two subarrays.
    Elements less than pivot are moved to the left subarray,
    and elements equal to pivot (within a small tolerance)
    or greater are moved to the right subarray.

    Parameters
    ----------
    array: list[float]
        The input array to be split and partially sorted.

    pivot: float
        The pivot value used for partitioning the array.

    left_edge: int
        The starting index of the subarray to be split.

    right_edge: int
        The ending index (exclusive) of the subarray to be split.

    Returns
    -------
    tuple[int, int]
        A tuple containing the new left and right edges of the split subarrays.
        If all elements are moved to one side, it returns (0, 0).
    """
    middle = left_edge
    for i in range(left_edge, right_edge):
        if array[i] < pivot:
            array[i], array[middle] = array[middle], array[i]
            middle += 1
    new_left_edge = middle
    if middle == len(array):
        return 0, 0
    for i in range(new_left_edge, right_edge):
        if abs(array[i] - pivot) <= 10**-14:
            array[i], array[middle] = array[middle], array[i]
            middle += 1
    new_right_edge = middle
    return new_left_edge, new_right_edge


def _split_find(array, left_edge, right_edge, index):
    """
    Recursively finds the element at the specified index
    inside array as if that array would be sorted in ascending order.

    This function recursively searches for the element
    at the given index within the subarray defined by left_edge
    and right_edge inside array.
    It uses random pivot selection and the split function to partition
    the array while narrowing down the search range.

    Parameters
    ----------
    array: list[float]
        The input array in which to search for the element.

    left_edge: int
        The starting index of the subarray in which to search.

    right_edge: int
        The ending index (exclusive) of the subarray in which to search.

    index: int
        The target index of the element to find.

    Returns
    -------
    float
        The element found at the specified index.
    """
    pivot = array[random.randint(left_edge, right_edge - 1)]
    new_left_edge, new_right_edge = split(array, pivot, left_edge, right_edge)
    if len(array[left_edge:right_edge]) <= abs(new_left_edge - new_right_edge):
        return array[index]
    if index < new_left_edge:
        return _split_find(array, left_edge, new_left_edge, index)
    else:
        return _split_find(array, new_left_edge, right_edge, index)


def split_find(a, index):
    """
    Searches for an element with the specified index in an array
    as if it was already sorted in ascending order.

    This function searches for the element at the specified index in
    ascending order in the input array without fully sorting the array.
    It uses the _split_find function to perform the search.
    If an array is already sorted this algorithm becomes Binary search.
    If not - average and worst cases lead to O(n^2) time complexity
    (as if you would have to perform the entire quick sort before search).

    Parameters
    ----------
    a: list[float]
        The input array in which to search for the element.

    index: int
        The target index of the element to find.

    Returns
    -------
    float
        The element found at the specified 'index'.

    """

    return _split_find(a, 0, len(a), index)
