import pytest
import random
import math

from Algorithms.python_solutions.avl_tree import AVLTree


@pytest.fixture
def avl_tree():
    tree = AVLTree()
    tree.insert(5)
    tree.insert(3)
    tree.insert(7)
    tree.insert(2)
    tree.insert(4)
    tree.insert(6)
    tree.insert(8)
    return tree


def test_insert(avl_tree):
    assert avl_tree.in_order_traversal() == [2, 3, 4, 5, 6, 7, 8]


def test_delete(avl_tree):
    avl_tree.delete(4)
    assert avl_tree.in_order_traversal() == [2, 3, 5, 6, 7, 8]
    avl_tree.delete(5)
    assert avl_tree.in_order_traversal() == [2, 3, 6, 7, 8]
    avl_tree.delete(2)
    assert avl_tree.in_order_traversal() == [3, 6, 7, 8]
    avl_tree.delete(8)
    assert avl_tree.in_order_traversal() == [3, 6, 7]


def test_delete_with_error(avl_tree):
    avl_tree_list = avl_tree.in_order_traversal()
    for _ in range(7):
        elt_to_delete = random.choice(avl_tree_list)
        avl_tree.delete(elt_to_delete)
    with pytest.raises(IndexError):
        avl_tree.delete(None)


def test_search(avl_tree):
    assert avl_tree._search(avl_tree.root, 3) is not None
    assert avl_tree._search(avl_tree.root, 9) is None


def test_random_length_and_elts():
    avltree = AVLTree()
    avltree_length = random.randint(1000, 2000)
    for _ in range(avltree_length):
        avltree.insert(random.randint(-1000, 1000))
        new_height = avltree.max_height()
        assert new_height >= int(math.log2(avltree.size) + 1)
        assert new_height <= 2*int(math.log2(avltree.size) + 1)
    list_avltree = avltree.in_order_traversal()
    assert len(list_avltree) == avltree_length
    assert sorted(list_avltree) == list_avltree
    for _ in range(avltree_length):
        elt_to_delete = random.choice(list_avltree)
        avltree.delete(elt_to_delete)
        list_avltree.remove(elt_to_delete)
        assert len(list_avltree) == avltree.size
        assert sorted(list_avltree) == avltree.in_order_traversal()
    assert len(avltree.in_order_traversal()) == 0
