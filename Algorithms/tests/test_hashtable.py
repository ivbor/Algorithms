from Algorithms.python_solutions.hashtable import HashTable, gen_primes
import random


def test_gen_primes():
    i = 0
    primes = list()
    for i in gen_primes():
        if i < 30:
            primes.append(i)
        else:
            break
    assert primes == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]


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
        ht[1 + 2 * (i + 1)] = random.uniform(-100, 100)
        ht[2 + 2 * (i + 1)] = chr(i)
        assert ht[2 + 2 * (i + 1)] == chr(i)
    assert ht.capacity == 67
    ht._pairs = [1, 2, 3, 4]
    for i in ht._pairs:
        assert not isinstance(i, int)
    #assert ht[True] == 0
    #assert ht['unbelievable'] == 1
    # print(ht.elements)
