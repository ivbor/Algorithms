import math

def real_bin_search(func, y, l, r, eps = 1e-6):
    '''
        basic binary search among real
        numbers for x where func(x) = y
        works only for monotonic functions
        in O(log2(n)) time where n is how
        many eps will fit in abs(r-l)
        r - right edge of search interval
        l - left one accordingly
    '''

    # this algo requires O(log2(n))
    # operations where n is the amount of
    # the smallest cuts we consider (epsilons)
    # that can fit in abs(r-l)

    # determine whether function is
    # ascending or descending

    # l+eps and r-eps we use
    # so that search can work
    # even if function does not
    # exist in l or r
    asc = (func(l+eps) < func(r-eps))

    # we can use while to ensure accuracy
    # is no less than eps
    while (abs(r-l) >= eps):

        # find the middle of the cut
        m = (l + r)/2

        if asc:

            # if function is ascending
            # and function is less than y
            # this means y is somewhere
            # in bigger x's (righer)
            # so move left border of the
            # current cut to the middle
            if func(m) < y:
                l = m

            # if ascending and function
            # is more than y - this means
            # y is lesser x's (lefter)
            # so move right border of the
            # current cut to the middle
            else:
                r = m

        # for descending - everything
        # works accordingly with the
        # change of sign in if clause
        else:
            if func(m) > y:
                l = m
            else:
                r = m

    # for even more accuracy
    # as an answer give the middle
    # of the accurate enough cut
    return (l + r)/2
