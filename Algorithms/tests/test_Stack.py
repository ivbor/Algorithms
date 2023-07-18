from Algorithms.python_solutions.Stack import Stack
import pytest


def test_can_make_stack():
    Stack()


@pytest.fixture()
def st():
    st = Stack()
    return st


def test_can_push_to_stack(st):
    st.push(None)
    assert st.size == 1, 'push method works wrong'


def test_can_access_stack_back(st):
    st.push(None)
    st.push('None')
    assert st.back() == 'None', 'back method works wrong'


def test_can_access_stack_front(st):
    assert st.front() is None, 'front method works wrong'


@pytest.fixture()
def st_with_3_elements():
    st = Stack()
    st.push(4)
    st.push([])
    st.push('None')
    return st


def test_can_pop_from_stack(st_with_3_elements):
    assert st_with_3_elements.pop() == 'None', 'pop method works wrong'
    assert isinstance(st_with_3_elements.back(), list), \
        'pop method does not invoke changes in back method'


def test_pop_until_one_element_left(st_with_3_elements):
    while len(st_with_3_elements) != 1:
        st_with_3_elements.pop()
    assert st_with_3_elements.front() == st_with_3_elements.back(), \
        'front is not equal back when one element left but should'


def test_pop_last_element(st_with_3_elements):
    for _ in range(3):
        st_with_3_elements.pop()
    assert len(st_with_3_elements) == 0, \
        'popping the last element does not lead to empty stack'
