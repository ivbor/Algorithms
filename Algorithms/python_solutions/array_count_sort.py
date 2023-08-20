def array_count_sort(array: list[list[int]], key=0, position=False):
    """
        This function performs counting sort on the 2-dimensional array
        of whole numbers.

        This algorithm uses count sort to sort rows inside matrix
        by ascending order. It works only with integer numbers,
        so if your matrix contains floats - do not use this algorithm.
        Time to work: O(number of rows in the array) or
        O(difference between the biggest and the lowest value
        in the key index) depending on what is more.

        Parameters
        ----------
        array: list[list[int]]
            2-dimensional array which will be sorted
        key: int
            shows by which index to sort, works even in situations
            when there are blank spaces with this index in the rows
            In this case puts those rows higher than those with
            filled spaces
            default value: 0
        position: bool
            tells function whether to return positions information
            among the sorted array
            this is handy if there are elements with the same value
            and you want to sort them further by other keys or indexes

            positions information is the list telling what rows of the array
            (by the indexes in the form of the numbers inside lists)
            where to put in order to create a sorted array
            (by the indexes of the lists containing numbers)
            default value: False

        Returns
        -------
        list[list[int]]
            sorted array
        optional: list[list[int|BLANK]]
            positions array which looks like this:
            [[53, 46, 18], [12], [36], [11, 34], ...]
            which means that
            53, 46 and 18 rows have the same lowest value among all rows
            so they should be placed first in the sorted array (meaning
            new indexes 0, 1 and 2) in any preferable order
            blank lists mean the absence of rows with some value
            in the key index
            and so on

            return is modified by parameter position
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
    # place strings with them higher than
    # those without empty places
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
