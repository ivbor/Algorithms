import pytest

from Algorithms.python_solutions.hashtable \
    import HashTable_closed, HashTable_open


@pytest.fixture()
def ht():
    ht = HashTable_closed()
    return ht


def test_stress_ht_closed(ht):
    for i in range(10000):
        ht[chr(i)] = chr(i)
    for i in range(10000):
        assert ht[chr(i)] == chr(i), \
            'ht_open does not stand stress test'
        del ht[chr(i)]
    assert ht.size == 0, \
        'del works wrong'


@pytest.fixture()
def ht_open():
    ht = HashTable_open()
    return ht


def test_stress_ht_open(ht_open):
    for i in range(100000):
        ht_open[chr(i + 100)] = chr(i + 100)
    assert ht_open.size == 100000, 'size calculates wrong'
    for i in range(100000):
        assert ht_open[chr(i + 100)] == chr(i + 100), \
            'ht_open does not stand stress test'
        del ht_open[chr(i + 100)]
    assert ht_open.size == 0, 'size calculates wrong'
