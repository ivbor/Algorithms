"""
Sparse table module
===================
This module defines a SparseTable class for efficient range queries on an
array. It allows you to quickly compute the minimum, maximum, and sum of
values within a specified range. The data structure is built on a tuple for
immutability, making it suitable for scenarios where the input array should
not be modified after construction.

Classes
-------
SparseTable
    A class for creating and querying a sparse table for efficient range
    queries.

"""

import math


class SparseTable(tuple):
    """
    A class for creating and querying a sparse table for efficient range
    queries on an array.


    Attributes
    ----------
    arr : list[float]
        The input array on which range queries will be performed.

    Methods
    -------
    append(self, x: Any) -> None
        Raises an error, overwriting append for tuple, so that Sparse table
        would be completely unchangeable after creation.

    extend(self, x: Any) -> None
        Raises an error, overwriting extend for tuple, so that Sparse table
        would be completely unchangeable after creation.

    query_min(self, left: int, right: int) -> float
        Query the minimum value within a specified range, both parameters
        included.

    query_max(self, left: int, right: int) -> float
        Query the maximum value within a specified range, both parameters
        included.

    query_sum(self, left: int, right: int) -> float
        Query the cumulative sum of values within a specified range, both
        parameters included.

    __new__(cls, arr: Iterable) -> SparseTable
        Create a new instance of SparseTable using tuple's __new__()

    """

    def __init__(self, arr):
        """
        Initialize a SparseTable instance with the given input array.

        Parameters
        ----------
        arr : list[float]
            The input array on which range queries will be performed.

        Returns
        -------
        None

        """
        super().__init__()
        self.N = len(arr)
        # Number of bits needed to represent N
        self.K = int(math.log2(self.N) + 1)
        self.table_min = [[0] * self.K for _ in range(self.N)]
        self.table_max = [[0] * self.K for _ in range(self.N)]
        self.table_sum = [[0] * self.K for _ in range(self.N)]

        for i in range(self.N):
            self.table_min[i][0] = arr[i]
            self.table_max[i][0] = arr[i]
            self.table_sum[i][0] = arr[i]

        for j in range(1, self.K):
            for i in range(self.N - (1 << j) + 1):
                self.table_min[i][j] = min(
                    self.table_min[i][j - 1],
                    self.table_min[i + (1 << (j - 1))][j - 1])
                self.table_max[i][j] = max(
                    self.table_max[i][j - 1],
                    self.table_max[i + (1 << (j - 1))][j - 1])
                self.table_sum[i][j] = self.table_sum[i][j - 1] + \
                    self.table_sum[i + (1 << (j - 1))][j - 1]

    def __new__(cls, arr):
        """
        Create a new SparseTable instance.

        Parameters
        ----------
        arr : list[float]
            The input array on which range queries will be performed.

        Returns
        -------
        SparseTable
            A new instance of the SparseTable class.

        """
        return super(SparseTable, cls).__new__(cls, tuple(arr))

    def append(self, x):
        """
        This method raises a TypeError because SparseTable instances are
        immutable and cannot be changed after creation.

        Parameters
        ----------
        x : Any
            The element to be appended.

        Raises
        ------
        TypeError
            SparseTable cannot be changed after creation.

        Returns
        -------
        None

        """
        raise TypeError('SparseTable cannot be changed after creation')

    def extend(self, x):
        """
        This method raises a TypeError because SparseTable instances are
        immutable and cannot be changed after creation.

        Parameters
        ----------
        x : Any
            The list with elements to append.

        Raises
        ------
        TypeError
            SparseTable cannot be changed after creation.

        Returns
        -------
        None

        """
        raise TypeError('SparseTable cannot be changed after creation')

    def query_min(self, left, right):
        """
        Query the minimum value within a specified range.

        Parameters
        ----------
        left : int
            The left index of the range (inclusive).

        right : int
            The right index of the range (inclusive).

        Returns
        -------
        float
            The minimum value within the specified range [left, right].

        """
        k = int(math.log2(right - left + 1))
        return min(
            self.table_min[left][k],
            self.table_min[right - (1 << k) + 1][k])

    def query_max(self, left, right):
        """
        Query the maximum value within a specified range.

        Parameters
        ----------
        left : int
            The left index of the range (inclusive).

        right : int
            The right index of the range (inclusive).

        Returns
        -------
        float
            The maximum value within the specified range [left, right].

        """
        k = int(math.log2(right - left + 1))
        return max(
            self.table_max[left][k],
            self.table_max[right - (1 << k) + 1][k])

    def query_sum(self, left, right):
        """
        Query the cumulative sum of values within a specified range.

        Parameters
        ----------
        left : int
            The left index of the range (inclusive).

        right : int
            The right index of the range (inclusive).

        Returns
        -------
        float
            The cumulative sum of values within the specified range
            [left, right].

        """
        total_sum = 0
        k = int(math.log2(right - left + 1))
        for j in range(k, -1, -1):
            if (1 << j) <= (right - left + 1):
                total_sum += self.table_sum[left][j]
                left += 1 << j

        return total_sum
