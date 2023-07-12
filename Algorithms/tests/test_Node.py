from Algorithms.python_solutions.Node import Node
from Algorithms.python_solutions.DoubleNodes import CyclicLinkedList
import pytest


def test_can_create_blank_node():
    node = Node()
    assert isinstance(node, Node), 'Cannot create blank Node'


@pytest.fixture()
def node():
    node = Node()
    return node


def test_can_assign_data_to_node(node):
    node.data = 4
    assert node.data == 4, 'Cannot assign data to blank node'


def test_can_create_node_with_data():
    node = Node(4)
    assert isinstance(node, Node), 'Cannot create node with data'


@pytest.fixture()
def node_with_data():
    node = Node(4)
    return node


def test_node_can_show_data(node_with_data):
    assert str(node_with_data) == '4', \
        '__str__ method for node is absent or defined wrong'


def test_node_can_store_next_node(node):
    next_node = Node()
    node.next_node = next_node
    assert next(node) == next_node, \
        '__next__ method is absent or defined wrong'


def test_raises_error_when_next_node_is_not_node_or_none(node):
    try:
        next_node = 12
        node.next_node = next_node
        assert False, 'TypeError should be thrown and catched'
    except TypeError:
        pass


def test_raises_error_when_initialized_with_wrong_next_node():
    try:
        next_node = 12
        Node(4, next_node)
        assert False, 'TypeError should be thrown and catched'
    except TypeError:
        pass


def test_eq_for_node(node_with_data):
    node2 = Node(4)
    node3 = node_with_data
    assert not (node_with_data == node2), \
        '__eq__ method is absent or defined wrong'
    assert node3 == node_with_data, \
        '__eq__ method is absent or defined wrong'


def test_repr_in_node(node_with_data):
    assert node_with_data.__repr__() == '4', '__repr__ for node works wrong'


def test_cll():
    cll = CyclicLinkedList()
    # test init, list_all, erase,
    # insert, update
    # use iter in structure
    # for i in self: ... break
    # test insert, list_all,
    # update and erase for 1 element
    assert cll.size == 0
    cll.insert(12, 12)
    assert str(cll) == str([12]), cll.list_all()
    assert cll.size == 1, cll.size
    cll.update(1, None)
    assert cll.size == 1, cll.size
    assert str(cll) == str([None]), cll.list_all()
    cll.erase(1)
    assert str(cll) == str([]), cll.list_all()
    assert cll.size == 0, cll.size
    # test everything for many elements
    for i in range(10):
        cll.insert(i, str(i))
    assert str(cll) == str([str(i) for i in range(10)])
    assert cll.size == 10
    for i in enumerate(cll):
        if i[0] == cll.size:
            break
        cll.update(i[0], None)
    assert cll.list_all() == [None for i in range(10)]
    for i in enumerate(cll):
        if i[0] == 10:
            break
        cll.erase(9-i[0])
    assert cll.size == 0
    assert str(cll) == str([])
