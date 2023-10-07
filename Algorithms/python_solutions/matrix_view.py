"""
Matrix2dim Module
======================

A module for creating and displaying 2-Dimensional matrices.

This module contains the `Matrix2dim` class, which provides a convenient way
to create and display 2-Dimensional matrices.

Classes
-------
Matrix2dim
    A class for creating and displaying 2-Dimensional matrices.

"""


class Matrix2dim:
    """
    2-Dimensional Matrix Class

    The Matrix2dim class provides beautiful print method
    for 2-Dimensional lists.

    Attributes
    ----------
    data: list of lists
        A list of lists representing the 2D matrix.

    Methods
    -------
    __init__(self, data) -> None
        Initializes a Matrix2dim object with the provided data.

    __repr__(self, indexes=False) -> None
        Returns a string representation of the matrix.

    """

    def __init__(self, data) -> None:
        """
        Initialize a Matrix2dim object.

        Parameters
        ----------
        data: list of lists
            A list of lists representing the 2D matrix.

        Returns
        -------
        None

        """
        if isinstance(data, list) and len(data) > 0:
            if isinstance(data[0], list):
                self.data = data

    def __repr__(self, indexes=False) -> str:
        """
        Return a string representation of the 2D matrix.

        Parameters
        ----------
        indexes : bool, optional
            If True, include row and column indexes in the representation.
            Default is False.

        Returns
        -------
        None

        """
        array = self.data

        # this str will be returned
        res = ''

        # sizes: n for rows, m for columns
        n = len(array)
        m = max([len(array) for _ in array])

        # printing indexes of columns
        if indexes:
            for i in range(m + 1):
                if i == 0:
                    res += f'{i: 5.0f} '
                res += f'{i: 5.0f} '
            res += '\n'

        # printing matrix
        for i in range(n):
            for j in range(m + 1):
                if indexes:
                    if j == 0:
                        res += f'{i: 5.0f} '
                if j < len(array[i]):
                    res += f'{array[i][j]: 5.0f} '
            res += '\n\n'
        res += '\n'

        return res
