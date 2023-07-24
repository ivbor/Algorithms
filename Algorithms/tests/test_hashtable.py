from Algorithms.python_solutions.hashtable \
    import HashTable_closed, gen_primes
import random
import pytest


def test_gen_primes():
    i = 0
    primes = list()
    for i in gen_primes():
        if i < 30:
            primes.append(i)
        else:
            break
    assert primes == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]


def test_hashtable_closed_runs():
    ht = HashTable_closed()
    assert isinstance(ht, HashTable_closed), 'init for hashtable works wrong'
    assert ht.size == 0, \
        'elements of hashtable should be empty from the start'
    assert ht.capacity == 31, \
        'capacity is defined wrong inside init'


@pytest.fixture()
def ht():
    ht = HashTable_closed()
    return ht


def test_setter_in_hashtable_for_the_first_element(ht):
    ht[True] = 0
    assert ht.size == 1, \
        'size calculates wrong after addition of an element'
    assert ht[True] == 0, 'setter or getter work wrong'


def test_setter_in_hashtable_for_the_second_element(ht):
    ht[True] = 0
    ht['unbelievable'] = 1
    assert ht['unbelievable'] == 1, 'second element is unavailable'
    assert ht[True] == 0, 'first element is unavailable'
    assert ht.size == 2, \
        'size calculates wrong after addition of the second element'


def test_ht_handles_collisions(ht):
    for i in range(120):
        ht[1 + 2 * (i + 1)] = random.uniform(-100, 100)
        ht[2 + 2 * (i + 1)] = chr(i)
        assert ht[2 + 2 * (i + 1)] == chr(i)
    assert ht.size == 240, \
        'size calculates wrong when many collisions happen'
    assert ht.capacity == 31, \
        'collisions are handled ineffectively or wrong'


def test_cannot_set_size_and_capacity_for_ht_after_init(ht):
    with pytest.raises(Exception):
        ht.size = 9
    with pytest.raises(Exception):
        ht.capacity = 9
