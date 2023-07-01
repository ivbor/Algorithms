from Algorithms.python_solutions.Lesson5 import HashTable
import pytest
import random


@pytest.mark.skip
def test_hashtable():
    ht = HashTable()
    assert ht is not None
    assert (ht.size == 0 and ht.capacity == 31)
    ht[True] = 0
    assert ht.size == 1
    ht['unbelievable'] = 1
    assert ht['unbelievable'] == 1
    assert ht[True] == 0
    assert ht.size == 2
    for i in range(30):
        ht.append(random.uniform(-100, 100))
        ht.append(chr(i))
        assert ht[2 + 2 * (i + 1)] == chr(i)
    assert ht.capacity == 67
    assert ht[True] == 0
    assert ht['unbelievable'] == 1
    print(ht.elements)

