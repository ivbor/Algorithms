from Algorithms.python_solutions.heap import Heap, heap_sort
import random
import time


def test_can_create_heap():
    h = Heap(elements=[random.uniform(-100, 100) for i in range(40)])
    # check if sift up inside insert works correctly
    for i in range(h.size):
        children = h.get_children(i)
        if children is not None:
            if isinstance(children, tuple):
                for j in children:
                    assert h[i] <= j
            else:
                assert h[i] <= children
    assert h.height() == 6
    for i in range(h.size):
        min_h = min(h)
        assert h.remove_min() == min_h
    assert h.size == 0

    # tests for boundary cases
    h = Heap()
    h.insert(-30.13)
    assert h.size == 1
    assert h.height() == 1
    assert h.get_children(0) is None
    h.erase()
    assert h.size == 0
    assert h.height() == 0
    for i in range(100):
        h.insert(random.uniform(-100, 100))
    assert h.height() == 7
    assert h.size == 100


def test_heap_sort():
    h = [random.uniform(-100, 100) for i in range(100)]
    st = time.time()
    developed = heap_sort(h)
    et = time.time()
    developed_time = et - st

    st = time.time()
    built_in = sorted(h)
    et = time.time()
    built_in_time = et - st

    assert developed == built_in
    print(f'heap_sort: {developed_time:.10f},\
            sorted: {built_in_time:.10f}')


def test_repr():
    h = Heap(elements=[random.uniform(-100, 100) for i in range(40)])
    print(h)
    pass