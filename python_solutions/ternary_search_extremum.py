import math

def tern_search_min(func, start, end, eps = 1e-6):
    '''
        ternary search for min, if func has many mins
        this search will find only one of them
        so it is better to be used when func
        has only one min between start and end positions

        eps parameter controls accuracy of the
        min search

        works for O(log2(n)), where n is how many
        times can eps fit in abs(r-l)
        for local min determination uses
        absolute values of local func values
    '''
    l = start
    r = end
    while (abs(r-l) >= eps):
        m_l = l + (r - l)/3
        m_r = l + 2*(r - l)/3
        print(m_l, m_r)
        if func(m_r) < func(m_l):
            l = m_l
        else:
            r = m_r
    return (m_l + m_r)/2

def tern_search_max(func, start, end, eps = 1e-6):
    '''
        ternary search for max, if func has many maxes
        this search will find only one of them
        so it is better to be used when func
        has only one max between start and end positions

        eps parameter controls accuracy of the
        max search

        works for O(log2(n)), where n is how many
        times can eps fit in abs(r-l)
        for local max determination uses
        absolute values of local func values
    '''
    l = start
    r = end
    while (abs(r-l) >= eps):
        m_l = l + (r - l)/3
        m_r = l + 2*(r - l)/3
        if func(m_r) > func(m_l):
            l = m_l
        else:
            r = m_r
    return (m_l + m_r)/2
