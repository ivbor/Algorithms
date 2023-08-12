from Algorithms.python_solutions.two_dim_array_count_sort \
    import two_dim_array_count_sort


def to_m_based(number, base):
    m_based = []
    whole = number
    remainder = 0
    while whole != 0:
        remainder = whole % base
        whole = whole // base
        m_based.append(remainder)
    m_based = [i for i in reversed(m_based)]
    return m_based


def restore_to_nums(array, base):
    number = 0
    for power, multiplier in enumerate(array):
        number += pow(base, (len(array) - power - 1)) * multiplier
    return number


def digit_sort(array, base=10):
    '''
        for whole numbers (0 <= array[i] < base^k),
        helps with lots of small (meaning power) numbers
    '''
    # extend on negative numbers (- base^k < array[i] < base^k)
    min_of_array = min(array)
    if min_of_array < 0:
        array = [i - min_of_array for i in array]

    # translate any numeration to the m-based
    array = [to_m_based(i, base) for i in array]

    # translate array to 2-dim array, where k is number of digits,
    # add 0 before numbers where less than k digits so that
    # new 2dim list would be rectangular matrix
    max_length_of_a_i = max([len(i) for i in array])
    for i, m_based_number in enumerate(array):
        if len(m_based_number) < max_length_of_a_i:
            m_based_number = [j for j in reversed(m_based_number)]
            while len(m_based_number) < max_length_of_a_i:
                m_based_number.append(0)
            array[i] = [j for j in reversed(m_based_number)]

    # use written above func to sort 2-dim arrays
    array = two_dim_array_count_sort(array)

    # restore numbers from arrays
    array = [restore_to_nums(i, base) for i in array]

    # extend on negative numbers
    if min_of_array < 0:
        array = [i + min_of_array for i in array]

    return array
