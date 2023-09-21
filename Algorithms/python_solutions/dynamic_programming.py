# Dynamic programming (backpack problem) from Lesson 6: O(n*W) instead of
# 2^n on low W
# Maybe add there PTAS agos solving some other tasks
# Consider writing algo in the most abstract way possible
# For future reusage
# Maybe to write it as a generator (lazy algo)
# However we do not really need intermediate solutions
# so there is no need to store them or to even look at them
# if we need generator - to only get to the answer and collect it

from typing import Iterable


def dimensions(x):
    result = 1
    while isinstance(x, Iterable):
        x = x[0]
        result += 1
    return result


def DP_solution(start, movement, stop):
    storage = start
    stop = stop
    for _ in range(dimensions(start)):
        storage = list(storage)
    move = movement
    while len(storage) < stop:
        storage = move(storage)
    return storage[stop - 1]


def movement(a, i):
    try:
        return a[i - 1] + a[i - 2]
    except BaseException:
        return a[i - 1]


grig = DP_solution(start=1, movement=movement, stop=10)
