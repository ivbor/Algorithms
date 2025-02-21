import pytest
import random

from math import gcd

from Algorithms_Python.segment_tree \
    import SegmentTree, SegmentTreeOptimized

# Sample data
data1 = [random.randint(-100, 100)
         for _ in range(random.randint(100, 10000))]
data2 = data1 + [random.randint(-100, 100)]

data = [data1, data2]


@pytest.mark.parametrize('data', data)
def test_build_tree(data):
    segment_tree = SegmentTree(data)
    segment_tree_opt = SegmentTreeOptimized(data)
    mid = (len(data) // 2 + 1) if len(data) % 2 == 1 else (len(data) // 2)
    assert segment_tree.tree_sum[:3] == [sum(data),
                                         sum(data[:mid]),
                                         sum(data[mid:])]
    assert segment_tree.tree_min[:3] == [min(data),
                                         min(data[:mid]),
                                         min(data[mid:])]
    assert segment_tree.tree_max[:3] == [max(data),
                                         max(data[:mid]),
                                         max(data[mid:])]
    assert segment_tree.tree_gcd[:3] == [gcd(*data),
                                         gcd(*data[:mid]),
                                         gcd(*data[mid:])]
    assert [segment_tree_opt.tree[i][0] for i in range(3)] == \
        [sum(data), sum(data[:mid]), sum(data[mid:])]
    assert [segment_tree_opt.tree[i][1] for i in range(3)] == \
        [min(data), min(data[:mid]), min(data[mid:])]
    assert [segment_tree_opt.tree[i][2] for i in range(3)] == \
        [max(data), max(data[:mid]), max(data[mid:])]
    assert [segment_tree_opt.tree[i][3] for i in range(3)] == \
        [gcd(*data), gcd(*data[:mid]), gcd(*data[mid:])]


@pytest.mark.parametrize('data', data)
def test_query_sum(data):
    segment_tree = SegmentTree(data)
    segment_tree_opt = SegmentTreeOptimized(data)
    assert segment_tree.query(sum, 0, 3) == sum(data[0:4])
    assert segment_tree.query(sum, 2, 6) == sum(data[2:7])
    assert segment_tree.query(sum, 3, 5) == sum(data[3:6])
    assert segment_tree_opt.query(sum, 0, 3) == sum(data[0:4])
    assert segment_tree_opt.query(sum, 2, 6) == sum(data[2:7])
    assert segment_tree_opt.query(sum, 3, 5) == sum(data[3:6])


@pytest.mark.parametrize('data', data)
def test_query_min(data):
    segment_tree = SegmentTree(data)
    segment_tree_opt = SegmentTreeOptimized(data)
    assert segment_tree.query(min, 1, 4) == min(data[1:5])
    assert segment_tree.query(min, 0, 7) == min(data[0:8])
    assert segment_tree.query(min, 2, 6) == min(data[2:7])
    assert segment_tree_opt.query(min, 1, 4) == min(data[1:5])
    assert segment_tree_opt.query(min, 0, 7) == min(data[0:8])
    assert segment_tree_opt.query(min, 2, 6) == min(data[2:7])


@pytest.mark.parametrize('data', data)
def test_query_max(data):
    segment_tree = SegmentTree(data)
    segment_tree_opt = SegmentTreeOptimized(data)
    assert segment_tree.query(max, 1, 4) == max(data[1:5])
    assert segment_tree.query(max, 0, 7) == max(data[0:8])
    assert segment_tree.query(max, 2, 6) == max(data[2:7])
    assert segment_tree_opt.query(max, 1, 4) == max(data[1:5])
    assert segment_tree_opt.query(max, 0, 7) == max(data[0:8])
    assert segment_tree_opt.query(max, 2, 6) == max(data[2:7])


@pytest.mark.parametrize('data', data)
def test_query_gcd(data):
    segment_tree = SegmentTree(data)
    segment_tree_opt = SegmentTreeOptimized(data)
    assert segment_tree.query(gcd, 1, 4) == gcd(*data[1:5])
    assert segment_tree.query(gcd, 0, 7) == gcd(*data[0:8])
    assert segment_tree.query(gcd, 2, 6) == gcd(*data[2:7])
    assert segment_tree_opt.query(gcd, 1, 4) == gcd(*data[1:5])
    assert segment_tree_opt.query(gcd, 0, 7) == gcd(*data[0:8])
    assert segment_tree_opt.query(gcd, 2, 6) == gcd(*data[2:7])


@pytest.mark.parametrize('data', data)
def test_update(data):
    segment_tree = SegmentTree(data)
    segment_tree_opt = SegmentTreeOptimized(data)
    segment_tree.update(2, 7)
    segment_tree_opt.update(2, 7)
    data[2] = 7
    assert segment_tree.query(sum, 2, 6) == sum(data[2:7])
    assert segment_tree.query(max, 2, 6) == max(data[2:7])
    assert segment_tree.query(min, 2, 6) == min(data[2:7])
    assert segment_tree.query(gcd, 2, 6) == gcd(*data[2:7])
    assert segment_tree_opt.query(sum, 2, 6) == sum(data[2:7])
    assert segment_tree_opt.query(max, 2, 6) == max(data[2:7])
    assert segment_tree_opt.query(min, 2, 6) == min(data[2:7])
    assert segment_tree_opt.query(gcd, 2, 6) == gcd(*data[2:7])


@pytest.mark.parametrize('data', data)
def test_new_action(data):
    segment_tree_opt = SegmentTreeOptimized(data)

    new_action_func = sum
    neutral_elt = 0
    segment_tree_opt.new_action(new_action_func, neutral_elt)
    assert new_action_func in segment_tree_opt.action


@pytest.mark.parametrize('data', data)
def test_build_new_action(data):
    segment_tree_opt = SegmentTreeOptimized(data)

    new_action_func = sum
    neutral_elt = 0
    segment_tree_opt.new_action(new_action_func, neutral_elt)

    assert segment_tree_opt.query(new_action_func, 0, 4) == sum(data[0:5])

    new_action_func = lambda x: gcd(*x)
    segment_tree_opt.new_action(new_action_func, neutral_elt)

    assert segment_tree_opt.query(new_action_func, 1, 3) == gcd(*data[1:4])
