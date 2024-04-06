from Algorithms.python_solutions.DoubleNode import DoubleNode, prev
import pytest


@pytest.fixture()
def dn():
    dn = [0 for _ in range(3)]
    dn[0] = DoubleNode(3)
    dn[2] = DoubleNode(4)
    dn[1] = DoubleNode(5, dn[0], dn[2])
    return dn


def test_doublenode_prev(dn):
    assert prev(dn[1]) == dn[0], 'prev method works wrong'


def test_doublenode_next(dn):
    assert next(dn[1]) == dn[2], 'next method works wrong'


def test_doublenode_str(dn):
    assert str(dn[0]) == '3', 'str method works wrong'


def test_doublenode_initialization_without_data_gives_blank_node(dn):
    dn_0 = DoubleNode(prev_node=dn[1], next_node=dn[2])
    assert str(dn_0) == 'None', 'initialized node is not blank but should be'


def test_raises_error_when_init_with_wrong_next_node():
    with pytest.raises(Exception):
        node1 = 12
        DoubleNode(1, next_node=node1)


def test_raises_error_when_init_with_wrong_prev_node():
    with pytest.raises(Exception):
        node1 = 12
        DoubleNode(1, prev_node=node1)


def test_raises_error_when_trying_to_assign_wrong_prev_node():
    with pytest.raises(Exception):
        node2 = DoubleNode(12)
        node1 = 12
        node2.prev_node = node1
