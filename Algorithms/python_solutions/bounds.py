# helper function for recursive
# lower_bound

def _lower_bound(array, left_edge, right_edge, value_to_search):
    '''
        function-helper
        since lower_bound works on the cut
        we use recursion with cutting
        the previous cut by 2
        l parameter for left edge
        r for right accordingly
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
