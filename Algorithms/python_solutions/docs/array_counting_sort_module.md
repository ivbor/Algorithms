# array_counting_sort_module

Functions
---------
array_count_sort(arr: list[list[int]], key: int = 0)
    Sort a 2-dimensional array of integers based on a key index.

<a id="python_solutions.array_count_sort.array_count_sort"></a>

#### array\_count\_sort

```python
def array_count_sort(arr: list[list[int]], key: int = 0) -> list[list[int]]
```

This function performs counting sort on the 2-dimensional array
of whole numbers.

This algorithm uses count sort to sort rows inside matrix
by ascending order. It works only with integer numbers,
so if your matrix contains floats - do not use this algorithm.
- **Time to work**: O(number of rows in the array) or

O(difference between the biggest and the lowest value
in the key index) depending on what is more.

## Parameters
- **array**: list[list[int]]

    2-dimensional array which will be sorted

- **key**: int

    Shows by which index to sort, works even in situations
    when there are blank spaces with this index in the rows.
    In this case puts those rows higher than those with
    filled spaces.
- **Default value**: 0


## Returns

list[list[int]]
    Sorted array

AVL Tree Module

This module implements an AVL tree, a self-balancing binary search tree.
This tree has very fixed height, which is smaller than that of RedBlackTree,
and is between log2(size) and 2*log2(size).

Classes
-------
AVLNode
    A class representing a node in an AVL tree, extending TreeNode.

AVLTree
    A class representing an AVL tree,
    extending RedBlackTree and BinarySearchTree.

<a id="python_solutions.avl_tree.BinarySearchTree"></a>

## BinarySearchTree

<a id="python_solutions.avl_tree.TreeNode"></a>

## TreeNode

<a id="python_solutions.avl_tree.RedBlackTree"></a>

## RedBlackTree

<a id="python_solutions.avl_tree.AVLNode"></a>

## AVLNode Objects

```python
class AVLNode(TreeNode)
```

Node for AVL Tree

Represents a node in an AVL tree. Inherits from TreeNode and provides
methods to calculate height and balance factor.

## Attributes
- **data**: any

    The data stored in the node.

## Methods

__init__(self, data: int | float) -> None
    Initialize an AVLNode.

height(self) -> int
    Calculate the height of the node.

balance_factor(self) -> int
    Calculate the balance factor of the node.

<a id="python_solutions.avl_tree.AVLNode.__init__"></a>

#### \_\_init\_\_

```python
def __init__(data: int | float) -> None
```

Initialize an AVLNode object with data.

## Parameters
- **data**: int | float

    The data to be stored in the node.

## Returns

None

<a id="python_solutions.avl_tree.AVLNode.height"></a>

#### height

```python
def height() -> int
```

Calculate the height of the node.

## Returns

int
    The height of the node.

<a id="python_solutions.avl_tree.AVLNode.balance_factor"></a>

#### balance\_factor

```python
def balance_factor() -> int
```

Calculate the balance factor of the node.

## Returns

int
    The balance factor of the node.

<a id="python_solutions.avl_tree.AVLTree"></a>

## AVLTree Objects

```python
class AVLTree(RedBlackTree, BinarySearchTree)
```

AVL Tree Implementation

Represents an AVL tree, a self-balancing binary search tree.

## Methods

__init__(self) -> None
    Initialize an AVLTree object.

insert(self, key: int | float) -> None
    Insert a key into the AVL tree.

_insert(root: AVLNode, new_node: AVLNode)
    Helper method to insert a new node into the AVL tree.

delete(self, key: int | float) -> None
    Delete a key from the AVL tree.

_delete(node: AVLNode) -> None
    Helper method to delete a node from the AVL tree.

<a id="python_solutions.avl_tree.AVLTree.__init__"></a>

#### \_\_init\_\_

```python
def __init__() -> None
```

Initialize an AVLTree object.

## Returns

None

<a id="python_solutions.avl_tree.AVLTree.insert"></a>

#### insert

```python
def insert(key: int | float) -> None
```

Insert a key into the AVL tree.

## Parameters
- **key**: int | float

    The key to be inserted into the AVL tree.

## Returns

None

<a id="python_solutions.avl_tree.AVLTree._insert"></a>

#### \_insert

```python
def _insert(root: AVLNode, new_node: AVLNode) -> None
```

Helper method to insert a new node into the AVL tree.

## Parameters
- **root**: AVLNode

    The root node of the AVL tree.

- **new_node**: AVLNode

    The new node to be inserted into the AVL tree.

## Returns

None

<a id="python_solutions.avl_tree.AVLTree.delete"></a>

#### delete

```python
def delete(key: int | float) -> None
```

Delete a key from the AVL tree.

## Parameters
- **key**: int | float

    The key to be deleted from the AVL tree.

## Returns

None

<a id="python_solutions.avl_tree.AVLTree._delete"></a>

#### \_delete

```python
def _delete(node: AVLNode) -> None
```

Helper method to delete a node from the AVL tree.

## Parameters
- **node**: AVLNode

    The node to be deleted from the AVL tree.

## Returns

None