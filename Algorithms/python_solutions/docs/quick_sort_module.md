# quick_sort_module

This module provides Quick Sort implementations for efficiently sorting
a list of elements. Quick Sort is a divide-and-conquer algorithm that selects
a pivot value, divides the input array, and sorts the resulting parts.

Functions
---------
quick_sort(array: list[float], pivot_str: str = 'random') -> list[float]
    Sorts a list of elements using the Quick Sort algorithm.

split(a: list[float], pivot: float, left_edge: int, right_edge: int) ->
    tuple
    Divides the input array into two parts relative to the pivot value.

avg(a: list[float], left_edge: int, right_edge: int) -> float
    Calculates the average value of elements in a specified range.

clst_avg(a: list[float], avg: float, left_edge: int, right_edge: int) ->
    float
    Finds the element closest to the average value in a specified range.

_quick_sort(array: list[float], left_edge: int, right_edge: int,
- **pivot_str**: str = 'random') -> list[float]

    Performs the Quick Sort algorithm on a given array within specified
    indices.

median_of_medians(array: list[float], left: int, right: int) -> int
    Finds the index of median of medians for a given array within specified
    indices.

partition_small(array: list[float], left: int, right: int, opt: bool = True)
    -> int
    Sorts a small portion of the array using a bubble sort to find a
    median inside this array portion.
    Optimised version (opt=True) calls Insertion Sort for small arrays.

median_of_three(array: list[float], left: int, right: int) -> float
    Finds the median of three elements in a given array within specified
    indices.

<a id="python_solutions.quick_sort.logging"></a>

## logging

<a id="python_solutions.quick_sort.random"></a>

## random

<a id="python_solutions.quick_sort.split"></a>

#### split

```python
def split(a: list[float], pivot: float, left_edge: int,
- **right_edge**: int) -> tuple[int, int]

```

Split Function

Divide the input array  into two parts relative to the pivot value.
Elements less than pivot are moved to the left,
and elements greater or equal are moved to the right.

## Parameters
- **a**: list[float]

    The input list to be split.

- **pivot**: float

    The pivot value used for splitting the array.

- **left_edge**: int

    The starting index for the split operation.

- **right_edge**: int

    The ending index (exclusive) for the split operation.

## Returns

tuple
    A tuple containing two indices that represent the
    new boundaries for the split parts.

<a id="python_solutions.quick_sort.clst_avg"></a>

#### clst\_avg

```python
def clst_avg(a: list[float], left_edge: int, right_edge: int) -> float
```

Calculate the average value of elements in a specified range.

## Parameters
- **a**: list[float]

    The input list.

- **left_edge**: int

    The starting index for the range.

- **right_edge**: int

    The ending index (exclusive) for the range.

## Returns

float
    The average value of elements in the specified range.

<a id="python_solutions.quick_sort.partition_small"></a>

#### partition\_small

```python
def partition_small(array: list[float],
- **left**: int,

- **right**: int,

- **opt**: bool = QUICK_OPT) -> int

```

Partition a small portion of the array using a bubble sort algorithm.

## Parameters
- **array**: list[float]

    The input array.

- **left**: int

    The starting index for the range.

- **right**: int

    The ending index (exclusive) for the range.

## Returns

int
    The index representing the partitioned element.

<a id="python_solutions.quick_sort.median_of_medians"></a>

#### median\_of\_medians

```python
def median_of_medians(array: list[float], left: int, right: int) -> int
```

Find the median of medians for a given array within specified indices.

## Parameters
- **array**: list[float]

    The input array.

- **left**: int

    The starting index for the range.

- **right**: int

    The ending index (exclusive) for the range.

## Returns

int
    The median of medians.

<a id="python_solutions.quick_sort.median_of_three"></a>

#### median\_of\_three

```python
def median_of_three(array: list[float], left: int, right: int) -> float
```

Find the median of three elements in a given array within specified
indices.

## Parameters
- **array**: list[float]

    The input array.

- **left**: int

    The starting index for the range.

- **right**: int

    The ending index (exclusive) for the range.

## Returns

float
    The median of three elements.

<a id="python_solutions.quick_sort._quick_sort"></a>

#### \_quick\_sort

```python
def _quick_sort(array: list[float],
- **left_edge**: int,

- **right_edge**: int,

- **pivot_str**: str = 'random',

                no_recursion=False) -> list[float]
```

Quick Sort Function

Sort the input array using the Quick Sort algorithm. This function
performs a divide-and-conquer approach by selecting a pivot value and
- **splitting the array into two parts**: elements less than the pivot and

elements greater or equal to the pivot.

## Parameters
- **array**: list

    The input list to be sorted.

- **left_edge**: int

    The starting index for the sort operation.

- **right_edge**: int

    The ending index (exclusive) for the sort operation.

