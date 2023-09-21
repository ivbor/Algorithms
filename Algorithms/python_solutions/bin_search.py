def _bin_search(array, left_edge, right_edge, value_to_search):
    '''
        This is the binary search with recursion implementation helper.

        Binary search with recursion works on the cut,
        so edges of the cut inside the array have to be provided.

        Parameters
        ----------
        array: list[int]
            One-dimensional array consisting of whole numbers.
        left_edge: int
            Index inside the array meaning left edge of indexes
            inside array (itself included) where search will be performed.
        right_edge: int
            Index inside the array meaning right edge of indexes
            inside array (itself included) where search will be performed.
        value_to_search: int
            Value to be searched among the given indexes slice inside array.

        Returns
        -------
        bool
            Whether searched value is inside the array
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


def bin_search(array: list[int], value_to_search: int, no_recursion=False):
    '''
        This function performs a binary search inside sorted array
        consisting of whole numbers.
        Time to work: O(log2 of the size of the array) - best case

        Parameters
        ----------
        array: list[int]
            One-dimensional array consisting of whole numbers
        value_to_search: int
            Value to be searched inside the array
        no_recursion: bool
            Since binary search in general has two implementations,
            with or without recursion, this is the switcher between them.
            The no_recursion implementation requires exactly 3 variables
            which makes it very space efficient (O(1) to be exact),
            however time takes damage up to O(size of array).
            The recursion implementation requires space up to O(log2 of
            the size of the array), and time cuts up to the same value.

        Returns
        -------
        bool
            Whether searched value is inside the array
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
