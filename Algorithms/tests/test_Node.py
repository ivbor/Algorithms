from Algorithms.python_solutions.Node import Node
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
    with pytest.raises(Exception):
        next_node = 12
        Node(4, next_node)


def test_eq_for_node(node_with_data):
    node2 = Node(4)
    node3 = node_with_data
    assert not (node_with_data == node2), \
        '__eq__ method is absent or defined wrong'
    assert node3 == node_with_data, \
        '__eq__ method is absent or defined wrong'


def test_repr_in_node(node_with_data):
    assert node_with_data.__repr__() == '4', '__repr__ for node works wrong'
