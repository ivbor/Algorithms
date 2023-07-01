from Algorithms.python_solutions import Nodes
from Algorithms.python_solutions.DoubleNodes import CyclicLinkedList
import pytest


def test_can_create_node():
    node = Nodes.Node()
    node_data = Nodes.Node(4)
    assert type(node) == Nodes.Node
    assert type(node_data) == Nodes.Node


def test_node_can_take_and_print_data():
    node = Nodes.Node(4)
    assert str(node) == '4', None


def test_node_can_store_next_node():
    next_node = Nodes.Node('next')
    node = Nodes.Node('&', next_node)
    assert next(node) == next_node


def test_eq_for_node():
    node1 = Nodes.Node(4)
    node2 = Nodes.Node(4)
    node3 = node1
    assert not (node1 == node2), None
    assert node1 == node3, None


def test_can_create_ll():
    ll = Nodes.LinkedList()
    assert type(ll) == Nodes.LinkedList


def test_can_add_nodes_to_ll():

    # case 1 - no nodes
    ll = Nodes.LinkedList()
    assert ll.size == 0, ll.size
    assert ll.head is None, ll.head
    assert ll.tail is None, ll.tail

    # case 2 - one node
    node = Nodes.Node(4)
    ll = Nodes.LinkedList(node)
    assert ll.size == 1, ll.size
    assert ll.head == ll.tail, help(Nodes.LinkedList)

    # case 3 - 2 or more nodes
    # with specifying the head
    node2 = Nodes.Node(4)
    node1 = Nodes.Node(4, node2)
    ll = Nodes.LinkedList(node1)
    assert ll.size == 2, ll.size
    assert ll.head == node1, ll.head
    assert ll.tail == node2, ll.tail
    # with specifying the tail
    node2 = Nodes.Node(4)
    node1 = Nodes.Node(4, node2)
    node3 = Nodes.Node(31, node1)
    ll = Nodes.LinkedList(tail=node3)
    assert ll.size == 0, ll.size
    assert ll.head is None, ll.head
    assert ll.tail == ll.head, ll.tail


def test_iter_in_ll_works():

    node2 = Nodes.Node(1)
    node1 = Nodes.Node(2, node2)
    node3 = Nodes.Node(4, node1)
    ll = Nodes.LinkedList(tail=node3)
    for i in ll:
        assert str(i) == '4', i


def test_append():

    ll = Nodes.LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    for j, i in enumerate(ll):
        assert (j+1) == i, i


def test_insert():

    # insertion of the first element
    ll = Nodes.LinkedList()
    ll.insert(1, 5)
    ctr = 0
    for i in ll:
        assert i == 1, i
        ctr += 1
    assert ctr == 1, ctr

    # insertion in the head
    ll.insert(0, 0)
    ctr = 0
    for j, i in enumerate(ll):
        ctr += 1
        assert i == j, (i, j)
    assert ctr == 2, ctr

    # append by insertion
    ll.insert(2, 2)
    ctr = 0
    for j, i in enumerate(ll):
        assert i == j, (i, j)
        ctr += 1
    assert ctr == 3, ctr

    # check actual insertion
    ll.insert(4, 3)
    ll.insert(3, 3)
    ctr = 0
    for j, i in enumerate(ll):
        assert i == j, (i, j)
        ctr += 1
    assert ctr == 5, ctr


def test_erase():

    # delete head element
    ll = Nodes.LinkedList()
    ll.insert(1, 5)
    ll.insert(0, 0)
    ll.insert(2, 2)
    ll.insert(4, 3)
    ll.insert(3, 3)
    ll.erase(0)
    ctr = 0
    for j, i in enumerate(ll):
        assert i == (j + 1), (i, j)
        ctr += 1
    assert ctr == 4, ctr

    # delete the last element
    ll.erase(3)
    ctr = 0
    for j, i in enumerate(ll):
        assert i == (j + 1), (i, j)
        ctr += 1
    assert ctr == 3, ctr

    # delete i-th element
    ll.erase(1)
    ctr = 0
    for i in ll:
        if i == 1:
            ctr += 1
        if i == 3:
            ctr += 1
    assert ctr == 2, ctr


def test_neg_indexes_in_erase_and_repr():

    ll = Nodes.LinkedList()
    ll.insert(1, 5)
    ll.insert(0, 0)
    ll.insert(2, 2)
    ll.insert(4, 3)
    ll.insert(3, 3)
    ctr = 0
    for j, i in enumerate(ll):
        if j == i:
            ctr += 1
    assert ctr == 5, ctr
    ll.insert(5, 5)
    ctr = 0
    for j, i in enumerate(ll):
        if j == i:
            ctr += 1
    assert ctr == 6, print(ll)
    ll.erase(-5)
    ll.erase(0)
    ctr = 0
    for j, i in enumerate(ll):
        if j == (i - 2):
            ctr += 1
    assert ctr == 4, print(ll)


def test_update():

    ll = Nodes.LinkedList()
    ll.insert(1, 5)
    ll.insert(0, 0)
    ll.insert(2, 2)
    ll.insert(4, 3)
    ll.insert(3, 3)
    ll.update(0, 1)
    for j, i in enumerate(ll):
        if j == 0 or j == 1:
            assert i == 0, ll.list_all()


def test_ll_stores_nones():
    ll = Nodes.LinkedList()
    ll.insert(1, 5)
    ll.insert(0, 0)
    ll.insert(2, 2)
    ll.insert(4, 3)
    ll.insert(3, 3)
    ll.update(None, 1)
    assert ll.list_all()[1] is None


def test_ll_in():
    ll = Nodes.LinkedList()
    ll.insert(1, 5)
    ll.insert(0, 0)
    ll.insert(2, 2)
    ll.insert(4, 3)
    ll.insert(3, 3)
    ll.update(None, 1)
    assert 2 in ll, ll.list_all()


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
    cll.update(None, 1)
    assert cll.size == 1, cll.size
    assert str(cll) == str([None]), cll.list_all()
    cll.erase(1)
    assert str(cll) == str([]), cll.list_all()
    assert cll.size == 0, cll.size
    # test everything for many elements
    for i in range(10):
        cll.insert(str(i), i)
    assert str(cll) == str([str(i) for i in range(10)])
    assert cll.size == 10
    for i in enumerate(cll):
        if i[0] == cll.size:
            break
        cll.update(None, i[0])
    assert cll.list_all() == [None for i in range(10)]
    for i in enumerate(cll):
        if i[0] == 10:
            break
        cll.erase(9-i[0])
    assert cll.size == 0
    assert str(cll) == str([])
