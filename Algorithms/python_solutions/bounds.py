def _lower_bound(array, left_edge, right_edge, value_to_search):
    '''
        This is lower bound search helper.

        Lower bound search works on the cut,
        so edges of the cut inside the array have to be provided.
        Array has to be sorted already, time and complexity equal
        to the binary search with recursion.

        Parameters
        ----------
        array: list[int]
            one-dimensional array consisting of whole numbers
        left_edge: int
            index inside the array meaning left edge of indexes
            inside array (itself included) where search will be performed
        right_edge: int
            index inside the array meaning right edge of indexes
            inside array (itself included) where search will be performed
        value_to_search: int
            value to be searched among the given indexes slice inside array

        Returns
        -------
        int
            index there the lower bound with required value is located
    '''

    # determine the position of the middle element
    middle = int((left_edge + right_edge) / 2)

    # if the length of the array is 1
    # then it is lower_bound of value_to_search
    # and we return it immediately
    if left_edge == right_edge - 1:
        return right_edge

    # if the length of the current cut
    # is more than 1 - it is because
    # there are many values_to_search or they
    # are polluted by non-values_to_search

    # either way we need to clean them up
    # until one element (the leftest
    # among all values_to_search) is left
    if value_to_search <= array[middle]:
        return _lower_bound(array, left_edge, middle, value_to_search)
    else:
        return _lower_bound(array, middle, right_edge, value_to_search)


def lower_bound(array, value_to_search):
    '''
        search for the first encounter
        of the whole value_to_search if it its
        existency is known
    '''
    return _lower_bound(
        array, left_edge=0, right_edge=len(array) - 1,
        value_to_search=value_to_search)


def upper_bound(array, value_to_search):
    '''
        works like lower_bound
        for value_to_search + 1 and subtracts 1
        from calculated index
        giving the last position of value_to_search
    '''
    return _lower_bound(array, left_edge=0, right_edge=len(array) - 1,
                        value_to_search=value_to_search + 1) - 1
