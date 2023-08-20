from Algorithms.python_solutions.hashtable \
    import HashTable_closed, gen_primes, HashTable_open
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


def test_stress_ht_closed(ht):
    for i in range(100000):
        ht[chr(i)] = chr(i)
    for i in range(100000):
        assert ht[chr(i)] == chr(i), \
            'ht_open does not stand stress test'


def test_cannot_set_size_and_capacity_for_ht_after_init(ht):
    with pytest.raises(Exception):
        ht.size = 9
    with pytest.raises(Exception):
        ht.capacity = 9


@pytest.fixture()
def ht_with_samples(ht):
    ht[True] = 0
    ht['believe'] = 1
    ht[32] = 18
    return ht


def test_deletion_in_ht(ht_with_samples):
    del ht_with_samples[32]
    del ht_with_samples[0]
    assert ht_with_samples.size == 2, 'deletion works wrong'
    assert ht_with_samples[True] == 0, 'first element was lost during deletion'
    assert ht_with_samples['believe'] == 1, \
        'second element was lost during deletion'


def test_update_in_ht(ht_with_samples):
    ht_with_samples[32] = 2
    assert ht_with_samples[32] == 2, 'update works wrong'
    assert ht_with_samples.size == 3, 'update damages size'
    assert (ht_with_samples[True] == 0 and ht_with_samples['believe'] ==
            1), 'update damages other ht elements'


def test_to_dict(ht_with_samples):
    dict_from_ht = ht_with_samples.to_dict()
    assert len(dict_from_ht) == len(
        ht_with_samples), 'size of dict from ht is wrong'
    assert (dict_from_ht[True] == 0 and
            dict_from_ht[32] == 18 and
            dict_from_ht['believe'] == 1), \
        'transformation to dict does not save elements'


def test_search_in_ht(ht_with_samples):
    assert isinstance(ht_with_samples.search(True), int), \
        'search in ht considers absent actually present elements'
    assert ht_with_samples.search(18) is False, \
        'search in ht considers present actually absent elements'


def test_contains_in_ht(ht_with_samples):
    assert (True in ht_with_samples) is True, \
        'ht considers absent actually present elements'
    assert (18 in ht_with_samples) is False, \
        'ht considers present actually absent elements'


def test_from_dict(ht_with_samples):
    dict1 = {True: 0, 'believe': 1, 32: 18}
    ht = HashTable_closed.from_dict(dict1)
    assert ht == ht_with_samples, \
        'from dict method works wrong'


def test_can_create_ht_open():
    ht = HashTable_open()
    assert isinstance(ht, HashTable_open)


@pytest.fixture()
def ht_open():
    ht = HashTable_open()
    return ht


def test_setitem_and_getitem_in_ht(ht_open):
    ht_open[True] = 0
    ht_open['believe'] = 1
    ht_open[32] = 18
    assert (ht_open[True] == 0 and ht_open['believe'] == 1
            and ht_open[32] == 18), \
        'setitem or getitem work wrong'


# TODO replace to the separated file with stress tests
def test_stress_ht_open(ht_open):
    for i in range(10000):
        ht_open[chr(i)] = chr(i)
    for i in range(10000):
        assert ht_open[chr(i)] == chr(i), \
            'ht_open does not stand stress test'
    assert ht_open.size == 10000, 'size calculates wrong'
