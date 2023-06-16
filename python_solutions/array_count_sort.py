def array_count_sort(a, key=0, position=False):
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
    n = len(a)

    # let's find min and max among the values with index == key
    # where len of row is not enough - change value to 0
    a_i_key_s = [0 if len(a[i]) <= key else a[i][key] for i in range(n)]
    min_a = min(a_i_key_s)
    max_a = max(a_i_key_s)

    # all empty places will be filled
    # with values < min_a in order to
    # place them to the top
    a_i_key_s = [min_a-1 if len(a[i]) <= key else a[i][key] for i in range(n)]

    # create function value-min_a -> index
    # +2 means +1 for counting first entry
    # and another +1 for putting rows with
    # absent positions above others
    indexes = [[] for i in range(max_a-min_a+2)]
    for i in range(n):
        indexes[a_i_key_s[i]-min_a+1].append(i)

    # for optimization purposes
    # when n > max-min next operation
    # uses O(max-min) instead of O(n)
    if n > (max_a - min_a):
        for i in reversed(range(len(indexes))):
            if len(indexes[i]) == 0:
                del indexes[i]
                i += 1

    # calculate new index for each row
    p = []
    for i in range(len(indexes)):
        p.extend(indexes[i])

    new_a = [a[i] for i in p]

    # return positions of distinct
    # elements for future multiple
    # index sort
    if position:
        return new_a, indexes

    return new_a
