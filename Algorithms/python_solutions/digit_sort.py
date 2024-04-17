"""
Digit Sort
==================================

This module provides functions for performing digit sort, a sorting algorithm
specifically designed for integers.

Functions
---------
digit_sort(array: list[int], base: int = 10) -> list[int]
    Sort a list of non-negative integers using the digit sort algorithm.

to_m_based(number: int, base: int) -> list[int]
    Convert a decimal number to an M-based representation.

restore_to_nums(array: list[int], base: int = 10) -> int
    Restore an M-based representation to its decimal form.

"""
from Algorithms.python_solutions.two_dim_array_count_sort \
    import two_dim_array_count_sort


def to_m_based(number: int, base: int) -> list[int]:
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
    if base <= 2 and not isinstance(base, int):
        raise ValueError('base is not a positive integer greater than or ' +
                         'equal to 2')

    m_based = []
    while number != 0:
        number, remainder = divmod(number, base)
        m_based.insert(0, remainder)
    return m_based


def restore_to_nums(array: list[int], base: int = 10) -> int:
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
    for digit in array:
        number = number * base + digit
    return number


def digit_sort(array: list[int], base: int = 10) -> list[int]:
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
    min_of_array = min(array, default=0)

    # translate any numeration to the m-based
    array = [to_m_based(i - min_of_array, base) for i in array]

    # translate array to 2-dim array, where k is number of digits,
    # add 0 before numbers where less than k digits so that
    # new 2dim list would be rectangular matrix
    max_length_of_a_i = max([len(i) for i in array])
    array = [[0] * (max_length_of_a_i - len(m)) + m for m in array]

    # use imported func to sort 2-dim arrays
    array = two_dim_array_count_sort(array)

    # restore numbers from arrays
    array = [restore_to_nums(i, base) + min_of_array for i in array]

    return array


def digit_sort_opt(array: list[int], base: int = 10) -> list[int]:
    """
    Sort a list of non-negative integers using the digit + radix sort
    algorithm.

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
    # Extend on negative numbers (- base^k < array[i] < base^k)
    min_of_array = min(array, default=0)

    # Normalize the array to positive values
    array = [i - min_of_array for i in array]

    # Find the maximum number of digits in any integer in the array
    max_digits = max([len(str(i)) for i in array], default=1)

    # Perform radix sort on each digit from least significant to most
    # significant
    for digit_place in range(max_digits):
        buckets = [[] for _ in range(base)]

        for num in array:
            # Extract the digit at the current place value
            digit = (num // (base ** digit_place)) % base
            buckets[digit].append(num)

        # Reconstruct the array based on the current digit place
        array = [num for bucket in buckets for num in bucket]

    # Restore numbers to their original form
    array = [num + min_of_array for num in array]

    return array
