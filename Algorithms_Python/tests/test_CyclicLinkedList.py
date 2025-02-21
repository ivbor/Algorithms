from Algorithms_Python.CyclicLinkedList import CyclicLinkedList
from Algorithms_Python.DoubleNode import DoubleNode
import pytest


def test_can_make_cll():
    assert isinstance(CyclicLinkedList(), CyclicLinkedList), \
        'cannot initialize cll'


@pytest.fixture()
def cll():
    cll = CyclicLinkedList()
    return cll


@pytest.fixture()
def head():
    head = DoubleNode(12)
    return head


def test_can_initialize_cll_given_head(head):
    cll = CyclicLinkedList(head=head)
    assert cll.head == head, 'cll initializes wrong given head'


def test_initialize_from_chain(head):
    tail = DoubleNode(13)
    head.next_node = tail
    cll = CyclicLinkedList(head=head, tail=tail)
    assert cll.tail.next_node == cll.head, \
        'cyclization of chain never happens'


@pytest.fixture()
def cll_with_node(cll, head):
    cll.head = head
    return cll


def test_insert_in_cll(cll):
    cll.insert(12, 12)
    assert str(cll) == str([12]), 'insert works wrong for cll'
    assert cll.size == 1, 'size for cll after insert calculates wrong'


def test_insert_in_the_head(cll_with_node):
    cll_with_node.insert(0, 10)
    assert cll_with_node.list_all()[0] == 10, \
        'insertion in the head works wrong'
    assert cll_with_node.list_all()[1] == 12, \
        'insertion moves wrong elements'


def test_raises_when_inserting_futher_than_append_goes(cll_with_node):
    with pytest.raises(Exception):
        cll_with_node.insert(2, 0)


def test_update_in_cll(cll_with_node):
    cll_with_node.update(0, None)
    assert cll_with_node.size == 1, \
        'size for cll after update calculates wrong'
    assert str(cll_with_node) == str([None]), 'update works wrong for cll'


def test_erase_in_cll(cll_with_node):
    cll_with_node.erase(0)
    assert str(cll_with_node) == str([]), 'erase works wrong for cll'
    assert cll_with_node.size == 0, 'size calculates wrong after erase in cll'


def test_erase_by_index_not_existing(cll_with_node):
    with pytest.raises(Exception):
        cll_with_node.erase(10)


def test_erase_head(cll_with_node):
    cll_with_node.insert(1, 10)
    cll_with_node.erase(0)
    assert str(cll_with_node) == str([10]), 'erased wrong index'


def test_erase_by_neg_index(cll_with_node):
    cll_with_node.insert(1, 10)
    cll_with_node.erase(-1)
    assert str(cll_with_node) == str([12]), 'erased wrong index`'


def test_erase_tail(cll_with_node):
    cll_with_node.insert(1, 10)
    cll_with_node.erase(cll_with_node.size)
    assert str(cll_with_node) == str([12]), 'erased wrong index`'


def test_raises_when_nothing_to_erase(cll):
    with pytest.raises(Exception):
        cll.erase(0)


def test_insert_for_many_elements(cll):
    for i in range(10):
        cll.insert(i, str(i))
    assert str(cll) == str([str(i) for i in range(10)]), \
        'insert does not work for many elements'
    assert cll.size == 10, 'size is wrong after insertion of many elements'


@pytest.fixture()
def cll_with_many_nodes(cll):
    for i in range(10):
        cll.insert(i, str(i))
    return cll


def test_can_update_many_elements(cll_with_many_nodes):
    for i in enumerate(cll_with_many_nodes):
        if cll_with_many_nodes.size == i[0] - 1:
            break
        cll_with_many_nodes.update(i[0], None)
    assert cll_with_many_nodes.list_all() == [None for _ in range(10)], \
        'update does not work for many elements'


def test_erase_works_for_many_elements(cll_with_many_nodes):
    for i in range(10):
        cll_with_many_nodes.erase(9-i)
    assert str(cll_with_many_nodes) == str([]), \
        'erase did not erased all elements, but should'
    assert cll_with_many_nodes.size == 0, \
        'size is wrong after erasing all elements'


def test_insert_using_neg_index(cll_with_many_nodes):
    cll_with_many_nodes.insert(-2, None)
    assert cll_with_many_nodes.list_all()[-2] is None, \
        'insertion using negative indexes has gone wrong'
