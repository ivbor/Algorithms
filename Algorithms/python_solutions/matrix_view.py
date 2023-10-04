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

    def __repr__(self, indexes=False) -> None:
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

        # sizes: n for rows, m for columns
        n = len(array)
        m = max([len(array) for _ in array])

        # printing indexes of columns
        if indexes:
            for i in range(m + 1):
                if i == 0:
                    print(f'{i: 5.0f}', end=' ')
                print(f'{i: 5.0f}', end=' ')
            print('\n', end='')

        # printing matrix
        for i in range(n):
            for j in range(m + 1):
                if indexes:
                    if j == 0:
                        print(f'{i: 5.0f}', end=' ')
                if j < len(array[i]):
                    print(f'{array[i][j]: 5.0f}', end=' ')
            print('\n', end='')
        print('\n', end='')
