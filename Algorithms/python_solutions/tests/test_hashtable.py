from Algorithms.python_solutions.hashtable \
    import HashTable_closed, gen_primes, HashTable_open, poly_hash
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


# TODO replace to the separated file with stress tests
# @pytest.mark.skip
def test_stress_ht_closed(ht):
    for i in range(10000):
        ht[chr(i)] = chr(i)
    for i in range(10000):
        assert ht[chr(i)] == chr(i), \
            'ht_open does not stand stress test'
        del ht[chr(i)]
    assert ht.size == 0, \
        'del works wrong'


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


def test_property_pairs_getter(ht_with_samples):
    assert ht_with_samples.pairs is not ht_with_samples.pairs, \
        'check for defensive copying does not pass'


def test_property_pairs_setitem(ht_with_samples):
    with pytest.raises(NotImplementedError):
        ht_with_samples._pairs[19] = 19
        assert ht_with_samples[19] != 19, \
            'ht lets access internal stash when it should not'


def test_property_pairs_setter(ht_with_samples):
    with pytest.raises(NotImplementedError):
        ht_with_samples.pairs = []


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


def test_to_dict_closed(ht_with_samples):
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


def test_getitem_raises_for_absent_element(ht_with_samples):
    with pytest.raises(KeyError):
        print(ht_with_samples[23])


def test_str_and_repr(ht_with_samples):
    assert str(ht_with_samples) == str(ht_with_samples.to_dict()), \
        'str works wrong'
    assert ht_with_samples.__repr__() == str(ht_with_samples), \
        'repr works wrong'


def test_from_dict(ht_with_samples):
    dict1 = {True: 0, 'believe': 1, 32: 18}
    ht = HashTable_closed.from_dict(dict1)
    assert ht == ht_with_samples, \
        'from dict method works wrong'


def test_ht_with_different_hashes():
    hashes = ['poly', 'sha1', 'md5', poly_hash]
    ht_s = list()
    for index, i in enumerate(hashes):
        ht_s.append(HashTable_closed(hashfunc=i))
        ht_s[index][True] = 0
        ht_s[index]['a'] = 1
        ht_s[index][6] = 2
        assert (ht_s[index][True] == 0 and
                ht_s[index]['a'] == 1 and
                ht_s[index][6] == 2), \
            f'ht with chains and {i} hash works wrong'


def test_ht_with_poly_hash_as_callable():
    ht = HashTable_closed(hashfunc=poly_hash)
    ht[True] = 0
    ht['a'] = 1
    ht[6] = 2
    assert (ht[True] == 0 and ht['a'] == 1 and ht[6] == 2), \
        'ht with chains and polynomial hash works wrong'

# HashTable_open


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


@pytest.fixture
def ht_open_with_samples(ht_open):
    ht_open[True] = 0
    ht_open['believe'] = 1
    ht_open[32] = 18
    return ht_open

# TODO replace to the separated file with stress tests


# @pytest.mark.skip
def test_stress_ht_open(ht_open):
    for i in range(1000):
        ht_open[chr(i + 100)] = chr(i + 100)
    assert ht_open.size == 1000, 'size calculates wrong'
    for i in range(1000):
        assert ht_open[chr(i + 100)] == chr(i + 100), \
            'ht_open does not stand stress test'
        del ht_open[chr(i + 100)]
    assert ht_open.size == 0, 'size calculates wrong'


def test_property_elements_defensive_copy(ht_open_with_samples):
    assert ht_open_with_samples.elements is not \
        ht_open_with_samples.elements, \
        'defensive copying for ht open works wrong'


def test_property_elements_setitem(ht_open_with_samples):
    with pytest.raises(Exception):
        ht_open_with_samples._elements[9] = 9
        assert ht_open_with_samples[9] != 9, \
            'ht lets access internal stash when it should not'


def test_set_elements(ht_open_with_samples):
    with pytest.raises(Exception):
        ht_open_with_samples._elements(True, 31)


def test_update_in_ht_open(ht_open_with_samples):
    ht_open_with_samples.update(True, 31)
    assert ht_open_with_samples[True] == 31, \
        'update works wrong'


def test_errors_in_update_and_getitem(ht_open_with_samples):
    with pytest.raises(Exception):
        ht_open_with_samples.update(24, 1)
    with pytest.raises(Exception):
        ht_open_with_samples[18]


def test_search_returns_false_when_no_elements_found(ht_open_with_samples):
    assert ht_open_with_samples.search(18) is False


def test_to_dict_open(ht_open):
    dict_compare = {}
    for i in range(1000):
        dict_compare[chr(i + 100)] = chr(i + 100)
        ht_open[chr(i + 100)] = chr(i + 100)
    dict_with_samples = ht_open.to_dict()
    assert isinstance(dict_with_samples, dict)
    assert dict_with_samples.items() == dict_compare.items()
