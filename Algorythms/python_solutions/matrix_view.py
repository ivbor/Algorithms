def matrix_view_2dim(a: list, indexes = False) -> None:
    """
        Print() function for 2dim matrix
        [[],[],...,[]]
    """

    # sizes: n for rows, m for columns
    n = len(a)
    m = max([len(i) for i in a])

    # printing indexes of columns
    if indexes:
        for i in range(m+1):
            if i == 0:
                print(f'{i: 5.0f}', end = ' ')
            print(f'{i: 5.0f}', end = ' ')
        print('\n', end='')

    # printing
    for i in range(n):
        for j in range(m+1):
            if indexes:
                if j == 0:
                    print(f'{i: 5.0f}', end = ' ')
            if j < len(a[i]):
                print(f'{a[i][j]: 5.0f}', end = ' ')
        print('\n', end='')
    print('\n', end='')
