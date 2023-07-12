def insert_sort(array):
    """
        For k-th iteration first k elements are sorted
        Search for the place for k+1-th
        We are done after len(a)+1 iterations o(n**2)
    """
    for i in range(len(array)):
        k = i
        while (k > 0 and array[k - 1] > array[k]):
            array[k - 1], array[k] = array[k], array[k - 1]
            k -= 1
    return array
