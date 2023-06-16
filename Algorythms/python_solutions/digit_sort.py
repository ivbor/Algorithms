from two_dim_array_count_sort import two_dim_array_count_sort

def to_m_based(a, m, array = True):
    m_based = []
    whole = a
    remain = 0
    while whole != 0:
        remain = whole % m
        whole = whole // m
        m_based.append(remain)
    m_based = [i for i in reversed(m_based)]
    if array:
        return m_based
    if not array:
        m_based = restore_to_nums(m_based)
        return m_based

def restore_to_nums(a):
    a_i = 0
    for p, k in enumerate(a):
        a_i += pow(10, (len(a) - p - 1)) * k
    return a_i

# for whole numbers (0 <= a[i] < m^k), helps with lots of small (meaning power) numbers
def digit_sort(a, m = 10):

    # extend on negative numbers (- m^k < a[i] < m^k)
    min_a = min(a)
    if min_a < 0:
        a = [i - min_a for i in a]

    # translate any numeration to the m-based
    a = [to_m_based(i, m) for i in a]

    # translate array to 2-dim array, where k is number of digits,
    # add 0 before numbers where less than k digits
    k = max([len(i) for i in a])
    for i, p in enumerate(a):
        if len(p) < k:
            p = [j for j in reversed(p)]
            while len(p) < k:
                p.append(0)
            a[i] = [j for j in reversed(p)]

    # use written above func to sort 2-dim arrays
    a = two_dim_array_count_sort(a)

    # restore numbers from arrays
    a = [restore_to_nums(i) for i in a]

    # extend on negative numbers
    if min_a < 0:
        a = [i + min_a for i in a]

    return a




