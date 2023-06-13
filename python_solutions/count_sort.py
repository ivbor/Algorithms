def count_sort(a):
    """
        only for whole numbers (or derived from them basic rational) with little range o(n + k),
        where n - size of the array, k - difference between lowest and biggest number
    """
    n = len(a)
    min_a = min(a)
    max_a = max(a)
    cnt = [0 for i in range(max_a+1-min_a)]
    for i in range(n):
        cnt[a[i]-min_a] += 1

    i = 0
    b = a.copy()
    for j in range(max_a+1-min_a):
        while (cnt[j] > 0):
            b[i] = j + min_a
            i += 1
            cnt[j] -= 1
    return b
