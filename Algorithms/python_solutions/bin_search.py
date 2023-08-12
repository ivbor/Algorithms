def _bin_search(array, left_edge, right_edge, value_to_search):
    '''
        function-helper
        since bin_search works on the cut
        we use recursion with cutting
        the previous cut by 2
        l parameter for left edge
        r for right accordingly
    '''

    # once the cut has the length of 1
    # we require the search to give the answer
    if left_edge == right_edge - 1:
        return (array[left_edge] == value_to_search)

    # if the length != 1 yet - calculate
    # the middle of the cut for future
    # cut by half
    middle = int((left_edge + right_edge)/2)

    # if the middle of the cut
    # equals the searched value -
    # there is no point in going further
    # and we can give the answer
    # immediately
    if value_to_search == array[middle]:
        return True

    # if the searched value has not yet
    # been reached and current cut does not
    # have length == 1 - we can safely
    # cut from further by half

    # if value_to_search < array[middle] =>
    # array[left_edge] < value_to_search < array[middle]
    # if value_to_search is in array, of course
    if value_to_search < array[middle]:
        return _bin_search(array, left_edge, middle, value_to_search)

    # otherwise => array[middle] < value_to_search < array[right_edge]
    else:
        return _bin_search(array, middle, right_edge, value_to_search)


def bin_search(array, value_to_search, no_recursion=False):
    '''
        this is binary search function
        works only for already sorted arrays
        consisting of only whole numbers
        for log2(n) time

        there are 2 options available -
        with recursion or without
        switch is made by changing
        no_recursion option
    '''

    # this is no recursion realization
    if no_recursion:

        # introduce left and right edge values
        # make them slightly over real edges
        # so that while will not freak out
        left_edge = 0
        right_edge = len(array) - 1
        while left_edge < right_edge:

            # calculate the middle point
            middle = int((left_edge + right_edge) / 2)

            # just as in helper function
            # for recursion option
            # move the edges according
            # to presumable place of value_to_search in array
            if value_to_search <= array[middle]:
                right_edge = middle
            else:
                left_edge = middle

            # not to forget to make an exit point
            # for value not found situation
            if left_edge + 1 == right_edge:
                break

        # we can return either position
        # or boolean, if value_to_search is in array
        return (value_to_search == array[right_edge] or
                value_to_search == array[left_edge])

    # here is the launch of helper function
    # which is needed because bin_search
    # is a search in cut, not in array
    else:
        return _bin_search(
            array, left_edge=0, right_edge=len(array),
            value_to_search=value_to_search)
