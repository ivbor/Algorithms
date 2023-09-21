def count_sort(array):
    """
        This function implements
        only for whole numbers (or derived from them basic rational)
        with little range
        requires o(n + k) time, where
        where n - size of the array,
        k - difference between lowest and biggest number
    """
    lenght_of_array = len(array)
    min_of_array = min(array)
    max_of_array = max(array)
    array_of_counters = [0 for _ in range(max_of_array + 1 - min_of_array)]
    for i in range(lenght_of_array):
        array_of_counters[array[i] - min_of_array] += 1

    i = 0
    new_array = array.copy()
    for j in range(max_of_array + 1 - min_of_array):
        while (array_of_counters[j] > 0):
            new_array[i] = j + min_of_array
            i += 1
            array_of_counters[j] -= 1
    return new_array
