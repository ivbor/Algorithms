def merge(a, b):
    """
        Divide and conquer
        Divide on 2 parts
        Sort them using recursive func
        Merge them into one
        o(nlogn)
    """
    n = len(a)
    m = len(b)
    i = 0
    j = 0
    c = [0 for i in range(len(a) + len(b))]
    while (i + j < n + m): #end for both is not reached
        if (j==m or (i < n and a[i] < b[j])): #end for the second is reached or (end for the first is not reached and i-th element from the first less than j-th element from the second)
            c[i+j] = a[i] # add to c an element from the first
            #print('c[i+j]=',c[i+j])
            #print('i+j=',i+j)
            i+=1 # continue movement on the first
        else: # end for the first is reached but not for the second
            c[i+j] = b[j] # add to c an element from the second
            #print('c[i+j]=',c[i+j])
            #print('i+j=',i+j)
            j+=1 # continue movement on the second
    del a
    del b
    return c


def _merge_sort(a):
    n = len(a)
    #print(n)
    if (n == 1):
        return a
    #if (n == 0):
    #    raise RecursionError
    l = a[:round(n/2)]
    #print('l=',l)
    r = a[round(n/2):n]
    #print('r=',r)
    l = _merge_sort(l)
    r = _merge_sort(r)
    return merge(l, r)

def merge_sort(a):
    return _merge_sort(a)
