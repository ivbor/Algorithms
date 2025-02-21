from Algorithms_Python.Deque import Deque
import pytest


def test_can_make_deck():
    Deque()


@pytest.fixture()
def d():
    d = Deque()
    return d


def test_push_front_works_for_deque(d):
    assert d.size == 0, 'size is initialized incorrectly'
    d.push_front(None)
    assert d.size == 1, 'size has not charged after push_front method'
    assert d.front() is None, 'element was not added by push_front'


def test_push_back_works_for_deque(d):
    d.push_back(4)
    d.push_front([None, 'None', 4, []])
    d.push_back('None')
    assert isinstance(d.front(), list), \
        'wrong element is on the front of deque'


def test_pop_front_works_for_deque(d):
    d.push_front(None)
    d.push_front(4)
    d.pop_front()
    assert d.front() is None, 'wrong element popped'


def test_pop_back_works_for_deque(d):
    d.push_back('4')
    d.push_back('None')
    d.pop_back()
    assert d.back() == '4', 'wrong element popped'
