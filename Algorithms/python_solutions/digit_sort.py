"""
Digit Sort
==================================

This module provides functions for performing digit sort, a sorting algorithm
specifically designed for non-negative integers.

Functions
---------
digit_sort(array: List[int], base: int = 10) -> List[int]
    Sort a list of non-negative integers using the digit sort algorithm.

to_m_based(number: int, base: int) -> List[int]
    Convert a decimal number to an M-based representation.

restore_to_nums(array: List[int], base: int = 10) -> int
    Restore an M-based representation to its decimal form.

"""
from Algorithms.python_solutions.two_dim_array_count_sort \
    import two_dim_array_count_sort


def to_m_based(number, base):
    """
        Convert a decimal number to an M-based representation.

        This function converts a decimal number into its M-based
        representation, where M is the specified base. The result
        is returned as a list of digits in the M-based representation.
        Optionally, you can choose to return the result as an array or
        restore it to its original decimal form.

        Parameters
        ----------
        number : int
            The decimal number to be converted to an M-based representation.

        base : int
            The base (M) to which the number should be converted. It must be
            a positive integer greater than or equal to 2.

        Returns
        -------
        list[int]
            A list of integers representing the M-based representation
            of the decimal number.

    """
    m_based = []
    whole = number
    remainder = 0
    while whole != 0:
        remainder = whole % base
        whole = whole // base
        m_based.append(remainder)
    m_based = [i for i in reversed(m_based)]
    return m_based


def restore_to_nums(array, base=10):
    """
        Restore an M-based representation to its decimal form.

        This function takes a list of digits representing an M-based
        representation and restores it to its original decimal form.
        You can specify the base (M) used for the representation,
        which defaults to 10 for decimal restoration.

        Parameters
        ----------
        array : list[int]
            A list of digits representing an M-based number.

        base : int, optional
            The base (M) used for the M-based representation.
            It must be a positive integer greater than or equal to 2.
            The default value is 10 for decimal restoration.

        Returns
        -------
        int
            The decimal number restored from the M-based representation.

    """
    number = 0
    for power, multiplier in enumerate(array):
        number += pow(base, (len(array) - power - 1)) * multiplier
    return number


def digit_sort(array, base=10):
    """
        This function performs digit sort on a list of non-negative integers.

        Digit sort is a sorting algorithm that works specifically for
        non-negative integers. It sorts the integers by their individual
        digits, starting from the least significant digit to the most
        significant digit. This algorithm has a time complexity of O(n * k),
        where n is the number of integers in the input list and k is
        the maximum number of digits in any integer inside array.
        It is important that the amount of digits can be reduced by
        changing the base for the integers. Hence, when k = 1 this sort
        appears to be counting sort with O(n) time complexity.

        Parameters
        ----------
        array: list[int]
            A list of non-negative integers to be sorted using digit sort.
        base: int
            The array's integers' base depending on which number of digits
            will be determined.

        Returns
        -------
        list[int]
            A sorted list of non-negative integers.

    """

    # extend on negative numbers (- base^k < array[i] < base^k)
    min_of_array = min(array)
    if min_of_array < 0:
        array = [i - min_of_array for i in array]

    # translate any numeration to the m-based
    array = [to_m_based(i, base) for i in array]

    # translate array to 2-dim array, where k is number of digits,
    # add 0 before numbers where less than k digits so that
    # new 2dim list would be rectangular matrix
    max_length_of_a_i = max([len(i) for i in array])
    for i, m_based_number in enumerate(array):
        if len(m_based_number) < max_length_of_a_i:
            m_based_number = [j for j in reversed(m_based_number)]
            while len(m_based_number) < max_length_of_a_i:
                m_based_number.append(0)
            array[i] = [j for j in reversed(m_based_number)]

    # use written above func to sort 2-dim arrays
    array = two_dim_array_count_sort(array)

    # restore numbers from arrays
    array = [restore_to_nums(i, base) for i in array]

    # extend on negative numbers
    if min_of_array < 0:
        array = [i + min_of_array for i in array]

    return array