- **pivot_str**: 'random', 'clst_avg', 'm3' or 'mm'

    A strategy to choose pivot element.

    'random' for random selection among the elements, works well for
    random or uniformly distributed data.

    'clst_avg' for selection of element close to the average of the
    array,  works well for data with known distribution.

    'm3' or median of three provides some resistance against worst
    cases, works well on data with some outliers or some degree of
    ordering but not fully sorted.

    'mm' of median of medians or introselect performs well consistently
    regardless of the input data

- **no_recursion**: bool

    Switcher between recursive and non-recursive algorithms.

## Returns

list
    The sorted array.

<a id="python_solutions.quick_sort.quick_sort"></a>

#### quick\_sort

```python
def quick_sort(array: list[float],
- **pivot_str**: str = 'random',

- **no_recursion**: bool = False) -> list[float]

```

Quick Sort Function (Wrapper)

Sort the input list using the Quick Sort algorithm. This function is a
wrapper for the `_quick_sort` function and sets initial values for the
sorting process. A wide selection of pivot strategies is available.
- **Average and worst space complexities**: - random: O(log n), O(n)

- closest to the average: O(log n), O(n)
- median of three: O(log n), O(log n)
- median of medians: O(log n), O(log n)
- **Average and worst time complexities**: - random: O(n * log n), O(n ** 2)

- closest to the average: O(n * log n), O(n * log n)
- median of three: O(n * log n), O(n * log n)
- median of medians: O(n * log n), O(n * log n)
- **Important considerations**: O(n ** 2) performance is so extremely rare, it has no implications in

practical usage. Median of medians pivot calculation suffers from
big constant factor, which makes it impractical for small arrays.
It is worth noting that quick sort is unstable.

## Parameters
- **array**: list

    The input list to be sorted.

- **pivot_str**: 'random', 'clst_avg', 'm3' or 'mm'

    A strategy to choose pivot element.

    'random' for random selection among the elements, works well for
    random or uniformly distributed data.

    'clst_avg' for selection of element close to the average of the
    array,  works well for data with known distribution.

    'm3' or median of three provides some resistance against worst
    cases, works well on data with some outliers or some degree of
    ordering but not fully sorted.

    'mm' of median of medians or introselect performs well consistently
    regardless of the input data

- **no_recursion**: bool

    Switcher between recursive and non-recursive algorithms.

## Returns

list
    The sorted list.

Real Binary Search Module

This module provides a binary search function for finding an approximate
input value (x) for which a given function func(x) is close to func_value
within a specified epsilon. The binary search algorithm is suitable for
monotonic functions.

Functions
---------
real_bin_search(func, func_value, left_edge,
    right_edge, eps=1e-6, check=False)
    Performs a binary search among real numbers to find an x
    where func(x) is approximately equal to func_value.

<a id="python_solutions.real_bin_search.real_bin_search"></a>

#### real\_bin\_search

```python
def real_bin_search(func,
                    func_value,
                    left_edge,
                    right_edge,
                    eps=1e-6,
                    check=False)
```

This function performs a binary search among real numbers to find an x
where func(x) is approximately equal to func_value.

It works only for monotonic functions and
has a time complexity of O(log2(n)),
where n is the number of epsilon intervals that can fit in the
absolute difference between right_edge and left_edge.

## Parameters
- **func**: callable

    The function for which we are searching for an input value.

- **func_value**: float

    The target value we want to find an input value for.

- **left_edge**: float

    The left edge of the search interval.
    The function is assumed to exist within this interval.

- **right_edge**: float

    The right edge of the search interval.
    The function is assumed to exist within this interval.

- **eps**: float, optional

    The epsilon value that determines the desired accuracy of the result.
    The search will stop when the interval size
    becomes smaller than this epsilon. Default is 1e-6.

- **check**: bool, optional

    If True, the function will perform a check to ensure that
    the func_value is reachable within the given edges. Default is False.

## Returns

float
    The approximate input value (x) for which func(x) is close to
    func_value within the specified epsilon.

## Raises

KeyError
    Is raised if the check parameter is set to True and the func_value is
    unreachable within the given edges.

Red-Black Tree Module
=========================

This module defines a Red-Black Tree class which represents balanced
binary search tree. By coloring nodes it is possible to maintain
the height of O(logn), here in particular it is 3*log2n.

Classes
-------
TreeNode
    A class representing a node in the Red-Black Tree.

BinarySearchTree
    A class representing a Red-Black Tree.

<a id="python_solutions.red_black_tree.logging"></a>

## logging

<a id="python_solutions.red_black_tree.TreeNode"></a>

## TreeNode

<a id="python_solutions.red_black_tree.BinarySearchTree"></a>

## BinarySearchTree

<a id="python_solutions.red_black_tree.RBTreeNode"></a>

## RBTreeNode Objects

```python
class RBTreeNode(TreeNode)
```

Red-Black Tree Node Class

