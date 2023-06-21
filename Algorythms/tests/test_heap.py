from Algorythms.python_solutions.heap import Heap, heap_sort
import random


def test_can_create_heap():
    h = Heap()
    pass


def test_shell_parsing():
    h = Heap(elements=[random.randint(-100, 100) for i in range(40)])
    print(h)
    pass
