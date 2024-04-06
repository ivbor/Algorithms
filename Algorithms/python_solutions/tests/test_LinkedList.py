from Algorithms.python_solutions.LinkedList import LinkedList
from Algorithms.python_solutions.Node import Node
import pytest


def test_can_create_blank_linkedlist():
    ll = LinkedList()
    assert isinstance(ll, LinkedList)


@pytest.fixture()
def blank_ll():
    ll = LinkedList()
    return ll


def test_no_nodes_size_of_ll_exists(blank_ll):
    assert blank_ll.size == 0, \
        'size attribute is absent or defined incorrectly'


def test_no_nodes_head_of_ll_exists(blank_ll):
    assert blank_ll.head is None, \
        'head attribute is absent or defined incorrectly'


def test_no_nodes_tail_of_ll_exists(blank_ll):
    assert blank_ll.tail is None, \
        'head attribute is absent or defined incorrectly'


def test_can_not_modify_tail_manually(blank_ll):
    with pytest.raises(Exception):
        blank_ll.tail = 12


def test_can_not_modify_size_manually(blank_ll):
    with pytest.raises(Exception):
        blank_ll.size = 100


@pytest.fixture()
def ll_with_node():
    node = Node(4)
    ll = LinkedList(node)
    return ll


@pytest.fixture()
def ll_with_same_head_and_tail():
    node = Node(1)
    ll = LinkedList(head=node, tail=node)
    return ll


def test_size_ll_with_1_node_initialized_differently(
        ll_with_same_head_and_tail):
    assert ll_with_same_head_and_tail.size == 1, \
        'size is wrong when head and tail of ll are same'


def test_head_and_tail_in_ll_with_1_node(
        ll_with_same_head_and_tail):
    assert ll_with_same_head_and_tail.head == \
        ll_with_same_head_and_tail.tail


def test_one_node_ll_has_size(ll_with_node):
    assert ll_with_node.size == 1, 'size attribute defined incorrectly'


def test_size1_ll_has_equal_head_and_tail(ll_with_node):
    assert ll_with_node.head == ll_with_node.tail, \
        'LinkedList with size 1 incorrectly initialized'


def test_can_initialize_ll_from_chain_of_nodes_using_head():
    node2 = Node(4)
    node1 = Node(4, node2)
    assert isinstance(LinkedList(node1), LinkedList), \
        'll was not initialized but should'


@pytest.fixture()
def ll_with_2_nodes_from_head():
    node2 = Node(4)
    node1 = Node(31, node2)
    ll = LinkedList(node1)
    return ll


def test_size_for_ll_with_2_nodes_is_2(ll_with_2_nodes_from_head):
    assert ll_with_2_nodes_from_head.size == 2, 'size calculated incorrectly'


def test_head_determines_correctly_for_ll_with_2_nodes(
        ll_with_2_nodes_from_head):
    assert str(ll_with_2_nodes_from_head.head) == '31', 'head \
            determines incorrectly or __str__ method for Node is wrong'


def test_tail_determines_correctly_for_ll_with_2_nodes(
        ll_with_2_nodes_from_head):
    assert str(ll_with_2_nodes_from_head.tail) == '4', 'tail \
        determines incorrectly or __str__ method for Node is wrong'


def test_ll_from_chain_of_nodes_using_tail_leads_to_blank_ll():
    node2 = Node(4)
    node1 = Node(4, node2)
    node3 = Node(31, node1)
    assert str(LinkedList(tail=node3)) == str(LinkedList())


@pytest.fixture()
def ll_with_2_nodes_from_tail():
    node2 = Node(4)
    node1 = Node(4, node2)
    node3 = Node(31, node1)
    ll = LinkedList(tail=node3)
    return ll


def test_size_for_ll_with_2_nodes_from_tail_is_0(ll_with_2_nodes_from_tail):
    assert ll_with_2_nodes_from_tail.size == 0, \
        'size for ll with 2 nodes from tail calculates incorrectly'


def test_head_of_ll_with_2_nodes_from_tail_is_none(ll_with_2_nodes_from_tail):
    assert ll_with_2_nodes_from_tail.head is None, \
        'head determines incorrectly when ll with 2 nodes \
        is initialized from tail'


def test_tail_of_ll_with_2_nodes_from_tail_is_none(ll_with_2_nodes_from_tail):
    assert ll_with_2_nodes_from_tail.tail is None, \
        'tail determines incorrectly when ll with 2 nodes \
        is initialized from tail'


