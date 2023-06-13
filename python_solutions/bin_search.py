def _bin_search(a, l, r, x):
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
    if l == r - 1:
        return (a[l] == x)

    # if the length != 1 yet - calculate
    # the middle of the cut for future
    # cut by half
    m = int((l + r)/2)

    # if the middle of the cut
    # equals the searched value -
    # there is no point in going further
    # and we can give the answer
    # immediately
    if x == a[m]:
        return True

    # if the searched value has not yet
    # been reached and current cut does not
    # have length == 1 - we can safely
    # cut from further by half

    # if x < a[m] => a[l] < x < a[m]
    # if x is in array, of course
    if x < a[m]:
        return _bin_search(a, l, m, x)

    # otherwise => a[m] < x < a[r]
    else:
        return _bin_search(a, m, r, x)

def bin_search(a, x, no_rec = False):
    '''
        this is binary search function
        works only for already sorted arrays
        consisting of only whole numbers
        for log2(n) time

        there are 2 options available -
        with recursion or without
        switch is made by changing
        no_rec option
    '''

    # this is no recursion realization
    if no_rec:

        # introduce left and right edge values
        # make them slightly over real edges
        # so that while will not freak out
        l = -1
        r = len(a)
        while l < r-1:

            # calculate the middle point
            m = int((l+r)/2)

            # just as in helper function
            # for recursion option
            # move the edges according
            # to presumable place of x in a
            if x <= a[m]:
                r = m
            else:
                l = m

        # we can return either position
        # or boolean, if x is in a
        return x == a[r]

    # here is the launch of helper function
    # which is needed because bin_search
    # is a search in cut, not in array
    else:
        return _bin_search(a, 0, len(a), x)
