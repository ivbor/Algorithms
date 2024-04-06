from Algorithms.python_solutions.Queue import Queue
import pytest


def test_can_make_queue():
    Queue()


@pytest.fixture()
def q():
    q = Queue()
    return q


def test_can_push_into_queue(q):
    q.push(None)
    assert q.size == 1, 'push works wrong in queue'


def test_front_in_queue_works(q):
    assert q.front() is None, 'front works wrong in queue'


@pytest.fixture()
def q_with_4_elements():
    q = Queue()
    q.push(None)
    q.push(4)
    q.push([None, 'None', 4, []])
    q.push('None')
    return q


def test_can_pop_from_queue(q_with_4_elements):
    assert q_with_4_elements.pop() is None, 'pop method works wrong in queue'
    assert q_with_4_elements.front() == 4, 'pop method invokes wrong changes'


def test_pop_until_one_element_left(q_with_4_elements):
    while len(q_with_4_elements) != 1:
        q_with_4_elements.pop()
    assert q_with_4_elements.front() == q_with_4_elements.back(), \
        'front is not equal back when one element is left'
    assert q_with_4_elements.front() == 'None', \
        'pop pops elements in wrong order'


def test_pop_last_element(q):
    q.push(None)
    q.pop()
    assert len(q) == 0, 'popping the last element does not lead to \
        empty queue'
