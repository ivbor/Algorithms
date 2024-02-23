"""
HyperLogLog Module

This module implements the HyperLogLog algorithm for approximate cardinality
estimation of large data sets.

Classes
-------
HyperLogLog
    A class implementing the HyperLogLog algorithm.

"""

import math
import hashlib
import array


class HyperLogLog:
    """
    HyperLogLog Algorithm Implementation

    This class provides methods to estimate the cardinality of a
    large data set using the HyperLogLog algorithm.

    Attributes
    ----------
    precision : int, optional
        The precision parameter for the algorithm. This parameter corresponds
        to the amount of binary registers where the numbers will be written
        to. The higher the precision - the thinner bins for probability
        distribution for the algorithm. Default is 14.

    Methods
    -------
    __init__(self, precision=14) -> None
        Initialize HyperLogLog structure.

    _hash(self, element: str) -> str
        Hash the element using SHA256.

    _leading_zeros(self, binary_string: str) -> int
        Count the number of leading zeros in a binary string.

    add(self, element: str) -> None
        Add an element to the HyperLogLog data structure.

    count(self) -> int
        Estimate the cardinality of the data set.

    """

    def __init__(self, precision=14) -> None:
        """
        Initialize a HyperLogLog object with a given precision.

        Parameters
        ----------
        precision : int, optional
            The precision parameter for the algorithm. Default is 14.

        Returns
        -------
        None

        """

        self.precision = precision
        self.num_buckets = 2 ** precision
        self.buckets = array.array('H', [0] * self.num_buckets)

    def _hash(self, element) -> str:
        """
        Hash the element using SHA256.

        Parameters
        ----------
        element : str
            The element to be hashed.

        Returns
        -------
        str
            The binary hash value of the element.

        """

        hash_value = int(
            hashlib.sha256(element.encode()).hexdigest(), 16)
        return bin(hash_value & ((1 << 64) - 1))[2:]

    def _leading_zeros(self, binary_string) -> int:
        """
        Count the number of leading zeros in a binary string.

        Parameters
        ----------
        binary_string : str
            The binary string.

        Returns
        -------
        int
            The number of leading zeros.

        """

        count = 0
        binary_value = int(binary_string, 2)
        while binary_value:
            binary_value >>= 1
            count += 1
        return count

    def add(self, element) -> None:
        """
        Add an element to the HyperLogLog data structure.

        Parameters
        ----------
        element : str
            The element to be added.

        Returns
        -------
        None

        """

        hash_value = self._hash(element)
        index = int(hash_value[-self.precision:], 2)
        leading_zeros = self._leading_zeros(hash_value)
        self.buckets[index] = max(self.buckets[index], leading_zeros + 1)

    def count(self) -> int:
        """
        Estimate the cardinality of the data set.

        Returns
        -------
        int
            The estimated cardinality of the data set.

        """

        alpha = 0.7213 / (1 + 1.079 / self.num_buckets)
        estimate = alpha * (self.num_buckets ** 2) / sum(
            2 ** -bucket for bucket in self.buckets)
        if estimate <= 2.5 * self.num_buckets:
            # Small range correction
            zeros = self.buckets.count(0)
            if zeros != 0:
                return round(self.num_buckets * math.log(
                    self.num_buckets / zeros))
            else:
                return round(estimate)
        elif estimate > 2 ** 32 / 30:
            # Large range correction
            return round(-(2 ** 32) * math.log(1 - estimate / (2 ** 32)))
        else:
            # No correction needed
            return round(estimate)
