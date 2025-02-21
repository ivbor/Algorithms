import random
import logging
import pytest

from Algorithms_Python.heap import Heap, heap_sort


def test_can_create_heap():
    h = Heap(elements=[random.uniform(-100, 100) for _ in range(40)])
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
    for _ in range(h.size):
        min_h = min(h)
        assert h.remove_min() == min_h
    assert h.size == 0
    with pytest.raises(Exception):
        h.remove_min()


def test_boundary_cases():
    h = Heap()
    h.insert(-30.13)
    assert h.size == 1
    assert h.height() == 1
    assert h.get_children(0) is None
    h.erase()
    assert h.size == 0
    assert h.height() == 0
    for _ in range(100):
        h.insert(random.uniform(-100, 100))
    assert h.height() == 7
    assert h.size == 100
    for _ in range(100):
        h.append(random.uniform(-100, 100))
    assert h.size == 200


def test_heap_sort():
    h = [random.uniform(-100, 100) for _ in range(100)]
    developed = heap_sort(h)
    built_in = sorted(h)

    assert developed == built_in


def test_repr():
    h = Heap(elements=[random.uniform(-100, 100) for _ in range(40)])
    logging.info(h)
