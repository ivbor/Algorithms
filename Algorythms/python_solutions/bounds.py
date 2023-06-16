# helper function for recursive
# lower_bound

def _lower_bound(a, l, r, x):
    '''
        function-helper
        since lower_bound works on the cut
        we use recursion with cutting
        the previous cut by 2
        l parameter for left edge
        r for right accordingly
    '''

    # determine the position of the middle element
    m = int((l+r)/2)

    # if the length of the array is 1
    # then it is lower_bound of x
    # and we return it immediately
    if l == r - 1:
        return r

    # if the length of the current cut
    # is more than 1 - it is because
    # there are many x values or they
    # are polluted by non-x's

    # either way we need to clean them up
    # until one element (the leftest
    # among all x values) is left
    if x <= a[m]:
        return _lower_bound(a, l, m, x)
    else:
        return _lower_bound(a, m, r, x)

def lower_bound(a, x):
    '''
        search for the first encounter
        of the whole number x if it its
        existency is known
    '''
    return _lower_bound(a, 0, len(a)-1, x)

def upper_bound(a, x):
    '''
        works like lower_bound
        for x + 1 and subtracts 1
        from calculated index
        giving the last position of x
    '''
    return _lower_bound(a, 0, len(a)-1, x + 1) - 1
