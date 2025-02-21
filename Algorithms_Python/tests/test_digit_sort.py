import random
import pytest

from Algorithms_Python.digit_sort \
    import restore_to_nums, to_m_based


@pytest.fixture()
def number():
    number = random.randint(0, 1000000)
    return number


def test_to_m_based_array(number):
    number_string = ''
    for i in to_m_based(number, 6):
        number_string += str(i)
    assert int(str(number_string), base=6) == number, \
        'translation number to new base works wrong'


def test_restore_to_nums(number):
    assert restore_to_nums(to_m_based(number, base=6), 6) == number, \
        'restore to nums works wrong'
