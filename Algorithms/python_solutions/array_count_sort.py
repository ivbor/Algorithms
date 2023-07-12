def array_count_sort(array, key=0, position=False):
    """
        for 2-dim arrays, consisting of whole numbers
        algo sorts 1-dim arrays inside 2-dim array

        key is always int and shows by which index to sort

        time to work - O(n) or O(k) - depends on what's bigger
        n - array length,
        k - difference between biggest and lowest value
    """

    # in order to do that let's first introduce
    # dim's sizes
    len_of_array = len(array)

    # let's find min and max among the values with index == key
    # where len of row is not enough - change value to 0
    array_i_key = [0
                   if len(array[i]) <= key else array[i][key]
                   for i in range(len_of_array)]
    min_array_key = min(array_i_key)
    max_array_key = max(array_i_key)

    # all empty places will be filled
    # with values < min_a in order to
    # place them to the top
    array_i_key = [min_array_key - 1
                   if len(array[i]) <= key else array[i][key]
                   for i in range(len_of_array)]

    # create function value-min_a -> index
    # +2 means +1 for counting first entry
    # and another +1 for putting rows with
    # absent positions above others
    count_first_entry = 1
    rows_with_absent_key_position = 1
    indexes = [
        []
        for _ in range(
            max_array_key - min_array_key + count_first_entry +
            rows_with_absent_key_position)]
    for i in range(len_of_array):
        indexes[array_i_key[i] - min_array_key + 1].append(i)

    # for optimization purposes
    # when n > max-min next operation
    # uses O(max-min) instead of O(n)
    if len_of_array > (max_array_key - min_array_key):
        for i in reversed(range(len(indexes))):
            if len(indexes[i]) == 0:
                del indexes[i]
                i += 1

    # calculate new index for each row
    positions = []
    for i in range(len(indexes)):
        positions.extend(indexes[i])

    new_array = [array[i] for i in positions]

    # return positions of distinct
    # elements for future multiple
    # index sort
    if position:
        return new_array, indexes

    return new_array
