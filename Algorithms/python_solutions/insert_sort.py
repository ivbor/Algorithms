def insert_sort(a):
    """
        For k-th iteration first k elements are sorted
        Search for the place for k+1-th
        We are done after len(a)+1 iterations o(n**2)
    """
    for i in range(len(a)):
        j = i
        while (j > 0 and a[j-1] > a[j]):
            a[j-1], a[j] = a[j], a[j-1]
            j-=1
    return a

