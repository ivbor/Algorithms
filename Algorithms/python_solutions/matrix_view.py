class Matrix2dim:

    def __init__(self, data) -> None:
        if type(data) == list and len(data) > 0:
            if type(data[0]) == list:
                self.data = data

    def __repr__(self, indexes=False) -> None:
        """
            Print() function for 2dim matrix
            [[],[],...,[]]
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