This class represents a node in a red-black tree.
It extends the TreeNode class.

## Attributes
- **color**: str

    The color of the node, either 'red' or 'black'.

<a id="python_solutions.red_black_tree.RBTreeNode.__init__"></a>

#### \_\_init\_\_

```python
def __init__(data, color)
```

Initialize a Red-Black Tree Node.

## Parameters
- **data**: any

    The data to be stored in the node.

- **color**: str

    The color of the node, either 'red' or 'black'.

## Returns

None

<a id="python_solutions.red_black_tree.RedBlackTree"></a>

## RedBlackTree Objects

```python
class RedBlackTree(BinarySearchTree)
```

Red-Black Tree Class

This class represents a red-black tree,
which is a self-balancing binary search tree.

## Attributes
- **node_class**: RBTreeNode

    The class to use for creating nodes in the tree.

## Methods

__init__(self) -> None
    Initialize a RedBlackTree object.

insert(self, key: int | float) -> None
    Insert key into RedBlackTree.

handle_rb(self, new_node: RBTreeNode) -> None
    The function managing insertion into RedBlackTree.

recolor(self, node: RBTreeNode, uncle: RBTreeNode) -> None
    The function handling the case when only recoloring is needed.

rotate_and_recolor(self, node: RBTreeNode, right: bool) -> None
    The function handling the case when both rotation and recoloring
    have to be done.

_left_rotate(self, node: RBTreeNode) -> None
    The function performing left rotation with node being moved to its
    left child place and the right child of the node moved to the
    node's place.

_right_rotate(self, node: RBTreeNode) -> None
    The function performing right rotation with node being moved to its
    right child place and the left child of the node moved to the
    node's place.

_delete(self, node: RBTreeNode) -> None
    The function performing deletion of the node.

_fix_double_black(self, node: RBTreeNode) -> None
    The function handling the double black violation case
    (parent and child are black) when deleting node.

<a id="python_solutions.red_black_tree.RedBlackTree.__init__"></a>

#### \_\_init\_\_

```python
def __init__() -> None
```

Initialize a Red-Black Tree.

## Returns

None

<a id="python_solutions.red_black_tree.RedBlackTree.insert"></a>

#### insert

```python
def insert(key: int | float) -> None
```

Insert a key into the red-black tree.

## Parameters
- **key**: int | float

    The key to insert into the tree.

## Returns

None

<a id="python_solutions.red_black_tree.RedBlackTree.handle_rb"></a>

#### handle\_rb

```python
def handle_rb(new_node: RBTreeNode) -> None
```

Handle red-black tree properties after inserting a node.

## Parameters
- **new_node**: RBTreeNode

    The newly inserted node.

## Returns

None

<a id="python_solutions.red_black_tree.RedBlackTree.recolor"></a>

#### recolor

```python
def recolor(node: RBTreeNode, uncle: RBTreeNode) -> None
```

Recolor nodes in the red-black tree after insertion.

## Parameters
- **node**: RBTreeNode

    The newly inserted node.

- **uncle**: RBTreeNode

    The uncle node of the newly inserted node.

## Returns

None

<a id="python_solutions.red_black_tree.RedBlackTree.rotate_and_recolor"></a>

#### rotate\_and\_recolor

```python
def rotate_and_recolor(node: RBTreeNode, right: bool) -> None
```

Rotate and recolor nodes in the red-black tree after insertion.

## Parameters
- **node**: RBTreeNode

    The newly inserted node.

- **right**: bool

    Flag indicating if the uncle of the newly inserted node is on
    the right (in this case is True) or on the left (False).

## Returns

None

<a id="python_solutions.red_black_tree.RedBlackTree._left_rotate"></a>

#### \_left\_rotate

```python
def _left_rotate(node: RBTreeNode) -> None
```

Perform a left rotation on the red-black tree.

## Parameters
- **node**: RBTreeNode

    The node around which the rotation is performed.

## Returns

None

<a id="python_solutions.red_black_tree.RedBlackTree._right_rotate"></a>

#### \_right\_rotate

```python
def _right_rotate(node: RBTreeNode) -> None
```

Perform a right rotation on the red-black tree.

## Parameters
- **node**: RBTreeNode

    The node around which the rotation is performed.

## Returns

None

<a id="python_solutions.red_black_tree.RedBlackTree._delete"></a>

#### \_delete

```python
def _delete(node: RBTreeNode) -> None
```

Delete a node from the red-black tree.

## Parameters
- **node**: RBTreeNode

    The node to be deleted.

## Returns

None

<a id="python_solutions.red_black_tree.RedBlackTree._fix_double_black"></a>

#### \_fix\_double\_black

```python
def _fix_double_black(node: RBTreeNode) -> None
```

Fix double black violation in the red-black tree.

## Parameters
- **node**: TreeNode

    The node causing the double black violation.

## Returns

None