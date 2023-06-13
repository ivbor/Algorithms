import random

def split(a, x, l, r):
    m = l
    for i in range(l, r):
        if a[i] < x:
            a[i], a[m] = a[m], a[i]
            m+=1
    new_l = m
    if m == len(a):
        return 0,0
    for i in range(new_l, r):
        if abs(a[i] - x) <= 10**-14 :
            a[i], a[m] = a[m], a[i]
            m+=1
    new_r = m
    return new_l, new_r

def _split_find(a, l, r, k):
    x = a[random.randint(l, r-1)]
    m, n = split(a, x, l, r)
    if len(a[l:r]) <= abs(m-n):
        return a[k]
    if k < m:
        return _split_find(a, l, m, k)
    else:
        return _split_find(a, m, r, k)

def split_find(a, *args):
    """
        search for k-th element by increase without sort in any array o(nlogn) -> o(n) if sorted
    """
    for k in args:
        return _split_find(a, 0, len(a), k)
