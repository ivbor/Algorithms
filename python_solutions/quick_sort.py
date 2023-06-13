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
        if a[i] == x:
            a[i], a[m] = a[m], a[i]
            m+=1
    new_r = m
    return new_l, new_r

#the first, pivot = closest to avg
def avg(a, l, r):
    sum = 0
    for i in a[l:r]:
        sum+=i
    return sum/len(a[l:r])

#closest to avg
def clst_avg(a, avg, l, r):
    if len(a[l:r]) == 1:
        return a[l]
    dist = abs(a[l] - avg)
    #print(dist)
    idx = l
    #print(idx)
    for i in range(l,r):
        if abs(a[i]-avg) < dist:
            dist = abs(a[i]-avg)
            #print(dist)
            idx = i
            #print(idx)
    return a[idx]



#l - starting index (0 for initial array)
#r - ending index (len() - 1 for initial array)
def _quick_sort(a, l, r, faster=True):
    """
        Divide them by value relative to x: < x and >= x
        Sort them using recursive func
        Two quicksorts: first is unstable but is claimed to be quick in some cases;
        second is stable and quick but slower than the first
        avg time = o(nlogn)
    """
    #print('a=', a)
    if len(a[l:r]) <= 1:
        return 0
    #print('avg = ',avg(a, l, r))
    if faster:
        x = a[random.randint(l+1, r-1)]
    else:
        x = clst_avg(a, avg(a, l, r), l, r)
    #print('x = ',x)
    new_l, new_r = split(a, x, l, r)
    if (new_l == 0 and new_r == 0):
        return 0
    #print('new_l = ', new_l, ' new_r = ', new_r)
    #if (l == new_l and r == new_r):
    #    raise RecursionError
    _quick_sort(a, l, new_l)
    _quick_sort(a, new_r, r)
    #return a

def quick_sort(a): #o(nlogn)
    _quick_sort(a, l=0, r=len(a))


