def test_iter_in_ll_works():
    node2 = Node(2)
    node1 = Node(1, node2)
    node3 = Node(0, node1)
    ll = LinkedList(head=node3)
    for number, node in enumerate(ll):
        assert str(node) == str(number), '__iter__ in ll works incorrectly'


def test_append_in_ll_works():
    ll = LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    for j, i in enumerate(ll):
        assert (j+1) == i, 'append in ll works incorrectly'


def test_insertion_of_the_first_element_in_ll_works():
    ll = LinkedList()
    ll.insert(5, 1)
    for i in ll:
        assert i == 1, 'insertion of the first element \
            in ll works incorrectly'
    assert ll.size == 1, 'wrong size after insertion'


def test_insertion_in_the_head_in_ll_works():
    ll = LinkedList()
    ll.insert(5, 1)
    ll.insert(0, 0)
    for j, i in enumerate(ll):
        assert i == j, 'insertion in the head in ll works wrong'
    assert ll.size == 2, 'wrong size after insertion'


def test_append_by_insertion_in_ll_works():
    ll = LinkedList()
    other_ll = LinkedList()
    ll.insert(ll.size + 1, 1)
    ll.insert(0, 0)
    ll.insert(ll.size + 1, 2)
    for i in ll:
        other_ll.append(i)
    assert str(ll) == str(other_ll), 'append using insertion works wrong'


def test_actual_insertion_in_ll_works():
    ll = LinkedList()
    ll.insert(5, 1)
    ll.insert(0, 0)
    ll.insert(2, 2)
    ll.insert(3, 4)
    ll.insert(3, 3)
    for j, i in enumerate(ll):
        assert i == j, 'actual insertion works wrong in the ll'
    assert ll.size == 5, 'wrong size after insertion'


@pytest.fixture()
def ll_for_erase():
    ll = LinkedList()
    ll.insert(5, 1)
    ll.insert(0, 0)
    ll.insert(2, 2)
    ll.insert(3, 4)
    ll.insert(3, 3)
    return ll


def test_delete_head_element_in_ll_works(ll_for_erase):
    ll_for_erase.erase(0)
    for j, i in enumerate(ll_for_erase):
        assert i == (j + 1), 'deletion of the head element works wrong'
    assert ll_for_erase.size == 4, 'wrong size after deletion'


def test_delete_the_last_element_in_ll_works(ll_for_erase):
    ll_for_erase.erase(4)
    for j, i in enumerate(ll_for_erase):
        assert i == j, 'deletion of the last element works wrong'
    assert ll_for_erase.size == 4, 'wrong size after deletion'


def test_delete_only_element_in_ll(ll_with_node):
    ll_with_node.erase(0)
    ll = LinkedList()
    assert str(ll_with_node) == str(ll), 'deletion of the last \
        element should lead to the blank ll but does not'


def test_delete_i_th_element_in_ll_works(ll_for_erase):
    ll_for_erase.erase(1)
    assert 1 not in ll_for_erase.list_all(), \
        'deletion of the i-th element works wrong'


def test_neg_indexes_in_erase_in_ll_work(ll_for_erase):
    ll_for_erase.insert(5, 5)
    ll_for_erase.erase(-5)
    ll_for_erase.erase(0)
    ctr = 0
    for j, i in enumerate(ll_for_erase):
        if j == (i - 2):
            ctr += 1
    assert ctr == 4, 'negative index points to wrong element in the ll'


def test_update(ll_for_erase):
    ll_for_erase.update(1, 0)
    for j, i in enumerate(ll_for_erase):
        if j == 0 or j == 1:
            assert i == 0, 'update works wrong in the ll'


def test_neg_index_in_update_never_works(ll_for_erase):
    with pytest.raises(Exception):
        ll_for_erase.update(-1, 3)


def test_ll_stores_nones(ll_for_erase):
    ll_for_erase.update(1, None)
    assert ll_for_erase.list_all()[1] is None, \
        'll cannot store nones but should'


def test_ll_contains(ll_for_erase):
    assert not (10 in ll_for_erase), '__contains__ shows the presence \
        of absent element'
    assert 2 in ll_for_erase, '__contains__ shows absence of present \
        number'


def test_ll_repr(ll_for_erase):
    assert ll_for_erase.__repr__() == str(ll_for_erase), \
        '__repr__ works wrong for ll'


def test_indexing_with_neg_numbers_inside_insert(ll_for_erase):
    with pytest.raises(Exception):
        ll_for_erase.insert(-1, -1)
