import random


def split(a, pivot, left_edge, right_edge):
    """
    Split Function

    Divide the input array  into two parts relative to the pivot value.
    Elements less than pivot are moved to the left,
    and elements greater or equal are moved to the right.

    Parameters
    ----------
    a: list
        The input list to be split.

    pivot: any
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
    if middle == len(a):
        return 0, 0
    for i in range(new_left_edge, right_edge):
        if a[i] == pivot:
            a[i], a[middle] = a[middle], a[i]
            middle += 1
    new_right_edge = middle
    return new_left_edge, new_right_edge


# the first option, where pivot = closest to avg
def avg(a, left_edge, right_edge):
    summ = 0
    for i in a[left_edge:right_edge]:
        summ += i
    return summ/len(a[left_edge:right_edge])


# closest to avg
def clst_avg(a, avg, left_edge, right_edge):
    if len(a[left_edge:right_edge]) == 1:
        return a[left_edge]
    dist = abs(a[left_edge] - avg)
    idx = left_edge
    for i in range(left_edge, right_edge):
        if abs(a[i] - avg) < dist:
            dist = abs(a[i] - avg)
            idx = i
    return a[idx]


# l - starting index (0 for initial array)
# r - ending index (len() - 1 for initial array)
def _quick_sort(array, left_edge, right_edge, faster=True):
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

    faster : bool, optional
        A flag indicating whether to use the "faster" version of Quick Sort
        that selects a random pivot (default) or the "stable" version that
        chooses the pivot closest to the average value. Default is True.

    Returns
    -------
    list
        The sorted array.

    """

    if len(array[left_edge:right_edge]) <= 1:
        return 0
    if faster:
        pivot = array[random.randint(left_edge + 1, right_edge - 1)]
    else:
        pivot = clst_avg(array, avg(array, left_edge, right_edge),
                         left_edge, right_edge)
    new_left_edge, new_right_edge = \
        split(array, pivot, left_edge, right_edge)
    if (new_left_edge == 0 and new_right_edge == 0):
        return 0
    _quick_sort(array, left_edge, new_left_edge)
    _quick_sort(array, new_right_edge, right_edge)
    return array


def quick_sort(array):  # o(nlogn)
    """
    Quick Sort Function (Wrapper)

    Sort the input list using the Quick Sort algorithm. This function is a
    wrapper for the `_quick_sort` function and sets initial values for the
    sorting process.
    Average and worst space complexities for both random and
    closest to the average pivots are O(log n) and O(n) accordingly.
    Average and worst time complexities for random pivot are O(n * log n)
    and O(n^2). For closest to the average case - O(n * log n) both.
    It is worth noting that quick sort is unstable.

    Parameters
    ----------
    array: list
        The input list to be sorted.

    Returns
    -------
    list
        The sorted list.

    """
    return _quick_sort(array, left_edge=0, right_edge=len(array))
