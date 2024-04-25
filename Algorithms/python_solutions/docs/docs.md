Algorithms
==========

This module contains implementations of some data structures
and sorting algorithms.

Contains
--------
- Folder 'python_solutions' with implementations on Python,
more info inside __init__.py file within the folder.

- Folder 'C_solutions' with implementations on C.

python_solutions
================

This module contains implementations of various sorting algorithms,
basic data structures and tests providing not only coverage for code,
but also examples of usage.

Contents
--------
- Sorting Algorithms
  ------------------
  - insertion_sorts (insert_sort.py)
  - merge_sort (merge_sort.py)
  - quick_sort (quick_sort.py)
  - heap_sort (heap.py)
  - sort by counting (count_sort.py)
  - sort by key inside array (array_count_sort.py)
  - sort by key inside 2-dim array (two_dim_array_count_sort.py)
  - sort by digits (digit_sort.py)
  ---------------
- Data Structures
  ---------------
  Array-like
  ---------------
  - Vector (vector.py)
  - Heap (heap.py)
  ----------------------
  Nodes and Linked Lists
  ----------------------
  - OneWayNode (Node.py)
  - TwoWayNode (DoubleNode.py)
  - LinkedList (LinkedList.py)
  - Queue (Queue.py)
  - Stack (Stack.py)
  - Deque (Deque.py)
  - CyclicLinkedList (CyclicLinkedList.py)
  -------------
  Probabilistic
  -------------
  - HashTables with different collision handling approaches (hashtable.py)
  - BloomFilter (bloom_filter.py)
  - HyperLogLog (hyperloglog.py)
  -----
  Trees
  -----
  - BinarySearchTree (bst.py)
  - AVLTree (avl_tree.py)
  - RedBlackTree (red_black_tree.py)
  - SegmentTree (segment_tree.py)
  - SparseTable (sparse_table.py)
  ----------------------
  Graphs and Graph Nodes
  ----------------------
  - GraphNodes and Edges (graph_nodes.py)
  - Graph (graph.py)
  - WeightedGraph (weighted_graph.py)
  --------------------
- Searching Algorithms
  --------------------
  - Binary Search (bin_search.py)
  - Binary Search for upper and lower bounds (bounds.py)
  - Binary Search for functions on the real domain (real_bin_search.py)
  - Search for k-th ascending element in the array without sorting
  (split_find.py)
  - Ternary Search for real function extrema (ternary_search_extremum.py)
  ------------------
- Some other tools and algorithms
  ------------------
  - Dynamic programming solutions to different problems
  (dynamic_programming.py)
  - Visualization tool for matrixes (matrix_view.py)
  - Edit distances (edit_distance.py)

Linked List Module
======================

A module for implementing a one-way linked list data structure.

This module contains the `LinkedList` class, which represents a one-way
linked list data structure. The `LinkedList` class allows for the creation
and manipulation of a linked list, including appending, inserting, erasing,
and searching for elements.

Classes
-------
LinkedList
    A one-way linked list data structure.

<a id="python_solutions.LinkedList.Node"></a>

## Node

<a id="python_solutions.LinkedList.LinkedList"></a>

## LinkedList Objects

```python
class LinkedList()
```

Linked List Implementation.

The LinkedList class represents a one-way linked list data structure.
It allows for the creation and manipulation of a linked list, including
appending, inserting, erasing, and searching for elements.

## Attributes
- **head**: Node or None

    The first node of the linked list.

- **tail**: Node or None

    The last node of the linked list.

- **size**: int

    The number of elements in the linked list.

## Methods

__init__(self, head=None, tail=None) -> None
    Creates an instance of the LinkedList class.
    It is important to note, that if there already is some
    connection between head and tail nodes - this method will
    effectively parse it.

append(self, x) -> None
    Add an element to the end of the linked list.

insert(self, i, x) -> None
    Insert an element at a specific index.

erase(self, i) -> None
    Remove the element at a specific index.

__contains__(self, x) -> bool
    Check if an element exists in the linked list.

__iter__(self) -> Generator
    Iterate through the elements of the linked list.

list_all(self) -> List[]
    Return a list of all elements in the linked list.

__str__(self) -> str
    Return a string representation of the linked list.

__repr__(self) -> str
    Print method for the linked list.

<a id="python_solutions.LinkedList.LinkedList.__init__"></a>

#### \_\_init\_\_

```python
def __init__(head=None, tail=None)
```

Initialize a Linked List.

## Parameters
- **head**: Node or None, optional

    The first node of the linked list.
    Default is None.

- **tail**: Node or None, optional

    The last node of the linked list.
    Default is None.

## Returns

None

<a id="python_solutions.LinkedList.LinkedList.head"></a>

#### head

```python
@property
def head()
```

Get the head of the linked list.

## Returns

Node or None
    The head of the linked list.

<a id="python_solutions.LinkedList.LinkedList.head"></a>

#### head

```python
@head.setter
def head(head)
```

Set the head of the linked list.

## Parameters
- **head**: Node or None

    The new head of the linked list.

## Returns

None

<a id="python_solutions.LinkedList.LinkedList.tail"></a>

#### tail

```python
@property
def tail()
```

Get the tail of the linked list.

## Returns

Node or None
    The tail of the linked list.

<a id="python_solutions.LinkedList.LinkedList.tail"></a>

#### tail

```python
@tail.setter
def tail(tail)
```

Raise NotImplementedError when trying to set the tail.
The tail should be set through insert or initialization methods.

## Parameters
- **tail**: Node or None

    The new tail of the linked list.

## Raises

NotImplementedError
    When trying to set the tail directly.

<a id="python_solutions.LinkedList.LinkedList.size"></a>

#### size

```python
@property
def size()
```

Get the size of the linked list.

## Returns

int
    The size of the linked list.

<a id="python_solutions.LinkedList.LinkedList.size"></a>

#### size

```python
@size.setter
def size(size)
```

Raise NotImplementedError when trying to set the size.
The size is calculated automatically.

## Parameters
- **size**: int

    The new size of the linked list.

## Raises

NotImplementedError
    When trying to set the size directly.

<a id="python_solutions.LinkedList.LinkedList.__contains__"></a>

#### \_\_contains\_\_

```python
def __contains__(x)
```

Check if a given element is present in the linked list.

## Parameters
- **x**: any

    The element to check for in the linked list.

## Returns

bool
    True if the element is found, False otherwise.

<a id="python_solutions.LinkedList.LinkedList.__iter__"></a>

#### \_\_iter\_\_

```python
def __iter__()
```

Iterate through the elements of the linked list.

## Returns

generator
    A generator to iterate through the elements.

<a id="python_solutions.LinkedList.LinkedList.list_all"></a>

#### list\_all

```python
def list_all()
```

Return a list of all elements in the linked list.

## Returns

list
    A list containing all elements of the linked list.

<a id="python_solutions.LinkedList.LinkedList.__str__"></a>

#### \_\_str\_\_

```python
def __str__()
```

Return a string representation of the linked list.

## Returns

str
    A string representation of the linked list.

<a id="python_solutions.LinkedList.LinkedList.__repr__"></a>

#### \_\_repr\_\_

```python
def __repr__()
```

Return a string representation of the linked list.

## Returns

str
    A string representation of the linked list.

<a id="python_solutions.LinkedList.LinkedList.append"></a>

#### append

```python
def append(x)
```

Append an element to the end of the linked list.

## Parameters
- **x**: any

    The element to append to the linked list.

## Returns

None

<a id="python_solutions.LinkedList.LinkedList.search"></a>

#### search

```python
def search(i)
```

Search for nodes at a given index in the linked list.

## Parameters
- **i**: int

    The index at which to search for nodes.

## Returns

tuple
    A tuple containing the previous and current nodes.

<a id="python_solutions.LinkedList.LinkedList.insert"></a>

#### insert

```python
def insert(i, x)
```

Insert an element at a given index in the linked list.

## Parameters
- **i**: int

    The index at which to insert the element.

- **x**: any

    The element to insert into the linked list.

## Raises

IndexError
    When trying to insert with negative indexing.
    Negative indexing is an undefined operation.

## Returns

None

<a id="python_solutions.LinkedList.LinkedList.erase"></a>

#### erase

```python
def erase(i)
```

Remove an element at the specified index in the linked list.

## Parameters
- **i**: int

    The index at which to remove the element.

## Raises

IndexError
    If the index is out of bounds or negative.

## Returns

None

<a id="python_solutions.LinkedList.LinkedList.update"></a>

#### update

```python
def update(i, x)
```

Update the element at the specified index in the linked list.

## Parameters
- **i**: int

    The index at which to update the element.
- **x**: any

    The new value to assign to the element.

## Raises

IndexError
    If the index is negative.

## Returns

None

Array Counting Sort Module
==========================

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

Binary Search Module
====================

This module provides implementations of binary search algorithms
for searching a value within a sorted one-dimensional array of whole numbers.
- **Two implementations are available**: one with recursion and another

without recursion. The choice between the two depends on your
requirements for space efficiency and time complexity.

Functions
---------
bin_search(array: list[int], value_to_search: int, no_recursion=False)
    Binary search in a sorted array.

_bin_search(array, left_edge, right_edge, value_to_search)
    Helper function for binary search with recursion.

<a id="python_solutions.bin_search._bin_search"></a>

#### \_bin\_search

```python
def _bin_search(array, left_edge, right_edge, value_to_search)
```

This is the binary search with recursion implementation helper.

Binary search with recursion works on the cut,
so edges of the cut inside the array have to be provided.

## Parameters
- **array**: list[int]

    One-dimensional array consisting of whole numbers.

- **left_edge**: int

    Index inside the array meaning left edge of indexes
    inside array (itself included) where search will be performed.

- **right_edge**: int

    Index inside the array meaning right edge of indexes
    inside array (itself included) where search will be performed.

- **value_to_search**: int

    Value to be searched among the given indexes slice inside array.

## Returns

bool
    Whether searched value is inside the array

<a id="python_solutions.bin_search.bin_search"></a>

#### bin\_search

```python
def bin_search(array: list[int], value_to_search: int, no_recursion=False)
```

This function performs a binary search inside sorted array
consisting of whole numbers.
- **Time to work**: O(log2 of the size of the array) - best case


## Parameters
- **array**: list[int]

    One-dimensional array consisting of whole numbers
- **value_to_search**: int

- **Value to be searched inside the array
no_recursion**: bool

    Since binary search in general has two implementations,
    with or without recursion, this is the switcher between them.
    The no_recursion implementation requires exactly 3 variables
    which makes it very space efficient (O(1) to be exact),
    however time takes damage up to O(size of array).
    The recursion implementation requires space up to O(log2 of
    the size of the array), and time cuts up to the same value.

## Returns

bool
    Whether searched value is inside the array

Bloom Filter Module

====================
This module provides an implementation of a Bloom filter, a probabilistic
data structure used to check whether an item is a member of a set with a
certain probability of false positives. The Bloom filter is used
for efficient membership testing.

Functions
---------
hashlittle2(data, initval=0, initval2=0)
rot(x)
mix(a, b, c)
final(a, b, c)
hashlittle(data, initval=0)
    All functions above participate in calculating Jenkins hash of data
    using an optional seed.

Classes
-------
Bloom_filter(items_count=1000000, fp_prob=0.05, hashfunc='mmh3')
    Implements a Bloom filter data structure for efficient membership testing.

<a id="python_solutions.bloom_filter.math"></a>

## math

<a id="python_solutions.bloom_filter.mmh3"></a>

## mmh3

<a id="python_solutions.bloom_filter.bitarray"></a>

## bitarray

<a id="python_solutions.bloom_filter.rot"></a>

#### rot

```python
def rot(x, k)
```

<a id="python_solutions.bloom_filter.mix"></a>

#### mix

```python
def mix(a, b, c)
```

<a id="python_solutions.bloom_filter.final"></a>

#### final

```python
def final(a, b, c)
```

<a id="python_solutions.bloom_filter.hashlittle2"></a>

#### hashlittle2

```python
def hashlittle2(data, initval=0, initval2=0)
```

<a id="python_solutions.bloom_filter.hashlittle"></a>

#### hashlittle

```python
def hashlittle(data, initval=0)
```

This function calculates Jenkins hash of data using initval as seed.

It utilises rot(), mix(), final(), hashlittle() functions to
calculate Jenkins hash as a python translation of the author's
original C++ algorithm.

## Parameters
- **data**: any

    Object of class with defined __getitem__ method consisting
    of characters (which could be passed to ord() function)
- **initval**: int

    Seed for calculating hash
    Default value = 0

## Returns

int
    Jenkins hash of data

<a id="python_solutions.bloom_filter.Bloom_filter"></a>

## Bloom\_filter Objects

```python
class Bloom_filter()
```

This is an implementation of the Bloom filter data structure.

Bloom filter is used to determine whether passed object has
already been passed to it. It has a false positive outcome
probability which depends on the expected items count to be passed
and amount of hash functions available.
This particular implementation requires expected false positives
probability and items to be passed count and determines its size
and creates all hash functions on its own provided the algorithm
for function family.

## Attributes
- **fp_prob**: float

    False positives probability.
    Default value = 0.05

- **size**: int

    Real size of the structure, is calculated automatically

- **hash_count**: int

    Amount of hashes needed to redeem fp_prob given items_count,
    is calculated automatically provided with hashfunc family

- **bit_array**: bitarray

    Special structure imported from bitarray module, allows usage
    of only one byte per bucket, compared to unlimited memory for
    integer values inside lists, hence taking much less memory.
    Consists of either 0's or 1's and has a size of self.size.
    It is the main storage and the filter itself.
    Cannot be modified directly, modifies itself when new values
    pass through filter.

- **hashfunc**: string

    Family of algorithms for generating hash functions.
    Default value = 'mmh3' (murmur3 hash), possible value = 'jenkins'
    for Jenkins hash

## Methods

__init__(self, items_count: int = 1000000,
- **fp_prob**: float = 0.05, hashfunc: string = 'mmh3') -> None

    Creates an instance of Bloom filter.

add(self, item: any) -> None
    Passes through the Bloom filter given item.

check(self, item: any) -> Bloom_filter
    Checks whether the item was passed through Bloom filter.

get_size(self, items_count: int, fp_prob: float) -> int
    Calculates full size of the Bloom filter.

get_hash_count(self, size: int, items_count: int) -> int:
    Calculates the necessary amount of hash functions to ensure
    false positives probability with expected
    items to be passed count.

<a id="python_solutions.bloom_filter.Bloom_filter.__init__"></a>

#### \_\_init\_\_

```python
def __init__(items_count=1000000, fp_prob=0.05, hashfunc='mmh3')
```

Creates an instance of Bloom filter

## Parameters
- **items_count**: int

    Expected amount of items to be passed through filter.
    Default value = 1000000

- **fp_prob**: float

    Expected false positive outcome probability.
    Default value = 0.05

- **hashfunc**: 'mmh3' or 'jenkins'

    Name of the family of functions to use for hash functions
    generation.
    Default value = 'mmh3'

## Returns

None

<a id="python_solutions.bloom_filter.Bloom_filter.add"></a>

#### add

```python
def add(item)
```

Passes given item through Bloom filter.

## Parameters
- **item**: str or byte-like


## Returns

None

<a id="python_solutions.bloom_filter.Bloom_filter.check"></a>

#### check

```python
def check(item)
```

Checks whether the item was passed through the Bloom filter.

## Parameters
- **item**: str or byte-like


## Returns

bool
    True if the item was passed through, False if it was not.

<a id="python_solutions.bloom_filter.Bloom_filter.get_size"></a>

#### get\_size

```python
def get_size(items_count, fp_prob)
```

Calculates the size of bloom filter for its initialization.

## Parameters
- **items_count**: int

    Amount of items expected to be passed through.

- **fp_prob**: float

    False positive case probability

## Returns

int
    Size of the bloom filter.

<a id="python_solutions.bloom_filter.Bloom_filter.get_hash_count"></a>

#### get\_hash\_count

```python
def get_hash_count(size, items_count)
```

Calculates amount of hash functions necessary to assure
required false probability.

## Parameters
- **size**: int

    Calculated size of the bloom filter.

- **items_count**: int

    Amount of items expected to be passed through the filter.

## Returns

int
    Amount of hash functions to generate different hashes.

Binary Boundaries Search Module
===============================

This module provides implementations of lower_bound and upper_bound
search algorithms for finding the first and last occurrences of a given
whole-numbered value in a sorted array. The lower_bound algorithm returns
the index of the first encounter of the value, while the upper_bound algorithm
returns the index of the last encounter.

Functions
---------
lower_bound(array, value_to_search)
    Determines the index of the first encounter of the whole-numbered value
    in a sorted array.

upper_bound(array, value_to_search)
    Determines the index of the last encounter of the whole-numbered value
    in a sorted array.

<a id="python_solutions.bounds._lower_bound"></a>

#### \_lower\_bound

```python
def _lower_bound(array, left_edge, right_edge, value_to_search)
```

This is lower bound search helper.

Lower bound search works on the cut,
so edges of the cut inside the array have to be provided.
Array has to be sorted already, time and complexity equal
to the binary search with recursion.

## Parameters
- **array**: list[int]

    one-dimensional array consisting of whole numbers

- **left_edge**: int

    index inside the array meaning left edge of indexes
    inside array (itself included) where search will be performed

- **right_edge**: int

    index inside the array meaning right edge of indexes
    inside array (itself included) where search will be performed

- **value_to_search**: int

    value to be searched among the given indexes slice inside array

## Returns

int
    index there the lower bound with required value is located

<a id="python_solutions.bounds.lower_bound"></a>

#### lower\_bound

```python
def lower_bound(array, value_to_search)
```

This function determines where is first encounter of the whole-
numbered value.

This function utilizes algorithm working on the cut, hence the
searching job is delegated to the function-helper. The algorithm
itself is similar to the binary search without any additional
calculation complexity.
Array where is the value to be searched for has to be already sorted.
Function assumes by-default the presence of the value to be searched.

## Parameters
- **array**: list[int]

    Sorted array where to find the first encounter of the
    searched value.

- **value_to_search**: int

    Searched value which first encounter is to be found by the
    function.

## Returns

int
    index of the first encounter of the searched value

<a id="python_solutions.bounds.upper_bound"></a>

#### upper\_bound

```python
def upper_bound(array, value_to_search)
```

This function determines where is the last encounter of the whole-
numbered value.

This function is very similar to the lower_bound() except for it
searches for the last encounter. Generally, it is done via
lower_bound of the next (+1) whole value and subtraction 1 from the
returned index.

## Parameters
- **array**: list[int]

    Sorted array where to find the last encounter of the
    searched value.

- **value_to_search**: int

    Searched value which last encounter is to be found by the
    function.

## Returns

int
    index of the last encounter of the searched value

Binary Search Tree Module
=========================

This module defines a Binary Search Tree (BST) class that allows the
insertion, deletion, and search of elements. It also provides methods for
traversing the tree in-order, finding the minimum and maximum values, and
determining the successor and predecessor of a given element.

Classes
-------
TreeNode
    A class representing a node in the Binary Search Tree.

BinarySearchTree
    A class representing a Binary Search Tree.

<a id="python_solutions.bst.Node"></a>

## Node

<a id="python_solutions.bst.TreeNode"></a>

## TreeNode Objects

```python
class TreeNode(Node)
```

A class representing a node in the Binary Search Tree.
Also a basic class to inherit from for more complicated tree nodes.

## Attributes
- **left**: TreeNode | None, optional

    The left child of the node if present, else - None. Default is None.

- **right**: TreeNode | None, optional

    The right child of the node if present, else - None. Default is None.

<a id="python_solutions.bst.TreeNode.__init__"></a>

#### \_\_init\_\_

```python
def __init__(data: int | float) -> None
```

Initializes a new instance of the TreeNode class with the specified
data.

## Parameters
- **data**: int | float

    Data to be put into the TreeNode.

## Returns

None

<a id="python_solutions.bst.BinarySearchTree"></a>

## BinarySearchTree Objects

```python
class BinarySearchTree()
```

A class representing a Binary Search Tree.

## Attributes
- **root**: TreeNode | None

    The root node of the tree if exists, else None.

- **size**: int

    The size of the tree.

## Methods

__init__(self) -> None
    Initializes a new instance of the BinarySearchTree class.

insert(self, data: int | float) -> None
    Inserts a new element with the specified data into the Binary Search
    Tree.

_insert(self, root: TreeNode, new_node: TreeNode) -> None
    Recursively inserts a new node into the Binary Search Tree.

delete(self, data: int | float) -> None
    Deletes the node with the specified data from the Binary Search Tree.

_delete(self, node: TreeNode) -> None
    Recursively deletes the specified node from the Binary Search Tree.

search(self, data: int | float) -> TreeNode
    Searches for a node with the specified data in the Binary Search Tree.

_search(self, root: TreeNode, data: int | float) -> TreeNode
    Recursively searches for a node with the specified data in the
    Binary Search Tree.

in_order_traversal(self) -> list[int | float]
    Performs an in-order traversal of the Binary Search Tree and returns
    a list of elements.

_in_order_traversal_rec(self, root: TreeNode, result: list) -> None
    Recursively performs an in-order traversal of the Binary Search Tree.

find_min(self) -> int | float
    Finds the minimum value in the Binary Search Tree.

_min_value_node(self, node: TreeNode) -> TreeNode
    Finds the node with the minimum value in the Binary Search Tree.

find_max(self) -> int | float
    Finds the maximum value in the Binary Search Tree.

_max_value_node(self, node: TreeNode) -> TreeNode
    Finds the node with the maximum value in the Binary Search Tree.

find_successor(self, data: int | float) -> int | float
    Finds the successor of the node with the specified data in the
    Binary Search Tree.

find_predecessor(self, data: int | float) -> int | float
    Finds the predecessor of the node with the specified data in the
    Binary Search Tree.

is_empty(self) -> bool
    Checks if the Binary Search Tree is empty.

max_height(self) -> int
    Finds the maximum height of the tree.

local_tree(self, node: TreeNode, b: int = 2, deepness: int = 1)
    -> list[int | float]
    Returns the local tree with the node being root and the required
    deepness. Nodes' data is loaded into the list down from root from
    the left to the right. Deepness 1 equals root and its children.
    b is the order of the tree, for the binary it is 2.

<a id="python_solutions.bst.BinarySearchTree.__init__"></a>

#### \_\_init\_\_

```python
def __init__() -> None
```

Initializes a new instance of the BinarySearchTree class.

## Returns

None

<a id="python_solutions.bst.BinarySearchTree.insert"></a>

#### insert

```python
def insert(data: int | float) -> None
```

Inserts a new element with the specified data into the Binary
Search Tree.

## Parameters
- **data**: int | float

    The data to be inserted.

## Returns

None

<a id="python_solutions.bst.BinarySearchTree._insert"></a>

#### \_insert

```python
def _insert(root: TreeNode, new_node: TreeNode) -> None
```

Recursively inserts a new node into the Binary Search Tree.

## Parameters
- **root**: TreeNode

    Current TreeNode.

- **new_node**: TreeNode

    The node with the data to be inserted.

## Returns

None

<a id="python_solutions.bst.BinarySearchTree.delete"></a>

#### delete

```python
def delete(data: int | float) -> None
```

Deletes the node with the specified data from the Binary Search Tree.

## Parameters
- **data**: int | float

    The data which contains the node to be deleted.

## Returns

None

<a id="python_solutions.bst.BinarySearchTree._delete"></a>

#### \_delete

```python
def _delete(node: TreeNode) -> None
```

Recursively deletes the specified node from the Binary Search Tree.

## Parameters
- **node**: TreeNode

    The node to be deleted.

## Returns

None

<a id="python_solutions.bst.BinarySearchTree.search"></a>

#### search

```python
def search(data: int | float) -> TreeNode | None
```

Searches for a node with the specified data in the Binary Search Tree.
In case of value duplicate returns only one node at random.

## Parameters
- **data**: int | float

    The data which contains inside the node to be searched.

## Returns

TreeNode | None
    TreeNode containing the data required or None if such TreeNode
    was not found.

<a id="python_solutions.bst.BinarySearchTree._search"></a>

#### \_search

```python
def _search(root: TreeNode, data: int | float) -> TreeNode | None
```

Recursively searches for a node with the specified data in the
Binary Search Tree.

## Parameters
- **root**: TreeNode

    Current TreeNode.

- **data**: int | float

    The data which contains inside the node to be searched.

## Returns

TreeNode | None
    TreeNode containing the data required or None if such TreeNode
    was not found.

<a id="python_solutions.bst.BinarySearchTree.node_height"></a>

#### node\_height

```python
def node_height(node: TreeNode) -> int
```

Finds the height of the node with value.

## Parameters
- **value**: int

    Node data.

## Returns

int
    Node height.

<a id="python_solutions.bst.BinarySearchTree.in_order_traversal"></a>

#### in\_order\_traversal

```python
def in_order_traversal() -> list[int | float]
```

Performs an in-order traversal of the Binary Search Tree and returns
a list of elements.

## Returns

list[int | float]
    The list of elements in increasing order.

<a id="python_solutions.bst.BinarySearchTree._in_order_traversal_rec"></a>

#### \_in\_order\_traversal\_rec

```python
def _in_order_traversal_rec(root: TreeNode,
- **result**: list[int | float | None]) -> None

```

Recursively performs an in-order traversal of the Binary Search Tree.

## Parameters
- **root**: TreeNode

    Current TreeNode.

- **result**: list[int | float | None]

    The list to store result from traversal.

## Returns

None

<a id="python_solutions.bst.BinarySearchTree.find_min"></a>

#### find\_min

```python
def find_min() -> int | float | None
```

Finds the minimum value in the Binary Search Tree.

## Returns

int | float | None
    The min if it was found, None otherwise.

<a id="python_solutions.bst.BinarySearchTree._min_value_node"></a>

#### \_min\_value\_node

```python
def _min_value_node(node: TreeNode) -> TreeNode
```

Finds the node with the minimum value in the Binary Search Tree.

## Parameters
- **node**: TreeNode

    The root if the BST.

## Returns

TreeNode
    TreeNode containing the minimum value.

<a id="python_solutions.bst.BinarySearchTree.find_max"></a>

#### find\_max

```python
def find_max() -> int | float | None
```

Finds the maximum value in the Binary Search Tree.

## Returns

int | float | None
    The maximum value if it was found, None otherwise.

<a id="python_solutions.bst.BinarySearchTree._max_value_node"></a>

#### \_max\_value\_node

```python
def _max_value_node(node: TreeNode) -> TreeNode
```

Finds the node with the maximum value in the Binary Search Tree.

## Parameters
- **node**: TreeNode

    The root of the BST.

## Returns

TreeNode
    The node containing the maximum value.

<a id="python_solutions.bst.BinarySearchTree.find_successor"></a>

#### find\_successor

```python
def find_successor(data: int | float) -> int | float | None
```

Finds the successor of the node with the specified data in the
Binary Search Tree.

## Parameters
- **data**: int | float

    The data, successor to which is to be found.

## Returns

int | float | None
    The successor to the data.

<a id="python_solutions.bst.BinarySearchTree.find_predecessor"></a>

#### find\_predecessor

```python
def find_predecessor(data: int | float) -> int | float | None
```

Finds the predecessor of the node with the specified data in the
Binary Search Tree.

## Parameters
- **data**: int | float

    The data, predecessor to which is to be found.

## Returns

int | float | None
    The predecessor to the data.

<a id="python_solutions.bst.BinarySearchTree.is_empty"></a>

#### is\_empty

```python
def is_empty() -> bool
```

Checks if the Binary Search Tree is empty.

## Returns

bool
    True if the BST is empty, False otherwise.

<a id="python_solutions.bst.BinarySearchTree.max_height"></a>

#### max\_height

```python
def max_height() -> int
```

The maximum height of the tree.

## Returns

int
    The height of the tree.

<a id="python_solutions.bst.BinarySearchTree.local_tree"></a>

#### local\_tree

```python
def local_tree(node: TreeNode,
- **b**: int = 2,

- **deepness**: int = 1) -> list[int | float]

```

Returns the local tree with the node being root and the required
deepness. Nodes' data is loaded into the list down from root from
the left to the right. Deepness 1 equals root and its children.
b is the order of the tree, for binary it is 2.

## Parameters
- **node**: TreeNode

    Node to be considered the root one.

- **b**: int

    The order of the tree. Default is 2.

- **deepness**: int

    The deepness of the local tree.

## Returns

list[int | float]
    List containing the tree nodes' data.

Counting Sort Module
====================

This module provides an implementation of the counting sort algorithm
for sorting an array of whole numbers.

The counting sort algorithm counts the occurrences of each whole number
in the input array and uses this information to create a sorted array.
It is particularly efficient when the range of values is small compared
to the array size.

Functions
---------
count_sort(array: list[int]) -> list[int]
    Sorts an array of whole numbers using the counting sort algorithm.

<a id="python_solutions.count_sort.count_sort"></a>

#### count\_sort

```python
def count_sort(array: list[int]) -> list[int]
```

This function implements counting sort on the array of whole numbers.

The algorithm of counting sort employs the basic counting
of the whole numbers inside array. It creates another array with
(max - min + 1) size, and counts, how many elements with each number
are inside the array to be sorted.
- **Time to work**: O(size of array + difference between the biggest and

the smallest elements)

## Parameters
- **array**: list[int]

    array to be sorted consisting of whole numbers

## Returns

list[int]
    sorted array

Cyclic Linked List Module
=========================

This module defines a cyclic linked list, which is a variation of a linked list
where the tail node is connected to the head node, creating a closed loop.

Classes
-------
CyclicLinkedList
    Represents a cyclic linked list and provides additional
    methods and behavior specific to cyclic linked lists.

<a id="python_solutions.CyclicLinkedList.DoubleNode"></a>

## DoubleNode

<a id="python_solutions.CyclicLinkedList.LinkedList"></a>

## LinkedList

<a id="python_solutions.CyclicLinkedList.CyclicLinkedList"></a>

## CyclicLinkedList Objects

```python
class CyclicLinkedList(LinkedList)
```

Represents a cyclic linked list, which is a variation of a linked list
where the tail node is connected to the head node, creating a closed loop.

This class inherits from the LinkedList class and provides additional
methods and behavior specific to cyclic linked lists. This means that
operations like list traversal and iteration will continue
indefinitely in a loop.

## Attributes
- **_head**: DoubleNode or None

    The head node of the cyclic linked list. Default is None.

- **_tail**: DoubleNode or None

    The tail node of the cyclic linked list. Default is None.

- **_size**: int

    The number of elements in the cyclic linked list. Default is None.

## Methods

__init__(self, head=None, tail=None) -> None
    Initializes empty cyclic linked list.

list_all(self) -> List[Unknown]
    Returns a list containing all the elements in the cyclic linked list.

search(self, i) -> tuple(DoubleNode | None, DoubleNode | None)
    Searches for the i-th element in the cyclic linked list and returns
    the previous and current nodes before the i-th element.

insert(self, i, x) -> None
    Inserts a new element x at the specified index i in
    the cyclic linked list.

erase(self, i) -> None
    Removes the element at the specified index i from
    the cyclic linked list.

update(self, i, x) -> None
    Updates the element at the specified index i in
    the cyclic linked list with x.

<a id="python_solutions.CyclicLinkedList.CyclicLinkedList.__init__"></a>

#### \_\_init\_\_

```python
def __init__(head=None, tail=None)
```

Initializes an empty cyclic linked list.

## Parameters
- **head**: DoubleNode or None, optional

    The head node of the cyclic linked list. Default is None.

- **tail**: DoubleNode or None, optional

    The tail node of the cyclic linked list. Default is None.

## Returns

None

<a id="python_solutions.CyclicLinkedList.CyclicLinkedList.list_all"></a>

#### list\_all

```python
def list_all()
```

Returns a list containing all the elements in the cyclic linked list.

## Returns

List[Unknown]
    A list containing all the elements in the cyclic linked list.

<a id="python_solutions.CyclicLinkedList.CyclicLinkedList.search"></a>

#### search

```python
def search(i)
```

Searches for the i-th element in the cyclic linked list and returns
the node before the i-th element (previous)
and the node with i-th element (current).

## Parameters
- **i**: int

    The index of the element to search for.

## Returns

tuple(DoubleNode | None, DoubleNode | None)
    A tuple containing the previous and current nodes if they exist.

<a id="python_solutions.CyclicLinkedList.CyclicLinkedList.insert"></a>

#### insert

```python
def insert(i, x)
```

Inserts a new element x at the specified index i
in the cyclic linked list.

## Parameters
- **i**: int

    The index at which to insert the new element.

- **x**: Unknown

    The element to insert.

## Returns

None

<a id="python_solutions.CyclicLinkedList.CyclicLinkedList.erase"></a>

#### erase

```python
def erase(i)
```

Removes the element at the specified index i
from the cyclic linked list.

## Parameters
- **i**: int

    The index of the element to remove.

## Returns

None

<a id="python_solutions.CyclicLinkedList.CyclicLinkedList.update"></a>

#### update

```python
def update(i, x)
```

Updates the element at the specified index i
in the cyclic linked list with x.

## Parameters
- **i**: int

    The index of the element to update.

- **x**: Unknown

    The new value to update the element with.

## Returns

None

Deque Module
============

This module defines a Double-ended Queue (Deque) class, which represents
a data structure that allows elements to be added or removed from both ends.

Classes
-------
Deque
    Represents a Double-ended Queue (Deque) and provides methods for adding,
    removing, and accessing elements from both ends.

<a id="python_solutions.Deque.DoubleNode"></a>

## DoubleNode

<a id="python_solutions.Deque.Stack"></a>

## Stack

<a id="python_solutions.Deque.Queue"></a>

## Queue

<a id="python_solutions.Deque.Deque"></a>

## Deque Objects

```python
class Deque(Queue, Stack)
```

Double-ended Queue (Deque) Class

The Deque class represents a double-ended queue,
which is a data structure that allows elements
to be added or removed from both ends.

## Attributes

Inherits attributes from Queue and Stack classes.

## Methods

push_back(self, value)
    Add an element to the back (left) end of the deque,
    equivalent to enqueue in a queue.

pop_front(self)
    Remove and return the element from the front (right) end of the deque,
    equivalent to dequeue in a queue.

pop_back(self)
    Remove and return the element from the back (left) end of the deque,
    equivalent to pop in a stack.

push_front(self, value)
    Add an element to the front (right) end of the deque.

<a id="python_solutions.Deque.Deque.push_back"></a>

#### push\_back

```python
def push_back(value)
```

Add an element to the back (left) end of the deque.

## Parameters
- **value**: any

    The element to be added to the deque.

## Returns

None

<a id="python_solutions.Deque.Deque.pop_front"></a>

#### pop\_front

```python
def pop_front()
```

Remove and return the element from the front (right) end of the deque.

## Returns

any
    The element removed from the front of the deque.

<a id="python_solutions.Deque.Deque.pop_back"></a>

#### pop\_back

```python
def pop_back()
```

Remove and return the element from the back (left) end of the deque.

## Returns

any
    The element removed from the back of the deque.

<a id="python_solutions.Deque.Deque.push_front"></a>

#### push\_front

```python
def push_front(value)
```

Add an element to the front (right) end of the deque.

## Parameters
- **value**: any

    The element to be added to the front of the deque.

## Returns

None

Digit Sort
==================================

This module provides functions for performing digit sort, a sorting algorithm
specifically designed for integers.

Functions
---------
digit_sort(array: list[int], base: int = 10) -> list[int]
    Sort a list of non-negative integers using the digit sort algorithm.

to_m_based(number: int, base: int) -> list[int]
    Convert a decimal number to an M-based representation.

restore_to_nums(array: list[int], base: int = 10) -> int
    Restore an M-based representation to its decimal form.

<a id="python_solutions.digit_sort.two_dim_array_count_sort"></a>

## two\_dim\_array\_count\_sort

<a id="python_solutions.digit_sort.to_m_based"></a>

#### to\_m\_based

```python
def to_m_based(number: int, base: int) -> list[int]
```

Convert a decimal number to an M-based representation.

This function converts a decimal number into its M-based
representation, where M is the specified base. The result
is returned as a list of digits in the M-based representation.
Optionally, you can choose to return the result as an array or
restore it to its original decimal form.

## Parameters
- **number**: int

    The decimal number to be converted to an M-based representation.

- **base**: int

    The base (M) to which the number should be converted. It must be
    a positive integer greater than or equal to 2.

## Returns

list[int]
    A list of integers representing the M-based representation
    of the decimal number.

<a id="python_solutions.digit_sort.restore_to_nums"></a>

#### restore\_to\_nums

```python
def restore_to_nums(array: list[int], base: int = 10) -> int
```

Restore an M-based representation to its decimal form.

This function takes a list of digits representing an M-based
representation and restores it to its original decimal form.
You can specify the base (M) used for the representation,
which defaults to 10 for decimal restoration.

## Parameters
- **array**: list[int]

    A list of digits representing an M-based number.

- **base**: int, optional

    The base (M) used for the M-based representation.
    It must be a positive integer greater than or equal to 2.
    The default value is 10 for decimal restoration.

## Returns

int
    The decimal number restored from the M-based representation.

<a id="python_solutions.digit_sort.digit_sort"></a>

#### digit\_sort

```python
def digit_sort(array: list[int], base: int = 10) -> list[int]
```

This function performs digit sort on a list of non-negative integers.

Digit sort is a sorting algorithm that works specifically for
non-negative integers. It sorts the integers by their individual
digits, starting from the least significant digit to the most
significant digit. This algorithm has a time complexity of O(n * k),
where n is the number of integers in the input list and k is
the maximum number of digits in any integer inside array.
It is important that the amount of digits can be reduced by
changing the base for the integers. Hence, when k = 1 this sort
appears to be counting sort with O(n) time complexity.

## Parameters
- **array**: list[int]

    A list of non-negative integers to be sorted using digit sort.
- **base**: int

    The array's integers' base depending on which number of digits
    will be determined.

## Returns

list[int]
    A sorted list of non-negative integers.

<a id="python_solutions.digit_sort.digit_sort_opt"></a>

#### digit\_sort\_opt

```python
def digit_sort_opt(array: list[int], base: int = 10) -> list[int]
```

Sort a list of non-negative integers using the digit + radix sort
algorithm.

## Parameters
- **array**: list[int]

    A list of non-negative integers to be sorted using digit sort.
- **base**: int

    The array's integers' base depending on which number of digits
    will be determined.

## Returns

list[int]
    A sorted list of non-negative integers.

<a id="python_solutions.docs.docs.os"></a>

## os

<a id="python_solutions.docs.docs.re"></a>

## re

<a id="python_solutions.docs.docs.Path"></a>

## Path

<a id="python_solutions.docs.docs.Context"></a>

## Context

<a id="python_solutions.docs.docs.PythonLoader"></a>

## PythonLoader

<a id="python_solutions.docs.docs.MarkdownRenderer"></a>

## MarkdownRenderer

<a id="python_solutions.docs.docs.NumpyProcessor"></a>

## NumpyProcessor

<a id="python_solutions.docs.docs.directory"></a>

#### directory

<a id="python_solutions.docs.docs.directory"></a>

#### directory

<a id="python_solutions.docs.docs.context"></a>

#### context

<a id="python_solutions.docs.docs.loader"></a>

#### loader

<a id="python_solutions.docs.docs.renderer"></a>

#### renderer

<a id="python_solutions.docs.docs.modules"></a>

#### modules

<a id="python_solutions.docs.docs.string"></a>

#### string

<a id="python_solutions.docs.docs.format_section_title"></a>

#### format\_section\_title

```python
def format_section_title(title)
```

Formats section titles to Markdown headers.

<a id="python_solutions.docs.docs.format_items"></a>

#### format\_items

```python
def format_items(section)
```

Format items within sections to list or table format if applicable.

<a id="python_solutions.docs.docs.process_docstring"></a>

#### process\_docstring

```python
def process_docstring(docstring)
```

Convert docstring sections to Markdown format.

<a id="python_solutions.docs.docs.render_markdown"></a>

#### render\_markdown

```python
def render_markdown(file_content)
```

Converts entire file of plain docstrings to Markdown format.

<a id="python_solutions.docs.docs.string"></a>

#### string

<a id="python_solutions.docs.docs.module_pattern"></a>

#### module\_pattern

<a id="python_solutions.docs.docs.modules"></a>

#### modules

<a id="python_solutions.docs.docs.output_dir"></a>

#### output\_dir

Two-Way Linked List Node
============================================

This module provides a DoubleNode class representing a node in a two-way linked
list, and a helper function `prev()` to access the previous node similar to
the built-in `next()` function.

Classes
-------
DoubleNode
    A class representing a node in a two-way linked list with access to both
    the next and previous nodes.

Functions
---------
prev(obj: object with defined prev() method) -> any
    Retrieve the previous object connected to the given DoubleNode object or
    return None if there is no previous object.

<a id="python_solutions.DoubleNode.Node"></a>

## Node

<a id="python_solutions.DoubleNode.prev"></a>

#### prev

```python
def prev(obj)
```

Function-helper for easier calling for previous DoubleNode.

Works as analog for built-in function next().
This function retrieves the previous node connected
to the given DoubleNode object or returns None if
there is no previous node.

## Parameters
- **obj**: object with defined prev() method

    Object for which to retrieve the previous object.

## Returns

any
    The previous object or None if no previous object exists.

<a id="python_solutions.DoubleNode.DoubleNode"></a>

## DoubleNode Objects

```python
class DoubleNode(Node)
```

Two-Way Linked List Node Class

The DoubleNode class represents a node in a two-way linked list.
It has the same functionality as a regular Node, but it can also
access the previous node stored into the added attribute
using the prev() method.

## Attributes

Inherits attributes from the Node class.

## Methods

__init__(self, data=None, prev_node=None, next_node=None)
    Initialize a DoubleNode object.

prev(self)
    Get the previous node of the DoubleNode.

<a id="python_solutions.DoubleNode.DoubleNode.__init__"></a>

#### \_\_init\_\_

```python
def __init__(data=None, prev_node=None, next_node=None)
```

Initialize a DoubleNode object with optional data,
previous node, and next node.

## Parameters
- **data**: any, optional

    The data to be stored in the DoubleNode. Default is None.
- **prev_node**: DoubleNode or None, optional

    The previous node in the linked list. Default is None.
- **next_node**: DoubleNode or None, optional

    The next node in the linked list. Default is None.

## Returns

None

## Raises

TypeError
    If the provided prev_node or next_node is of the wrong type.

<a id="python_solutions.DoubleNode.DoubleNode.prev_node"></a>

#### prev\_node

```python
@property
def prev_node()
```

Get the previous node of the DoubleNode.

## Returns

DoubleNode or None
    The previous DoubleNode object or None if no previous node exists.

<a id="python_solutions.DoubleNode.DoubleNode.prev_node"></a>

#### prev\_node

```python
@prev_node.setter
def prev_node(prev_node)
```

Set the previous node of the DoubleNode.

## Parameters
- **prev_node**: DoubleNode or None

    The previous node to be set for the DoubleNode.

## Raises

TypeError
    If the provided prev_node is of the wrong type.

<a id="python_solutions.DoubleNode.DoubleNode.prev"></a>

#### prev

```python
def prev()
```

This method is defined for providing the same access option
for the previous node as for the next node
(to make possible the same call as for built-in function)

## Parameters
- **prev_node**: DoubleNode or None

    The previous node to be set for the DoubleNode.

## Raises

TypeError
    If the provided prev_node is of the wrong type.

<a id="python_solutions.dynamic_programming.WeightedGraph"></a>

## WeightedGraph

<a id="python_solutions.dynamic_programming.DynamicProgrammingProblem"></a>

## DynamicProgrammingProblem Objects

```python
class DynamicProgrammingProblem()
```

Base class for dynamic programming problems.

## Attributes
- **dp**: list[Unknown]

    Dynamic programming memory. Can be an array of anything or multiple
    arrays depending on the problem requirements

## Methods

solve(self) -> None
    Subclasses must implement this method.

<a id="python_solutions.dynamic_programming.DynamicProgrammingProblem.__init__"></a>

#### \_\_init\_\_

```python
def __init__()
```

Creates an instance of the DynamicProgrammingProblem class

## Returns

None

<a id="python_solutions.dynamic_programming.DynamicProgrammingProblem.solve"></a>

#### solve

```python
def solve()
```

Subclasses must implement this method to solve a specific problem.

## Raises

NotImplementedError
    Raised to indicate that this method should be overridden in
    subclasses.

<a id="python_solutions.dynamic_programming.KnapsackProblem"></a>

## KnapsackProblem Objects

```python
class KnapsackProblem(DynamicProgrammingProblem)
```

Class for solving the Knapsack problem using dynamic programming.

Knapsack problem is an optimization problem. It can be described the
next way. You have a set of items, each with a weight and a value, and you
have a knapsack with a maximum weight capacity. The goal is to determine
the combination of items to include in the knapsack that maximizes the
total value while not exceeding the weight capacity.
Dynamic programming offers an option to solve this problem within O(n*w)
time where n - amount of items, w - knapsack capacity. Since this is
well-known NP-hard problem, usual time to solve is O(2**n).

## Attributes
- **weights**: list[int]

    Array of weights for the knapsack problem.

- **values**: list[int]

    Array of values for the knapsack problem.

- **capacity**: int

    Capacity of the knapsack.

## Methods

solve(self) -> int
    Solves the Knapsack problem and returns the maximum value.

<a id="python_solutions.dynamic_programming.KnapsackProblem.__init__"></a>

#### \_\_init\_\_

```python
def __init__(weights, values, capacity)
```

Creates an instance of the KnapsackProblem class

## Parameters
- **weights**: list[int]

    Array of weights for the knapsack problem.

- **values**: list[int]

    Array of values for the knapsack problem.

- **capacity**: int

    Capacity of the knapsack.

## Returns

None

<a id="python_solutions.dynamic_programming.KnapsackProblem.solve"></a>

#### solve

```python
def solve()
```

Solves the Knapsack problem using dynamic programming.

## Returns

int
    The maximum value that can be obtained.

<a id="python_solutions.dynamic_programming.LongestCommonSubsequence"></a>

## LongestCommonSubsequence Objects

```python
class LongestCommonSubsequence(DynamicProgrammingProblem)
```

Class for finding the Longest Common Subsequence (LCS) of two strings.

This problem has a naive solution with time complexity O(2**n) where n is
the length of the longest string. Dynamic programming offers solution
with O(n^2) time complexity, where n and m are the length of strings.

## Attributes
- **str1**: str

    First string of the two to find LCS for.

- **str2**: str

    Second string of the two to find LCS for.

## Methods

solve(self) -> int
    Finds the LCS of the two input strings.

<a id="python_solutions.dynamic_programming.LongestCommonSubsequence.__init__"></a>

#### \_\_init\_\_

```python
def __init__(str1, str2)
```

Creates an instance of the LongestCommonSubsequence class

## Parameters
- **str1**: str

    First string of the two to find LCS for.

- **str2**: str

    Second string of the two to find LCS for.

## Returns

None

<a id="python_solutions.dynamic_programming.LongestCommonSubsequence.solve"></a>

#### solve

```python
def solve()
```

Finds the Longest Common Subsequence (LCS) of two strings.

## Returns

int
    The length of the LCS.

<a id="python_solutions.dynamic_programming.DamerauLevensteinDistance"></a>

## DamerauLevensteinDistance Objects

```python
class DamerauLevensteinDistance(DynamicProgrammingProblem)
```

Class for calculating the Damerau-Levenshtein distance
between two strings using dynamic programming.

Damerau-Levenshtein distance is the option for the edit distance
between two strings. It calculates the difference based on the amount
of 4 operations needed to convert the first string to the second.
These are insertion, deletion, substitution and transposition. It is
important to note that transpositions are made only between adjacent
characters.

## Attributes
- **str1**: str

    First string of the two to find LCS for.

- **str2**: str

    Second string of the two to find LCS for.

## Methods

solve(self) -> int
    Calculates the Damerau-Levenshtein distance between the two input
    strings.

solve_optimized(self) -> int

<a id="python_solutions.dynamic_programming.DamerauLevensteinDistance.__init__"></a>

#### \_\_init\_\_

```python
def __init__(str1, str2)
```

Creates an instance of the DamerauLevensteinDistance class

## Parameters
- **str1**: str

    First string of the two to find DLD for.

- **str2**: str

    Second string of the two to find DLD for.

## Returns

None

<a id="python_solutions.dynamic_programming.DamerauLevensteinDistance.solve"></a>

#### solve

```python
def solve()
```

Calculates the Damerau-Levenshtein distance between the two input
strings.

## Returns

int
    The Damerau-Levenshtein distance.

<a id="python_solutions.dynamic_programming.DamerauLevensteinDistance.solve_optimized"></a>

#### solve\_optimized

```python
def solve_optimized()
```

Calculates the Damerau-Levenshtein distance between the two input
strings with dynamic programming memory reduced to O(m) instead of
O(m*n), where
m - the length of the longest string,
n - the length of the shortest string.

## Returns

int
    The Damerau-Levenshtein distance.

<a id="python_solutions.dynamic_programming.LongestIncreasingSubsequence"></a>

## LongestIncreasingSubsequence Objects

```python
class LongestIncreasingSubsequence(DynamicProgrammingProblem)
```

Class for finding the length of the Longest Increasing Subsequence (LIS)
in a list of numbers using dynamic programming.

This problem has a naive solution with time complexity O(2**n) where n is
the length of the longest string. Dynamic programming offers solution
with O(n^2) time complexity, where n and m are the length of strings.

## Attributes
- **nums**: list[float]

    The list where LIS will be determined and its length found.

## Methods

solve(self) -> int
    Finds the length of the Longest Increasing Subsequence (LIS).

<a id="python_solutions.dynamic_programming.LongestIncreasingSubsequence.__init__"></a>

#### \_\_init\_\_

```python
def __init__(nums)
```

Creates an instance of the LongestIncreasingSubsequence class

## Parameters
- **nums**: list[float]

    The list where to find the length of the LIS.

## Returns

None

<a id="python_solutions.dynamic_programming.LongestIncreasingSubsequence.solve"></a>

#### solve

```python
def solve()
```

Finds the length of the Longest Increasing Subsequence (LIS)
in the list of numbers.

## Returns

int
    The length of the Longest Increasing Subsequence.

<a id="python_solutions.dynamic_programming.LongestIncreasingSubsequence.solve_optimized"></a>

#### solve\_optimized

```python
def solve_optimized()
```

Finds the length of the Longest Increasing Subsequence (LIS)
in the list of numbers with time of work reduced from O(n^2) to
O(n*logn) by using binary search.

## Returns

int
    The length of the Longest Increasing Subsequence.

<a id="python_solutions.dynamic_programming.maxSubarraySum"></a>

## maxSubarraySum Objects

```python
class maxSubarraySum(DynamicProgrammingProblem)
```

This class provides a solution to the Maximum Subarray Sum problem
using Mo's algorithm and dynamic programming. It allows you to find
the maximum sum of a subarray within a given array for multiple
queries.

## Attributes
- **arr**: list[int]

    The input array for which maximum subarray sums will be
    calculated.

- **queries**: list[tuple]

    A list of queries, each represented as a tuple (l, r) where
    l and r are the left and right endpoints of the subarray to
    consider.

## Methods

solve(self, arr: list[int]) -> int
    Solves the Maximum Subarray Sum problem for each query in the
    sorted order of left endpoints and returns the maximum subarray
    sum for each query using Mo's algorithm.

solve_optimized(self) -> int
    Solves the Maximum Subarray Sum problem for each query in the
    sorted order of left endpoints and returns the maximum subarray
    sum for each query using dynamic programming.

<a id="python_solutions.dynamic_programming.maxSubarraySum.__init__"></a>

#### \_\_init\_\_

```python
def __init__(arr, queries)
```

Initializes a new maxSubarraySum instance with the provided input
array and a list of queries.

## Parameters
- **arr**: list[int]

    The input array for which maximum subarray sums will be
    calculated.

- **queries**: list[tuple]

    A list of queries, each represented as a tuple (l, r) where l
    and r are the left and right endpoints of the subarray to
    consider.

## Returns

None

<a id="python_solutions.dynamic_programming.maxSubarraySum.solve_optimized"></a>

#### solve\_optimized

```python
def solve_optimized()
```

Solves the Maximum Subarray Sum problem for each query in the sorted
order of left endpoints using dynamic programming. Time complexity
is O(Q), space complexity is O(array length).

## Returns

list[int]
    A list of maximum subarray sums for each query.

<a id="python_solutions.dynamic_programming.maxSubarraySum.solve"></a>

#### solve

```python
def solve(arr)
```

Solves the Maximum Subarray Sum problem for each query in an
optimized manner using Mo's algorithm.

The time complexity of this method is O(Q * sqrt(N)) for Q queries,
where N is the length of the input array.
This is because, in the worst case, each query requires
O(sqrt(N)) operations to adjust the pointers.
The space complexity of this method is O(1),
since it requires nothing, but 4 pointers and 2 variables for
storing sums.

## Returns

int
    The maximum subarray sum among queries.

<a id="python_solutions.dynamic_programming.TravellingSalesmanProblem"></a>

## TravellingSalesmanProblem Objects

```python
class TravellingSalesmanProblem(DynamicProgrammingProblem)
```

<a id="python_solutions.dynamic_programming.TravellingSalesmanProblem.__init__"></a>

#### \_\_init\_\_

```python
def __init__(cities, edges)
```

<a id="python_solutions.dynamic_programming.TravellingSalesmanProblem.solve"></a>

#### solve

```python
def solve()
```

Edit Distance Calculation Module
============================================

This module provides functions to calculate the edit distance between two
strings using different distance metrics. It includes functions for Hamming
distance, Jaro similarity, and uses the Longest Common Subsequence and
Damerau-Levenshtein distance algorithms for more complex edit distance
calculations.

Functions
---------
edit_distance(str1: str, str2: str, distance: str = 'dl') -> float
    Compute the edit distance between two strings using a specified distance
    metric.

hamming_distance(str1: str, str2: str) -> int
    Calculate the Hamming distance between two strings.

jaro_distance(str1: str, str2: str) -> float
    Calculate the Jaro similarity between two strings.

<a id="python_solutions.edit_distance.LongestCommonSubsequence"></a>

## LongestCommonSubsequence

<a id="python_solutions.edit_distance.DamerauLevensteinDistance"></a>

## DamerauLevensteinDistance

<a id="python_solutions.edit_distance.edit_distance"></a>

#### edit\_distance

```python
def edit_distance(str1, str2, distance='dl')
```

Compute the edit distance between two strings.

This function calculates the edit distance between two input strings
using one of the available distance metrics. You can choose the
- **following metrics**: Jaro, Hamming, LongestCommonSubsequence or

DamerauLevensteinDistance.

DamerauLevensteinDistance is the most universal of them.
Jaro distance can be the metric for the distance between the strings
containing matching and transposing characters.
LongestCommonSubsequence distance is a metric for edit distance, using
the length of LCS of the strings.
Hamming distance works only for the strings with the same length and
share a large share of characters (including their positions), e.g.
'karoline' and 'kathrine'.

## Parameters
- **str1**: str

    The first input string.

- **str2**: str

    The second input string.

- **distance**: str, optional

    The distance metric to use. Possible values are
    'jaro' for Jaro distance,
    'hamming' for Hammimg distance,
    'lcs' for distance based on the LongestCommonSubsequence or
    'dl' for DamerauLevensteinDistance.
    Default is 'dl'.

## Returns

float
    The computed edit distance based on the selected distance metric.

## Raises

ValueError
    Raised if the distance is 'hamming' and the input strings have
    different lengths.

<a id="python_solutions.edit_distance.hamming_distance"></a>

#### hamming\_distance

```python
def hamming_distance(str1, str2)
```

Calculate the Hamming distance between two strings.

The Hamming distance is the number of positions at which the
corresponding elements in the input strings of the same length are
different.

## Parameters
- **str1**: str

    The first input string.

- **str2**: str

    The second input string.

## Returns

int
    The Hamming distance between the two input strings.

## Raises

ValueError
    Raised if the input strings have different lengths.

<a id="python_solutions.edit_distance.jaro_distance"></a>

#### jaro\_distance

```python
def jaro_distance(str1, str2)
```

Calculate the Jaro similarity between two strings.

The Jaro similarity measures the similarity between two strings.
A higher value indicates more similarity between the strings.
- **The general formula looks the following way**: d = (matches / length1 + matches / length2 + (matches - transpositions)

/ matches) / 3, where
matches are matches of the characters in the strings if they are not
not farther than int(max(length1, length2) / 2) - 1 characters apart,
length1 and length2 are lengths of the first and the second strings
accordingly,
transpositions is the number of matching characters that are not in the
right order.

## Parameters
- **str1**: str

    The first input string.

- **str2**: str

    The second input string.

## Returns

float
    The Jaro similarity between the two input strings.

<a id="python_solutions.graph.heapq"></a>

## heapq

<a id="python_solutions.graph.logging"></a>

## logging

<a id="python_solutions.graph.deque"></a>

## deque

<a id="python_solutions.graph.GraphNode"></a>

## GraphNode

<a id="python_solutions.graph.Edge"></a>

## Edge

<a id="python_solutions.graph.VerticesList"></a>

## VerticesList Objects

```python
class VerticesList(dict)
```

<a id="python_solutions.graph.VerticesList.__init__"></a>

#### \_\_init\_\_

```python
def __init__()
```

<a id="python_solutions.graph.VerticesList.append"></a>

#### append

```python
def append(__object) -> None
```

<a id="python_solutions.graph.VerticesList.__getitem__"></a>

#### \_\_getitem\_\_

```python
def __getitem__(index)
```

<a id="python_solutions.graph.VerticesList.__iter__"></a>

#### \_\_iter\_\_

```python
def __iter__()
```

<a id="python_solutions.graph.VerticesList.__delitem__"></a>

#### \_\_delitem\_\_

```python
def __delitem__(index)
```

<a id="python_solutions.graph.Graph"></a>

## Graph Objects

```python
class Graph()
```

<a id="python_solutions.graph.Graph.__init__"></a>

#### \_\_init\_\_

```python
def __init__()
```

<a id="python_solutions.graph.Graph.all_vertices"></a>

#### all\_vertices

```python
def all_vertices()
```

<a id="python_solutions.graph.Graph.add_vertex"></a>

#### add\_vertex

```python
def add_vertex(*args, **kwargs)
```

<a id="python_solutions.graph.Graph._find_arg"></a>

#### \_find\_arg

```python
def _find_arg(default, arg_dict: dict[int, str], *args, **kwargs)
```

<a id="python_solutions.graph.Graph._find_index"></a>

#### \_find\_index

```python
def _find_index(**kwargs)
```

<a id="python_solutions.graph.Graph.remove_vertex"></a>

#### remove\_vertex

```python
def remove_vertex(**kwargs)
```

<a id="python_solutions.graph.Graph.add_edge"></a>

#### add\_edge

```python
def add_edge(u: int, v: int, *args, **kwargs)
```

<a id="python_solutions.graph.Graph.remove_edge"></a>

#### remove\_edge

```python
def remove_edge(u: int, v: int)
```

<a id="python_solutions.graph.Graph.bfs"></a>

#### bfs

```python
def bfs(start, target=None)
```

<a id="python_solutions.graph.Graph.to_adjacency_matrix"></a>

#### to\_adjacency\_matrix

```python
def to_adjacency_matrix()
```

<a id="python_solutions.graph.Graph.calculate_element"></a>

#### calculate\_element

```python
def calculate_element(vertex, neighbor)
```

<a id="python_solutions.graph.Graph.topological_sort_util"></a>

#### topological\_sort\_util

```python
def topological_sort_util(vertex, visited, stack)
```

<a id="python_solutions.graph.Graph.topological_sort"></a>

#### topological\_sort

```python
def topological_sort()
```

<a id="python_solutions.graph.Graph.tarjan_dfs"></a>

#### tarjan\_dfs

```python
def tarjan_dfs(vertex, index, stack, low_link, on_stack, scc)
```

<a id="python_solutions.graph.Graph.scc"></a>

#### scc

```python
def scc()
```

<a id="python_solutions.graph.Graph.kosaraju_scc"></a>

#### kosaraju\_scc

```python
def kosaraju_scc()
```

Finds strongly connected components in the given directed graph
using Kosaraju's algorithm.

- **Args**: - graph (DirectedGraph): The directed graph for which to find SCCs.


- **Returns**: - List[List[int]]: A list of lists, where each inner list contains

the indices of nodes that form a strongly connected component.

<a id="python_solutions.graph.Graph.fill_order"></a>

#### fill\_order

```python
def fill_order(vertex, visited, stack)
```

Utility function for DFS and to fill the stack with vertices
based on their finishing times (meaning the time when all not visited
vertices accessible from this vertex by transitions with direction 1
become visited).

- **Args**: - graph (DirectedGraph): The graph to perform DFS on.

- vertex (int): The starting vertex index for DFS.
- visited (set): Set of visited vertices.
- stack (list): Stack to push vertices according to their
finishing times.

<a id="python_solutions.graph.Graph.reverse_graph"></a>

#### reverse\_graph

```python
def reverse_graph()
```

Reverses the direction of all edges in the graph.

- **Args**: - graph (DirectedGraph): The graph to reverse.


- **Returns**: - DirectedGraph: A new graph with reversed edges.


<a id="python_solutions.graph.Graph.dfs_util"></a>

#### dfs\_util

```python
def dfs_util(reversed_graph, vertex, visited, scc)
```

A utility function for DFS traversal that tracks
the strongly connected component.

- **Args**: - graph (DirectedGraph): The graph to perform DFS on.

- vertex (int): The starting vertex index for DFS.
- visited (set): Set of visited vertices.
- scc (list): List to accumulate vertices in the current SCC.

<a id="python_solutions.graph.Graph.dijkstra"></a>

#### dijkstra

```python
def dijkstra(start: int)
```

<a id="python_solutions.graph.Graph.is_cyclic_util"></a>

#### is\_cyclic\_util

```python
def is_cyclic_util(vertex, visited, rec_stack)
```

<a id="python_solutions.graph.Graph.is_cyclic"></a>

#### is\_cyclic

```python
def is_cyclic()
```

<a id="python_solutions.graph.Graph.bellman_ford"></a>

#### bellman\_ford

```python
def bellman_ford(start)
```

<a id="python_solutions.graph.Graph.bfs_level_graph"></a>

#### bfs\_level\_graph

```python
def bfs_level_graph(source)
```

<a id="python_solutions.graph.Graph.dfs_blocking_flow"></a>

#### dfs\_blocking\_flow

```python
def dfs_blocking_flow(source, sink, flow, levels)
```

<a id="python_solutions.graph.Graph.dinics_algorithm"></a>

#### dinics\_algorithm

```python
def dinics_algorithm(source, sink)
```

<a id="python_solutions.graph.Graph.initialize_preflow"></a>

#### initialize\_preflow

```python
def initialize_preflow(source)
```

<a id="python_solutions.graph.Graph.push_flow"></a>

#### push\_flow

```python
def push_flow(u, v)
```

<a id="python_solutions.graph.Graph.lift_vertex"></a>

#### lift\_vertex

```python
def lift_vertex(u)
```

<a id="python_solutions.graph.Graph.discharge_excess_flow"></a>

#### discharge\_excess\_flow

```python
def discharge_excess_flow(u)
```

<a id="python_solutions.graph.Graph.goldberg_tarjan"></a>

#### goldberg\_tarjan

```python
def goldberg_tarjan(source, sink)
```

<a id="python_solutions.graph.Graph.color_vertices"></a>

#### color\_vertices

```python
def color_vertices()
```

<a id="python_solutions.graph.Graph.all_edges"></a>

#### all\_edges

```python
def all_edges()
```

<a id="python_solutions.graph.Graph.color_edges"></a>

#### color\_edges

```python
def color_edges()
```

<a id="python_solutions.graph_nodes.BaseGraphNode"></a>

## BaseGraphNode Objects

```python
class BaseGraphNode()
```

<a id="python_solutions.graph_nodes.BaseGraphNode.__init__"></a>

#### \_\_init\_\_

```python
def __init__(index, data, color) -> None
```

<a id="python_solutions.graph_nodes.BaseGraphNode.__str__"></a>

#### \_\_str\_\_

```python
def __str__() -> str
```

<a id="python_solutions.graph_nodes.BaseGraphNode.__repr__"></a>

#### \_\_repr\_\_

```python
def __repr__() -> str
```

<a id="python_solutions.graph_nodes.GraphNode"></a>

## GraphNode Objects

```python
class GraphNode(BaseGraphNode)
```

<a id="python_solutions.graph_nodes.GraphNode.__init__"></a>

#### \_\_init\_\_

```python
def __init__(index, data, edges=[], capacities=[], color=0) -> None
```

<a id="python_solutions.graph_nodes.WeightedGraphNode"></a>

## WeightedGraphNode Objects

```python
class WeightedGraphNode(GraphNode)
```

<a id="python_solutions.graph_nodes.WeightedGraphNode.__init__"></a>

#### \_\_init\_\_

```python
def __init__(index,
             data,
             edges=[],
             weights=[],
             capacities=[],
             color=0) -> None
```

<a id="python_solutions.graph_nodes.Edge"></a>

## Edge Objects

```python
class Edge()
```

<a id="python_solutions.graph_nodes.Edge.__init__"></a>

#### \_\_init\_\_

```python
def __init__(first_node: int,
- **second_node**: int,

             weight=1,
             capacity=0,
             flow=0,
             color=0,
             *args,
             **kwargs) -> None
```

Hash Table Implementations with Open and Closed Addressing
=========================================================

- **This module provides two hash table implementations**: HashTable_closed and

HashTable_open, using closed and open addressing, respectively, for collision
resolution. Both implementations offer methods for adding, retrieving,
and removing key-value pairs.

Classes
-------
HashTable_closed
    A hash table implementation using closed addressing (separate chaining) to
    handle collisions.

HashTable_open
    A hash table implementation using open addressing (multiple and cuckoo
    hashing) to handle collisions with multiple hash functions.

PairsVector
    A specialized vector for storing key-value pairs in hash tables using
    closed addressing.

ElementsList
    A specialized list for storing elements in hash tables using open
    addressing.

Pair
    A named tuple representing a key-value pair.

Functions
---------
gen_primes()
    Generate an infinite sequence of prime numbers for use as hash table
    capacity.

gen_prime(stop=30)
    Generate prime numbers up to a specified stop value.

poly_hash(x)
    Calculate a polynomial hash value for a given input.

<a id="python_solutions.hashtable.hashlib"></a>

## hashlib

<a id="python_solutions.hashtable.logging"></a>

## logging

<a id="python_solutions.hashtable.deque"></a>

## deque

<a id="python_solutions.hashtable.Any"></a>

## Any

<a id="python_solutions.hashtable.NamedTuple"></a>

## NamedTuple

<a id="python_solutions.hashtable.Vector"></a>

## Vector

<a id="python_solutions.hashtable.Pair"></a>

## Pair Objects

```python
class Pair(NamedTuple)
```

<a id="python_solutions.hashtable.Pair.key"></a>

#### key

<a id="python_solutions.hashtable.Pair.value"></a>

#### value

<a id="python_solutions.hashtable.gen_primes"></a>

#### gen\_primes

```python
def gen_primes()
```

Generate an infinite sequence of prime numbers.

<a id="python_solutions.hashtable.gen_prime"></a>

#### gen\_prime

```python
def gen_prime(stop=30)
```

<a id="python_solutions.hashtable.poly_hash"></a>

#### poly\_hash

```python
def poly_hash(x)
```

<a id="python_solutions.hashtable.simple_hash"></a>

#### simple\_hash

```python
def simple_hash(x)
```

<a id="python_solutions.hashtable.PairsVector"></a>

## PairsVector Objects

```python
class PairsVector(Vector)
```

<a id="python_solutions.hashtable.PairsVector.__setitem__"></a>

#### \_\_setitem\_\_

```python
def __setitem__(key, value)
```

<a id="python_solutions.hashtable.HashTable_closed"></a>

## HashTable\_closed Objects

```python
class HashTable_closed()
```

A hash table implementation using closed addressing
for collision resolution.

This class represents a hash table that uses closed addressing
(separate chaining) to handle collisions.
It provides methods for adding, retrieving, and removing key-value pairs.

## Attributes
- **capacity**: int

    The initial capacity of the hash table.

- **size**: int

    The number of key-value pairs currently stored in the hash table.

- **hashfunc**: str or callable

    The hashing function family used to determine the index
    for storing keys. Supported values: 'poly' (polynomial hash),
    'md5', 'sha1', or a custom callable function.

## Methods

__setitem__(self, key, value) -> None
    Adds a key-value pair to the hash table.

__getitem__(self, key) -> Any
    Retrieves the value associated with a given key.

__delitem__(self, key) -> None
    Removes a key-value pair from the hash table.

to_dict(self) -> dict
    Returns a dictionary representation of the hash table.

__contains__(self, key) -> bool
    Checks if a key exists in the hash table.

from_dict(cls, dictionary) -> HashTable_closed
    Creates a new hash table from a dictionary.

__str__(self) -> str
    Returns a string representation of the hash table.

__repr__(self) -> str
    Used for printing the contents of the hash table.

__eq__(self, other) -> bool
    Checks if two hash tables are equal.

## Notes

This hash table uses closed addressing to resolve collisions,
which means that multiple key-value pairs with the same hash value
are stored in linked lists within the hash table.

<a id="python_solutions.hashtable.HashTable_closed.__init__"></a>

#### \_\_init\_\_

```python
def __init__(capacity=30, hashfunc=simple_hash, load_factor_threshold=0.75)
```

Initializes a HashTable_closed object with specified capacity
and hash function.

## Parameters
- **capacity**: int

    The initial capacity of the hash table.

- **hashfunc**: str or callable

    The hashing function family used to determine the index
    for storing keys. Supported values: 'poly' (polynomial hash),
    'md5', 'sha1', or a custom callable function.

- **load_factor_threshold**: float

    The maximum size / capacity ratio. When the actual value
    excesses this factor - the hashtable increases its size.
    When the actual value < this / 4 - the hashtable decreases its
    size. Can be set to any between 0 and 1, but is recommended to be
    set around 0.7 - 0.9.

## Returns

None

<a id="python_solutions.hashtable.HashTable_closed.get_hash"></a>

#### get\_hash

```python
def get_hash(x)
```

Calculates the hash value for a given key
using the selected hash function.

## Parameters
- **x**: any

    The key to be hashed.

## Returns

int
    The calculated hash value.

<a id="python_solutions.hashtable.HashTable_closed.pairs"></a>

#### pairs

```python
@property
def pairs()
```

Property getter method for retrieving the pairs attribute
of the hash table.

## Returns

list
    A copy of the internal list of pairs in the hash table.

<a id="python_solutions.hashtable.HashTable_closed.pairs"></a>

#### pairs

```python
@pairs.setter
def pairs(value)
```

Setter method for the pairs attribute.
Raises an error as the pairs attribute is read-only.

## Parameters
- **value**: any

    The value to be set (not used).

## Returns

None

## Raises
- **NotImplementedError**: Always raised since the pairs attribute is

    read-only.

<a id="python_solutions.hashtable.HashTable_closed.size"></a>

#### size

```python
@property
def size()
```

Property getter method for retrieving the size attribute of the
hash table.

## Returns

int
    The number of key-value pairs currently stored in the hash table.

<a id="python_solutions.hashtable.HashTable_closed.size"></a>

#### size

```python
@size.setter
def size(size)
```

Setter method for the size attribute.
Raises an error as the size attribute is read-only.

## Parameters
- **size**: int

    The value to be set (not used).

## Returns

None

## Raises
- **NotImplementedError**: Always raised since the size attribute is

    read-only.

<a id="python_solutions.hashtable.HashTable_closed.capacity"></a>

#### capacity

```python
@property
def capacity()
```

Property getter method for retrieving the capacity attribute
of the hash table.

## Returns

int
    The current capacity of the hash table.

<a id="python_solutions.hashtable.HashTable_closed.capacity"></a>

#### capacity

```python
@capacity.setter
def capacity(capacity)
```

Setter method for the capacity attribute.
Raises an error as the capacity attribute is read-only.

## Parameters
- **capacity**: int

    The value to be set (not used).

## Returns

None

## Raises
- **NotImplementedError**: Always raised since the capacity attribute is

    read-only.

<a id="python_solutions.hashtable.HashTable_closed.__len__"></a>

#### \_\_len\_\_

```python
def __len__()
```

Returns the number of key-value pairs currently
stored in the hash table.

## Returns

int
    The size of the hash table.

<a id="python_solutions.hashtable.HashTable_closed.__setitem__"></a>

#### \_\_setitem\_\_

```python
def __setitem__(key, x)
```

Adds or updates (if already taken) a key-value pair to the hash table.

## Parameters
- **key**: any

    The key to be added.
- **x**: any

    The value associated with the key.

<a id="python_solutions.hashtable.HashTable_closed.__getitem__"></a>

#### \_\_getitem\_\_

```python
def __getitem__(i)
```

Retrieves the value associated with a given key from the hash table.

## Parameters
- **i**: int

    The key for which to retrieve the value.

## Returns

Any
    The value associated with the key.

## Raises
- **KeyError**: If the key is not found in the hash table.


<a id="python_solutions.hashtable.HashTable_closed.increase_capacity"></a>

#### increase\_capacity

```python
def increase_capacity()
```

Increases the capacity of the hash table.

## Returns

None

<a id="python_solutions.hashtable.HashTable_closed.recapacitate_and_rehash"></a>

#### recapacitate\_and\_rehash

```python
def recapacitate_and_rehash(old_capacity)
```

Recalculates the hash values and rehashes the key-value pairs.

## Parameters
- **old_capacity**: int

    The previous capacity of the hash table.

## Returns

None

<a id="python_solutions.hashtable.HashTable_closed.decrease_capacity"></a>

#### decrease\_capacity

```python
def decrease_capacity()
```

Decreases the capacity of the hash table.

<a id="python_solutions.hashtable.HashTable_closed.search"></a>

#### search

```python
def search(key)
```

Searches for a key in the hash table and returns the index if found,
or False if not found.

## Parameters
- **key**: any

    The key to search for.

## Returns

int or False
    The index of the key in the hash table if found,
    or False if not found.

<a id="python_solutions.hashtable.HashTable_closed.__delitem__"></a>

#### \_\_delitem\_\_

```python
def __delitem__(key)
```

Removes a key-value pair from the hash table.

## Parameters
- **key**: any

    The key to be removed.

## Returns

None

<a id="python_solutions.hashtable.HashTable_closed.to_dict"></a>

#### to\_dict

```python
def to_dict()
```

Returns a dictionary representation of the hash table.

## Returns

dict
    A dictionary containing the key-value pairs from the hash table.

<a id="python_solutions.hashtable.HashTable_closed.__contains__"></a>

#### \_\_contains\_\_

```python
def __contains__(key)
```

Checks if a key exists in the hash table.

## Parameters
- **key**: any

    The key to check for existence.

## Returns

bool
    True if the key exists in the hash table, False otherwise.

<a id="python_solutions.hashtable.HashTable_closed.from_dict"></a>

#### from\_dict

```python
@classmethod
def from_dict(cls, dictionary)
```

Creates a new HashTable_closed object from a dictionary.

## Parameters
- **dictionary**: dict

    The dictionary to create the hash table from.

## Returns

HashTable_closed
    A new HashTable_closed object initialized with
    the contents of the dictionary.

<a id="python_solutions.hashtable.HashTable_closed.__str__"></a>

#### \_\_str\_\_

```python
def __str__()
```

Returns a string representation of the hash table.

## Returns

str
    A string representation of the hash table as a dictionary.

<a id="python_solutions.hashtable.HashTable_closed.__repr__"></a>

#### \_\_repr\_\_

```python
def __repr__()
```

Returns a string representation of the hash table used for printing.

## Returns

str
    A string representation of the hash table as a dictionary.

<a id="python_solutions.hashtable.HashTable_closed.__eq__"></a>

#### \_\_eq\_\_

```python
def __eq__(other)
```

Checks if two hash tables are equal by comparing their
dictionary representations.

## Parameters
- **other**: object with defined to_dict method

    Another hash table to compare.

## Returns

bool
    True if the hash tables are equal, False otherwise.

<a id="python_solutions.hashtable.ElementsList"></a>

## ElementsList Objects

```python
class ElementsList(list)
```

<a id="python_solutions.hashtable.ElementsList.__setitem__"></a>

#### \_\_setitem\_\_

```python
def __setitem__(key, value)
```

<a id="python_solutions.hashtable.HashTable_open"></a>

## HashTable\_open Objects

```python
class HashTable_open(HashTable_closed)
```

A hash table implementation using open addressing
for collision resolution.

This class represents a hash table that uses open addressing
(multiple and cuckoo hashing) to handle collisions.
It provides methods for adding, retrieving, and removing key-value pairs.

## Attributes
- **capacity**: int

    The initial capacity of the hash table.

- **hashfuncs**: list of str or callable

    A list of hash functions used to determine the index for storing keys.
- **Supported values**: 'md5', 'sha1', 'poly' (polynomial hash),

    or custom callable functions.

## Methods

__setitem__(self, key, value) -> None
    Adds a key-value pair to the hash table.

__getitem__(self, key) -> Any
    Retrieves the value associated with a given key.

__delitem__(self, key) -> None
    Removes a key-value pair from the hash table.

to_dict(self) -> dict
    Returns a dictionary representation of the hash table.

update(self, key, value) -> None
    Updates the value associated with a given key in the hash table.

search(self, key) -> tuple(int, int) or False
    Searches for a key in the hash table and returns
    the table index and hashed key index if found, or False if not found.

increase_capacity(self) -> None
    Increases the capacity of the hash table.

decrease_capacity(self) -> None
    Decreases the capacity of the hash table.

one_table_capacity(self) -> int
    Calculates the capacity of each individual
    hash table within the open addressing scheme.

get_hashes(self, key) -> generator
    Generates hash values for a key using the specified hash functions.

current_hashed_key(self, key, table_index) -> int
    Computes the hashed key index for a key based on
    the current table index.

recapacitate_and_rehash(self) -> None
    Recapacitates and rehashes hashtable.

## Notes

This hash table uses open addressing (multiple and cuckoo hashing)
to resolve collisions, which means that when a collision occurs,
it looks for alternative positions within the table using multiple
hash functions.

Supported hash functions include 'md5', 'sha1', 'poly' (polynomial hash),
and custom callable functions.

<a id="python_solutions.hashtable.HashTable_open.__init__"></a>

#### \_\_init\_\_

```python
def __init__(capacity=30, hashfuncs=[hash, simple_hash], max_displasements=16)
```

Initializes a HashTable_open instance with the given capacity
and hash functions.

## Parameters
- **capacity**: int, optional

    The initial capacity of the hash table, by default 30.

- **hashfuncs**: list of str or callables, optional

    A list of hash functions used to determine the index
    for storing keys, by default ['md5', 'sha1'].

## Returns

None

<a id="python_solutions.hashtable.HashTable_open.one_table_capacity"></a>

#### one\_table\_capacity

```python
def one_table_capacity()
```

Calculates the capacity of each individual hash table
within the open addressing scheme.

## Returns

int
    The capacity of one hash table.

<a id="python_solutions.hashtable.HashTable_open.get_hashes"></a>

#### get\_hashes

```python
def get_hashes(key)
```

Generates hash values for a key using the specified hash functions.

## Parameters
- **key**: Any

    The key for which hash values are generated.

Yields
------
int
    A hash value for the key.

<a id="python_solutions.hashtable.HashTable_open.current_hashed_key"></a>

#### current\_hashed\_key

```python
def current_hashed_key(key, table_index)
```

Computes the hashed key index for a key based on the
current table index.

## Parameters
- **key**: Any

    The key for which the hashed key index is computed.

- **table_index**: int

    The index of the hash table within the open addressing scheme.

## Returns

int
    The hashed key index for the key in the specified table.

<a id="python_solutions.hashtable.HashTable_open.elements"></a>

#### elements

```python
@property
def elements()
```

Defensive copying of the elements array.

## Returns

list
    A copy of the elements array.

<a id="python_solutions.hashtable.HashTable_open.__setitem__"></a>

#### \_\_setitem\_\_

```python
def __setitem__(key, value)
```

Adds a key-value pair to the hash table.

## Parameters
- **key**: Any

    The key to be added.

- **value**: Any

    The value associated with the key.

## Returns

None

<a id="python_solutions.hashtable.HashTable_open.update"></a>

#### update

```python
def update(key, value)
```

Updates the value associated with a given key in the hash table.

## Parameters
- **key**: Any

    The key for which the value should be updated.

- **value**: Any

    The new value to associate with the key.

## Returns

None

## Raises

KeyError
    Raised if no value is present for the corresponding key.

<a id="python_solutions.hashtable.HashTable_open.__delitem__"></a>

#### \_\_delitem\_\_

```python
def __delitem__(key)
```

Removes a key-value pair from the hash table.

## Parameters
- **key**: Any

    The key to be removed.

## Returns

None

<a id="python_solutions.hashtable.HashTable_open.__getitem__"></a>

#### \_\_getitem\_\_

```python
def __getitem__(key)
```

Retrieves the value associated with a given key in the hash table.

## Parameters
- **key**: Any

    The key for which the value is retrieved.

## Returns

Any
    The value associated with the key.

## Raises

KeyError
    Raised if no value is found for the corresponding key.

<a id="python_solutions.hashtable.HashTable_open.search"></a>

#### search

```python
def search(key)
```

Searches for a key in the hash table and returns
the table index and hashed key index if found,
or False if not found.

## Parameters
- **key**: Any

    The key to be searched for.

## Returns

tuple(int, int) or False
    A tuple containing the table index and hashed key index if found,
    or False if the key is not present in the hash table.

<a id="python_solutions.hashtable.HashTable_open.recapacitate_and_rehash"></a>

#### recapacitate\_and\_rehash

```python
def recapacitate_and_rehash()
```

Recapacitates the hash table and rehashes its contents.

## Parameters
- **old_capacity**: int

    The old capacity of the hash table.

## Returns

None

<a id="python_solutions.hashtable.HashTable_open.to_dict"></a>

#### to\_dict

```python
def to_dict()
```

Returns a dictionary representation of the hash table.

## Returns

dict
    A dictionary containing key-value pairs from the hash table.

Binary Heap and Sort
====================

A module for implementing a binary tree-based min-heap data structure and
heap sort algorithm.

This module contains classes and functions for working with binary tree-based
min-heaps and performing heap sort. A binary tree-based min-heap is a data
structure where the minimum value is stored at the root, and each parent node
contains elements smaller than its children.

Classes
-------
Heap
    A binary tree-based min-heap that extends the Vector class to represent
    the heap. It provides methods for insertion, removal of the minimum
    element, and other heap-related operations.

Functions
---------
heap_sort(array: list[float]) -> list[float]
    Sorts an array in ascending order using the heap sort algorithm.
    Heap sort is an efficient comparison-based sorting algorithm that uses
    a binary heap to perform the sorting.

sift_up(array: list[float], element_index: int, size: int) -> None
    Performs the sift-up operation to maintain the heap property.

sift_down(array: list[float], element_index: int) -> None
    Performs the sift-down operation to maintain the heap property.

<a id="python_solutions.heap.Vector"></a>

## Vector

<a id="python_solutions.heap.Heap"></a>

## Heap Objects

```python
class Heap(Vector)
```

A binary tree-based min-heap data structure.

This class extends the Vector class to represent a binary
tree-based min-heap, where the minimum value is stored at the root,
and each parent node contains elements smaller than its children.

## Attributes
- **elements**: list or None, optional

    An optional list of initial elements for the heap,
    by default None.

- **size**: int, optional

    The initial size of the heap, by default 0.

- **capacity**: int, optional

    The initial capacity of the heap, by default 1.

## Methods

__init__(self, elements: list[float] | None = None,
- **size**: int = 0, capacity: int = 1) -> None

    Initialize the heap.

append(self, x: float) -> None
    Append an element to the heap.

get_children(self, i: int) -> tuple(float, float) or float or None
    Get the children of a node at the specified index.

height(self) -> int
    Calculate the height of the heap.

insert(self, x: float) -> None
    Insert an element into the heap.

remove_min(self) -> float
    Remove and return the minimum element from the heap.

__repr__(self) -> str
    Return a string representation of the heap.

erase(self) -> float
    Alias for `remove_min`.

<a id="python_solutions.heap.Heap.__init__"></a>

#### \_\_init\_\_

```python
def __init__(elements: list[float] | None = None,
- **size**: int = 0,

- **capacity**: int = 1) -> None

```

Initialize a new Heap instance.

## Parameters
- **elements**: list or None, optional

    An optional list of initial elements for the heap,
    by default None.

- **size**: int, optional

    The initial size of the heap, by default 0.

- **capacity**: int, optional

    The initial capacity of the heap, by default 1.

## Returns

None

<a id="python_solutions.heap.Heap.append"></a>

#### append

```python
def append(x: float) -> None
```

Append an element to the heap.

This method is an alias for `insert`.

## Parameters
- **x**: float

    The element to append to the heap.

## Returns

None

<a id="python_solutions.heap.Heap.get_children"></a>

#### get\_children

```python
def get_children(i: int) -> tuple[float, float] | float | None
```

Get the children of a node at the specified index.

## Parameters
- **i**: int

    The index of the node for which to retrieve children.

## Returns

tuple or float or None
    A tuple containing the left and right children of the node
    if both exist, the left child if only the left child exists,
    or None if the node has no children.

<a id="python_solutions.heap.Heap.height"></a>

#### height

```python
def height() -> int
```

Calculate the height of the heap.

## Returns

int
    The height of the heap.

<a id="python_solutions.heap.Heap.insert"></a>

#### insert

```python
def insert(x: float) -> None
```

Insert an element into the heap.

If the size of the heap becomes equal to its capacity after
insertion, the capacity is increased.

## Parameters
- **x**: Any

    The element to insert into the heap.

## Returns

None

<a id="python_solutions.heap.Heap.remove_min"></a>

#### remove\_min

```python
def remove_min() -> float
```

Remove and return the minimum element from the heap.

If the size of the heap becomes less than or equal to one-fourth
of its capacity after removal, the capacity is decreased.

## Returns

float
    The minimum element in the heap.

## Raises

IndexError
    Raised if the heap is empty.

<a id="python_solutions.heap.Heap.__repr__"></a>

#### \_\_repr\_\_

```python
def __repr__() -> str
```

Return a string representation of the heap.

## Returns

str
    A string representation of the heap in a tree-like format.

<a id="python_solutions.heap.Heap.erase"></a>

#### erase

```python
def erase() -> float
```

Alias for `remove_min`.

## Returns

float
    The minimum element in the heap.

<a id="python_solutions.heap.sift_up"></a>

#### sift\_up

```python
def sift_up(a: list[float], i: int) -> None
```

Perform the sift-up operation to maintain heap property.

## Parameters
- **a**: list

    The list representing the elements of the heap.

- **i**: int

    The index at which the sift-up operation is performed.

## Returns

None

<a id="python_solutions.heap.sift_down"></a>

#### sift\_down

```python
def sift_down(a: list[float], i: int, size: int) -> None
```

Perform the sift-down operation to maintain heap property.

## Parameters
- **a**: list

    The list representing the elements of the heap.

- **i**: int

    The index at which the sift-down operation is performed.

- **size**: int

    The size of the heap.

## Returns

None

<a id="python_solutions.heap.heap_sort"></a>

#### heap\_sort

```python
def heap_sort(array: list[float]) -> list[float]
```

Sort an array in ascending order using the heap sort algorithm.

Heap sort is a comparison-based sorting algorithm that builds a binary
heap data structure and repeatedly extracts the minimum element from the
heap. The sorted elements are stored in the original array. This algorithm
has a time complexity of O(n log n) in the worst case, making it efficient
for large datasets. However, it is not an in-place sorting algorithm since
it requires additional space for the heap, making its O(n) space
complexity.
- **The heap sort algorithm consists of two main phases**: heapify and sorting.

The "heapify" phase builds a binary heap from the input array,
ensuring that the heap property is maintained (parent nodes have smaller
values than their children).
The "sorting" phase repeatedly removes the minimum element from the heap
and places it at the end of the array until the heap is empty.

## Parameters
- **array**: list

    The list to be sorted.

## Returns

list
    The sorted list in ascending order.

HyperLogLog Module

This module implements the HyperLogLog algorithm for approximate cardinality
estimation of large data sets.

Classes
-------
HyperLogLog
    A class implementing the HyperLogLog algorithm.

<a id="python_solutions.hyperloglog.math"></a>

## math

<a id="python_solutions.hyperloglog.hashlib"></a>

## hashlib

<a id="python_solutions.hyperloglog.array"></a>

## array

<a id="python_solutions.hyperloglog.HyperLogLog"></a>

## HyperLogLog Objects

```python
class HyperLogLog()
```

HyperLogLog Algorithm Implementation

This class provides methods to estimate the cardinality of a
large data set using the HyperLogLog algorithm.

## Attributes
- **precision**: int, optional

    The precision parameter for the algorithm. This parameter corresponds
    to the amount of binary registers where the numbers will be written
    to. The higher the precision - the thinner bins for probability
    distribution for the algorithm. Default is 14.

## Methods

__init__(self, precision=14) -> None
    Initialize HyperLogLog structure.

_hash(self, element: str) -> str
    Hash the element using SHA256.

_leading_zeros(self, binary_string: str) -> int
    Count the number of leading zeros in a binary string.

add(self, element: str) -> None
    Add an element to the HyperLogLog data structure.

count(self) -> int
    Estimate the cardinality of the data set.

<a id="python_solutions.hyperloglog.HyperLogLog.__init__"></a>

#### \_\_init\_\_

```python
def __init__(precision=14) -> None
```

Initialize a HyperLogLog object with a given precision.

## Parameters
- **precision**: int, optional

    The precision parameter for the algorithm. Default is 14.

## Returns

None

<a id="python_solutions.hyperloglog.HyperLogLog._hash"></a>

#### \_hash

```python
def _hash(element) -> str
```

Hash the element using SHA256.

## Parameters
- **element**: str

    The element to be hashed.

## Returns

str
    The binary hash value of the element.

<a id="python_solutions.hyperloglog.HyperLogLog._leading_zeros"></a>

#### \_leading\_zeros

```python
def _leading_zeros(binary_string) -> int
```

Count the number of leading zeros in a binary string.

## Parameters
- **binary_string**: str

    The binary string.

## Returns

int
    The number of leading zeros.

<a id="python_solutions.hyperloglog.HyperLogLog.add"></a>

#### add

```python
def add(element) -> None
```

Add an element to the HyperLogLog data structure.

## Parameters
- **element**: str

    The element to be added.

## Returns

None

<a id="python_solutions.hyperloglog.HyperLogLog.count"></a>

#### count

```python
def count() -> int
```

Estimate the cardinality of the data set.

## Returns

int
    The estimated cardinality of the data set.

Insertion Sort
==============

A module with Insertion Sort algorithm to sort a list of elements.

Insertion Sort is a simple sorting algorithm that works by iterating through
the input list and, for each element, comparing it with the elements to its
left and inserting it into its correct position within the already sorted
portion of the list. This process continues until the entire list is sorted.

Functions
---------
insert_sort(array: list[float]) -> list[float]
    Sorts a list of elements using the Insertion Sort algorithm.

insert_sort_opt(array: list[float]) -> list[float]
    Sorts a list of elements using the optimized Insertion Sort algorithm.
    This version uses binary search to find the correct position for each
    element, reducing the number of comparisons and improving efficiency.

<a id="python_solutions.insert_sort.insert_sort"></a>

#### insert\_sort

```python
def insert_sort(array: list[float]) -> list[float]
```

This function implements the Insertion Sort algorithm
to sort a list of elements in-place.

The Insertion Sort algorithm works by iterating through the input list,
and for each element, it compares it with the elements
to its left and inserts it into its correct position within
the already sorted portion of the list.
This process continues until the entire list is sorted.
Worst and average cases time complexity - O(n^2).
Space complexity - O(1) as sorting is done in-place.

## Parameters
- **array**: list

    The input list to be sorted.

## Returns

list
    A list containing the elements of the input list in sorted order.

<a id="python_solutions.insert_sort.bin_search_fl"></a>

#### bin\_search\_fl

```python
def bin_search_fl(array: list[float], value: float, start: int,
- **end**: int) -> int

```

<a id="python_solutions.insert_sort.insert_sort_opt"></a>

#### insert\_sort\_opt

```python
def insert_sort_opt(array: list[float]) -> list[float]
```

This function implements the in-place Insertion sort algorithm
enhanced by binary search.

Sorts a list of elements using the optimized Insertion Sort algorithm.
This version uses binary search to find the correct position for each
element, reducing the number of comparisons and improving efficiency.

## Parameters
- **array**: list

    The input list to be sorted.

## Returns

list
    A list containing the elements of the input list in sorted order.

Matrix2dim Module
======================

A module for creating and displaying 2-Dimensional matrices.

This module contains the `Matrix2dim` class, which provides a convenient way
to create and display 2-Dimensional matrices.

Classes
-------
Matrix2dim
    A class for creating and displaying 2-Dimensional matrices.

<a id="python_solutions.matrix_view.Matrix2dim"></a>

## Matrix2dim Objects

```python
class Matrix2dim()
```

2-Dimensional Matrix Class

The Matrix2dim class provides beautiful print method
for 2-Dimensional lists.

## Attributes
- **data**: list of lists

    A list of lists representing the 2D matrix.

## Methods

__init__(self, data) -> None
    Initializes a Matrix2dim object with the provided data.

__repr__(self, indexes=False) -> None
    Returns a string representation of the matrix.

<a id="python_solutions.matrix_view.Matrix2dim.__init__"></a>

#### \_\_init\_\_

```python
def __init__(data) -> None
```

Initialize a Matrix2dim object.

## Parameters
- **data**: list of lists

    A list of lists representing the 2D matrix.

## Returns

None

<a id="python_solutions.matrix_view.Matrix2dim.__repr__"></a>

#### \_\_repr\_\_

```python
def __repr__(indexes=False) -> str
```

Return a string representation of the 2D matrix.

## Parameters
- **indexes**: bool, optional

    If True, include row and column indexes in the representation.
    Default is False.

## Returns

None

Merge Sort Module
=================

A module containing Merge Sort algorithms and a helper function for merging
arrays.

This module specializes in various implementations of the Merge Sort
algorithm and a helper function for merging two sorted arrays into a single
sorted array.

Functions
---------
merge(array: list[float], part_one: list[float], part_two: list[float])
    -> None
    Merge two sorted arrays into a single sorted array.

merge_sort(array: list[float], opt: bool = True, batch_size: int = 3)
    -> list[float]
    Sort a list of elements using the Merge Sort algorithm.
    Optimised version (opt=True) calls Insertion Sort for small arrays.

merge_sort_parallel(array: list[float], batch_size=None, depth=0)
    -> list[float]
    Sort a list of elements with multiprocessing using the Merge Sort
    algorithm.

parallel_merge_sort(arr: list[float], batch_size=None, depth=0)
    -> list[float]
    Function-helper for merge_sort_parallel which handles recursion
    and multiprocessing.

Constants
---------
- **MERGE_OPT**: bool

    Determines whether the merge sort will utilize insertion sort at all
    or not. Assumes a value automatically based on whether it is possible
    to import insertion sort function.

- **MAX_DEPTH**: int

    Recursion control constant. Determines the depth after which parallel
    merge sort implementation will not call recursion any longer.
    Default is set to cpu_count.

<a id="python_solutions.merge_sort.logging"></a>

## logging

<a id="python_solutions.merge_sort.cpu_count"></a>

## cpu\_count

<a id="python_solutions.merge_sort.Pool"></a>

## Pool

<a id="python_solutions.merge_sort.MAX_DEPTH"></a>

#### MAX\_DEPTH

<a id="python_solutions.merge_sort.merge"></a>

#### merge

```python
def merge(array: list[float], part_one: list[float],
- **part_two**: list[float]) -> None

```

Merge Two Sorted Arrays

This function merges two sorted arrays, `part_one` and `part_two`, into
a single sorted array. This is a helper for the Merge Sort function.
Both space and time complexities are O(n), where n - the number of
elements inside two arrays combined.

## Parameters
- **array**: list[float]

    The resulting array

- **part_one**: list[float]

    The first sorted array to be merged.

- **part_two**: list[float]

    The second sorted array to be merged.

## Returns

None

<a id="python_solutions.merge_sort.merge_sort"></a>

#### merge\_sort

```python
def merge_sort(array: list[float],
- **opt**: bool = MERGE_OPT,

               batch_size=3) -> list[float]
```

Merge Sort

This function implements the Merge Sort algorithm
to sort a list of elements.

The Merge Sort algorithm works by dividing the input list into
two halves, recursively sorting each half, and then merging the
two sorted halves into one sorted list.
Time Complexity is O(n*log(n)), space complexity - O(n).
Space is used for storing divided subarrays during sorting.

## Parameters
- **array**: list[float]

    The input list to be sorted.

- **opt**: bool

    A switch between faster version using Insertion Sort
    on small arrays and slower version without it. Default is True.

- **batch_size**: int

    A threshold for switching between further dividing the input and
    binary search optimized insertion sort, if opt is True.
    Default, tuned for the best performance, value is 3.

## Returns

list[float]
    A new list containing the elements of the input list
    in sorted order.

<a id="python_solutions.merge_sort.parallel_merge_sort"></a>

#### parallel\_merge\_sort

```python
def parallel_merge_sort(arr: list[float],
                        batch_size=None,
                        depth=0) -> list[float]
```

<a id="python_solutions.merge_sort.merge_sort_parallel"></a>

#### merge\_sort\_parallel

```python
def merge_sort_parallel(array: list[float],
                        batch_size=None,
                        depth=0) -> list[float]
```

Parallel Merge Sort using dynamic ThreadPoolExecutor

This function implements the Merge Sort algorithm in parallel
to sort a list of elements.

## Parameters
- **array**: list[float]

    The input list to be sorted.

- **batch_size**: int

    A threshold to switch from parallel algorithm to the usual one
    once the part to be sorted will become as small as a batch_size.
    Default is None, which would later translate to
    (len(array) // 100) + 1

- **depth**: int

    Recursion depth control parameter, used for avoiding overheading.
    Default is 4. If set to None will translate to the number of cores.

## Returns

list[float]
    A new list containing the elements of the input list in sorted order.

Node Module

This module defines a simple one-way node class that can store data and
have a reference to the next node in a linked list.

Classes
-------
Node
    A class representing a one-way node with basic operations.

<a id="python_solutions.Node.Node"></a>

## Node Objects

```python
class Node()
```

Simple One-Way Node Class

The Node class represents a simple one-way node that can store data and
have a reference to the next node in a linked list. It supports basic
operations like getting the next node and printing the data.

## Attributes
- **_next_node**: Node or None

    Reference to the next node if it exists.

- **_data**: any

    Data stored inside the node.

## Methods

__init__(self, data=None, next_node=None)
    Initialize a Node object with optional data and next node.

__str__(self)
    Return a string representation of the data stored in the node.

__next__(self)
    Get the reference to the next node.

__repr__(self)
    Return a string representation of the node.

__eq__(self, other)
    Compare if two nodes are the same (reference equality).

<a id="python_solutions.Node.Node.__init__"></a>

#### \_\_init\_\_

```python
def __init__(data=None, next_node=None)
```

Initialize a Node object with optional data and next node.

## Parameters
- **data**: any, optional

    The data to be stored in the node. Default is None.

- **next_node**: Node or None, optional

    The next node in the linked list. Default is None.

## Returns

None

## Raises

TypeError
    If the provided next_node is of the wrong type.

<a id="python_solutions.Node.Node.__str__"></a>

#### \_\_str\_\_

```python
def __str__()
```

Return a string representation of the data stored in the node.

## Returns

str
    The string representation of the data.

<a id="python_solutions.Node.Node.__next__"></a>

#### \_\_next\_\_

```python
def __next__()
```

Get the reference to the next node.

## Returns

Node or None
    The reference to the next node or None if it doesn't exist.

<a id="python_solutions.Node.Node.__repr__"></a>

#### \_\_repr\_\_

```python
def __repr__()
```

Return a string representation of the node.

## Returns

str
    The string representation of the node.

<a id="python_solutions.Node.Node.__eq__"></a>

#### \_\_eq\_\_

```python
def __eq__(other)
```

Compare if two nodes are the same (reference equality).

## Parameters
- **other**: any

    The other object to compare with.

## Returns

bool
    True if both nodes are the same, False otherwise.

<a id="python_solutions.Node.Node.next_node"></a>

#### next\_node

```python
@property
def next_node()
```

Get the reference to the next node.

## Returns

Node or None
    The reference to the next node or None if it doesn't exist.

<a id="python_solutions.Node.Node.next_node"></a>

#### next\_node

```python
@next_node.setter
def next_node(next_node)
```

Set the reference to the next node.

## Parameters
- **next_node**: Node or None

    The next node to be set for the current node.

## Raises

TypeError
    If the provided next_node is of the wrong type.

<a id="python_solutions.Node.Node.data"></a>

#### data

```python
@property
def data()
```

Get or set the data stored in the node.

## Returns

any
    The data stored in the node.

<a id="python_solutions.Node.Node.data"></a>

#### data

```python
@data.setter
def data(data)
```

Set the data stored in the node.

## Parameters
- **data**: any

    The data to be stored in the node.

Queue Module

This module defines a Queue class representing a queue data structure with
a first-in-first-out (FIFO) ordering of elements. Elements are enqueued
to the back and dequeued from the front of the queue.

Classes
-------
Queue
    A class representing a queue data structure with enqueue and dequeue
    operations.

<a id="python_solutions.Queue.DoubleNode"></a>

## DoubleNode

<a id="python_solutions.Queue.Stack"></a>

## Stack

<a id="python_solutions.Queue.Queue"></a>

## Queue Objects

```python
class Queue(Stack)
```

Queue class

The Queue class represents a queue data structure
with a first-in-first-out (FIFO) ordering of elements.
Elements are added to the back (enqueued) and
removed from the front (dequeued) of the queue.

## Attributes

Inherits attributes from the Stack class.

## Methods

push(self, value)
    Enqueue an element to the back of the queue.

pop(self)
    Dequeue and return the element from the front of the queue.

<a id="python_solutions.Queue.Queue.push"></a>

#### push

```python
def push(value)
```

Enqueue an element to the back of the queue.

## Parameters
- **value**: any

    The element to be added to the back of the queue.

## Returns

None

<a id="python_solutions.Queue.Queue.pop"></a>

#### pop

```python
def pop()
```

Dequeue and return the element from the front of the queue.

## Returns

any
    The element removed from the front of the queue.

Quick Sort Module
=================

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

Segment Tree Module
===================

This module defines two classes, `SegmentTree` and `SegmentTreeOptimized`,
that implement a segment tree data structure.
A segment tree is a versatile data structure that allows for efficient
querying and updating of segments of an array.

Classes
-------
SegmentTree
    A class representing a segment tree.

SegmentTreeOptimized
    An optimized version of the segment tree class.

<a id="python_solutions.segment_tree.gcd"></a>

## gcd

<a id="python_solutions.segment_tree.Callable"></a>

## Callable

<a id="python_solutions.segment_tree.SegmentTree"></a>

## SegmentTree Objects

```python
class SegmentTree(list)
```

A class representing a segment tree.

## Attributes
- **n**: int

    The length of array on which SegmentTree is built.

- **tree_size**: int

    The size of the SegmentTree.

tree_`action`: list[float]
    SegmentTrees for each distinct operation `action`.

## Methods

__init__(self, arr: list) -> None
    Initializes a new instance of the `SegmentTree` class with
    the given array.

build_tree(self, current_index: int, left: int, right: int) -> None
    Builds the segment tree using a recursive function.

query(self, action: Callable, query_left: int, query_right: int) -> float
    Performs a query on the segment tree for the specified range
    (including query_left and query_right indexes) and action.

_query(self, current_index: int, segment_left: int,
- **segment_right**: int, action: Callable, query_left: int,

- **query_right**: int) -> float

    Recursively performs a query on the segment tree.

update(self, index: int, new_value: float) -> None
    Updates the value of a specified index in the segment tree.

_update(self, current_index: int, segment_left: int, segment_right: int,
- **index**: int, new_value: float) -> None

    Recursively updates the value of a specified index in the segment
    tree.

<a id="python_solutions.segment_tree.SegmentTree.__init__"></a>

#### \_\_init\_\_

```python
def __init__(arr: list[float]) -> None
```

Initializes a new instance of the `SegmentTree` class with the given
array.

## Parameters
- **arr**: list[float]

    An array to built the SegmentTree on.

## Returns

None

<a id="python_solutions.segment_tree.SegmentTree.build_tree"></a>

#### build\_tree

```python
def build_tree(current_index: int, left: int, right: int) -> None
```

Builds the segment tree using a recursive function.

## Parameters
- **current_index**: int

    Index for which the function currently calculates actions.

- **left_index**: int

    Left border of the tree with root in current_index.

- **right_index**: int

    Right border of the tree with root in current_index.

## Returns

None

<a id="python_solutions.segment_tree.SegmentTree.query"></a>

#### query

```python
def query(action: Callable, query_left: int, query_right: int) -> float
```

Performs a query on the segment tree for the specified range and
action.

## Parameters
- **action**: Callable

    Operation to query among available for the tree. If action is not
    among available (sum, min, max, gcd), raises an error.

- **query_left**: int

    Left border of the range, included in the query.

- **query_right**: int

    Right border of the range, included in the query.

## Returns

float
    The result of the query.

## Raises

KeyError
    If query is called to perform operation not among defined.

<a id="python_solutions.segment_tree.SegmentTree._query"></a>

#### \_query

```python
def _query(current_index, segment_left, segment_right, action, query_left,
           query_right) -> float
```

Recursively performs a query on the segment tree.

## Parameters
- **current_index**: int

    Index for which the function currently calculates actions.

- **segment_left**: int

    Left border of the segment with root in current_index.

- **segment_right**: int

    Right border of the segment with root in current_index.

- **action**: Callable

    Operation to query among available for the tree.

- **query_left**: int

    Left border of the range, included in the query.

- **query_right**: int

    Right border of the range, included in the query.

## Returns

float
    The result of the query.

<a id="python_solutions.segment_tree.SegmentTree.update"></a>

#### update

```python
def update(index: int, new_value: float) -> None
```

Updates the value of a specified index in the segment tree.

## Parameters
- **index**: int

    Index to update.

- **new_value**: float

    New value to assign to the specified index.

## Returns

None

<a id="python_solutions.segment_tree.SegmentTree._update"></a>

#### \_update

```python
def _update(current_index: int, segment_left: int, segment_right: int,
- **index**: int, new_value: float) -> None

```

Recursively updates the value of a specified index in the segment
tree.

## Parameters
- **current_index**: int

    Index for which the function currently calculates actions.

- **segment_left**: int

    Left border of the segment with root in current_index.

- **segment_right**: int

    Right border of the segment with root in current_index.

- **index**: int

    Index to update.

- **new_value**: float

    New value to assign to the specified index.

## Returns

None

<a id="python_solutions.segment_tree.SegmentTreeOptimized"></a>

## SegmentTreeOptimized Objects

```python
class SegmentTreeOptimized()
```

An optimized version of the segment tree class.

## Attributes
- **n**: int

    The length of array on which SegmentTree is built.

- **tree_size**: int

    The size of the SegmentTree.

- **tree**: list[list[float]]

    The main tree structure. Contains lists with the length equal to
    number of actions defined.

- **action**: list[Callable]

    A list where all defined operations are stored.

- **arr**: list[float]

    The list SegmentTreeOptimized is built on

- **neutral**: dict[Callable: float]

    The dict defining the neutral elements for each operation.

## Methods

__init__(self, arr) -> None
    Initializes a new instance of the `SegmentTreeOptimized` class with
    the given array.

determine_queries(self, left_index: int, right_index: int) ->
    tuple[Callable, Callable] | tuple[Callable, float] |
    tuple[float, float]
    Determines the queries for the left and right indices.

build_tree(self, arr: list[float], current_index: int,
- **left**: int, right: int, action: Callable | None = None) -> None

    Builds the segment tree using a recursive function.

query(self, action: Callable, query_left: int, query_right: int) -> float
    Performs a query on the segment tree for the specified range
    (including query_left and query_right indexes) and action.

_query(self, current_index: int, segment_left: int,
- **segment_right**: int, action: Callable, query_left: int,

- **query_right**: int) -> float

    Recursively performs a query on the segment tree.

update(self, index: int, new_value: float) -> None
    Updates the value of a specified index in the segment tree.

_update(self, current_index: int, segment_left: int,
- **segment_right**: int, index: int, new_value: float) -> None

    Recursively updates the value of a specified index in the segment
    tree.

new_action(self, func: Callable, neutral: float)
    Adds a new action to the segment tree and updates the
    tree accordingly.

<a id="python_solutions.segment_tree.SegmentTreeOptimized.__init__"></a>

#### \_\_init\_\_

```python
def __init__(arr) -> None
```

Initializes a new instance of the `SegmentTreeOptimized` class with
the given array.

## Parameters
- **arr**: list

    An array to build the SegmentTree on.

## Returns

None

<a id="python_solutions.segment_tree.SegmentTreeOptimized.determine_queries"></a>

#### determine\_queries

```python
def determine_queries(left_index, right_index) -> tuple[Callable, Callable] | tuple[Callable, float] | \
            tuple[float, float]
```

Determines the queries for the left and right indices.
Its purpose is to give the same looking calls for the queries
with only one element and with more than one element.

## Parameters
- **left_index**: int

    The left index.

- **right_index**: int

    The right index.

## Returns
- **left_query**: Callable

    A lambda function representing the query for the left index.

- **right_query**: Callable

    A lambda function representing the query for the right index.

<a id="python_solutions.segment_tree.SegmentTreeOptimized.build_tree"></a>

#### build\_tree

```python
def build_tree(arr: list,
- **current_index**: int,

- **left**: int,

- **right**: int,

- **action**: Callable | None = None) -> None

```

Builds the segment tree using a recursive function.

## Parameters
- **arr**: list

    The array on which the SegmentTreeOptimized is built.

- **current_index**: int

    Index for which the function currently calculates action.

- **left**: int

    Left border of the tree with root in current_index.

- **right**: int

    Right border of the tree with root in current_index.

- **action**: Callable, optional

    Operation to query among available for the tree.

## Returns

None

<a id="python_solutions.segment_tree.SegmentTreeOptimized.query"></a>

#### query

```python
def query(action: Callable, query_left: int, query_right: int) -> float
```

Performs a query on the segment tree for the specified range and
action.

## Parameters
- **action**: Callable

    Operation to query among available for the tree. If action is not
    among available, raises an error.

- **query_left**: int

    Left border of the range, included in the query.

- **query_right**: int

    Right border of the range, included in the query.

## Returns

float
    The result of the query.

<a id="python_solutions.segment_tree.SegmentTreeOptimized._query"></a>

#### \_query

```python
def _query(current_index: int, segment_left: int, segment_right: int,
- **action**: Callable, query_left: int, query_right: int) -> float

```

Recursively performs a query on the segment tree.

## Parameters
- **current_index**: int

    Index for which the function currently calculates actions.

- **segment_left**: int

    Left border of the segment with root in current_index.

- **segment_right**: int

    Right border of the segment with root in current_index.

- **action**: Callable

    Operation to query among available for the tree.

- **query_left**: int

    Left border of the range, included in the query.

- **query_right**: int

    Right border of the range, included in the query.

## Returns

float
    The result of the query.

<a id="python_solutions.segment_tree.SegmentTreeOptimized.update"></a>

#### update

```python
def update(index: int, new_value: float) -> None
```

Updates the value of a specified index in the segment tree.

## Parameters
- **index**: int

    Index to update.

- **new_value**: float

    New value to assign to the specified index.

## Returns

None

<a id="python_solutions.segment_tree.SegmentTreeOptimized._update"></a>

#### \_update

```python
def _update(current_index: int, segment_left: int, segment_right: int,
- **index**: int, new_value: float) -> None

```

Recursively updates the value of a specified index in the
segment tree.

## Parameters
- **current_index**: int

    Index for which the function currently calculates actions.

- **segment_left**: int

    Left border of the segment with root in current_index.

- **segment_right**: int

    Right border of the segment with root in current_index.

- **index**: int

    Index to update.

- **new_value**: float

    New value to assign to the specified index.

## Returns

None

<a id="python_solutions.segment_tree.SegmentTreeOptimized.new_action"></a>

#### new\_action

```python
def new_action(func: Callable, neutral: float) -> None
```

Adds a new action to the segment tree and updates the tree
accordingly.

## Parameters
- **func**: Callable

    The new action to add to the segment tree.

neutral
    The neutral element associated with the new action.

## Returns

None

Sparse table module
===================
This module defines a SparseTable class for efficient range queries on an
array. It allows you to quickly compute the minimum, maximum, and sum of
values within a specified range. The data structure is built on a tuple for
immutability, making it suitable for scenarios where the input array should
not be modified after construction.

Classes
-------
SparseTable
    A class for creating and querying a sparse table for efficient range
    queries.

<a id="python_solutions.sparse_table.math"></a>

## math

<a id="python_solutions.sparse_table.SparseTable"></a>

## SparseTable Objects

```python
class SparseTable(tuple)
```

A class for creating and querying a sparse table for efficient range
queries on an array.

## Attributes
- **arr**: list[float]

    The input array on which range queries will be performed.

## Methods

append(self, x: Any) -> None
    Raises an error, overwriting append for tuple, so that Sparse table
    would be completely unchangeable after creation.

extend(self, x: Any) -> None
    Raises an error, overwriting extend for tuple, so that Sparse table
    would be completely unchangeable after creation.

query_min(self, left: int, right: int) -> float
    Query the minimum value within a specified range, both parameters
    included.

query_max(self, left: int, right: int) -> float
    Query the maximum value within a specified range, both parameters
    included.

query_sum(self, left: int, right: int) -> float
    Query the cumulative sum of values within a specified range, both
    parameters included.

__new__(cls, arr: Iterable) -> SparseTable
    Create a new instance of SparseTable using tuple's __new__()

<a id="python_solutions.sparse_table.SparseTable.__init__"></a>

#### \_\_init\_\_

```python
def __init__(arr)
```

Initialize a SparseTable instance with the given input array.

## Parameters
- **arr**: list[float]

    The input array on which range queries will be performed.

## Returns

None

<a id="python_solutions.sparse_table.SparseTable.__new__"></a>

#### \_\_new\_\_

```python
def __new__(cls, arr)
```

Create a new SparseTable instance.

## Parameters
- **arr**: list[float]

    The input array on which range queries will be performed.

## Returns

SparseTable
    A new instance of the SparseTable class.

<a id="python_solutions.sparse_table.SparseTable.append"></a>

#### append

```python
def append(x)
```

This method raises a TypeError because SparseTable instances are
immutable and cannot be changed after creation.

## Parameters
- **x**: Any

    The element to be appended.

## Raises

TypeError
    SparseTable cannot be changed after creation.

## Returns

None

<a id="python_solutions.sparse_table.SparseTable.extend"></a>

#### extend

```python
def extend(x)
```

This method raises a TypeError because SparseTable instances are
immutable and cannot be changed after creation.

## Parameters
- **x**: Any

    The list with elements to append.

## Raises

TypeError
    SparseTable cannot be changed after creation.

## Returns

None

<a id="python_solutions.sparse_table.SparseTable.query_min"></a>

#### query\_min

```python
def query_min(left, right)
```

Query the minimum value within a specified range.

## Parameters
- **left**: int

    The left index of the range (inclusive).

- **right**: int

    The right index of the range (inclusive).

## Returns

float
    The minimum value within the specified range [left, right].

<a id="python_solutions.sparse_table.SparseTable.query_max"></a>

#### query\_max

```python
def query_max(left, right)
```

Query the maximum value within a specified range.

## Parameters
- **left**: int

    The left index of the range (inclusive).

- **right**: int

    The right index of the range (inclusive).

## Returns

float
    The maximum value within the specified range [left, right].

<a id="python_solutions.sparse_table.SparseTable.query_sum"></a>

#### query\_sum

```python
def query_sum(left, right)
```

Query the cumulative sum of values within a specified range.

## Parameters
- **left**: int

    The left index of the range (inclusive).

- **right**: int

    The right index of the range (inclusive).

## Returns

float
    The cumulative sum of values within the specified range
    [left, right].

Real Binary Search Module
=========================

This module provides a binary search function for finding an element at
a specified index in an array as if it was already sorted in ascending order.
The binary search algorithm uses a randomized pivot selection and partitioning
to efficiently search for the element.

Functions
---------
split_find(a, index)
    Searches for an element with the specified index in an array as if it was
    already sorted in ascending order. It is a wrapper for _split_find
    function.

split(array, pivot, left_edge, right_edge)
    Splits an array into two parts based on a pivot value. Elements less
    than the pivot are moved to the left subarray, and elements equal to
    or greater than the pivot are moved to the right subarray.

_split_find(array, left_edge, right_edge, index)
    Recursively finds the element at the specified index inside an array as
    if it were sorted in ascending order. It uses random pivot selection
    and the split function to partition the array while narrowing down
    the search range.

<a id="python_solutions.split_find.random"></a>

## random

<a id="python_solutions.split_find.split"></a>

#### split

```python
def split(array, pivot, left_edge, right_edge)
```

Splits an array into two parts based on a pivot value.

This function partitions the input array into two subarrays.
Elements less than pivot are moved to the left subarray,
and elements equal to pivot (within a small tolerance)
or greater are moved to the right subarray.

## Parameters
- **array**: list[float]

    The input array to be split and partially sorted.

- **pivot**: float

    The pivot value used for partitioning the array.

- **left_edge**: int

    The starting index of the subarray to be split.

- **right_edge**: int

    The ending index (exclusive) of the subarray to be split.

## Returns

tuple[int, int]
    A tuple containing the new left and right edges of the split subarrays.
    If all elements are moved to one side, it returns (0, 0).

<a id="python_solutions.split_find._split_find"></a>

#### \_split\_find

```python
def _split_find(array, left_edge, right_edge, index)
```

Recursively finds the element at the specified index
inside array as if that array would be sorted in ascending order.

This function recursively searches for the element
at the given index within the subarray defined by left_edge
and right_edge inside array.
It uses random pivot selection and the split function to partition
the array while narrowing down the search range.

## Parameters
- **array**: list[float]

    The input array in which to search for the element.

- **left_edge**: int

    The starting index of the subarray in which to search.

- **right_edge**: int

    The ending index (exclusive) of the subarray in which to search.

- **index**: int

    The target index of the element to find.

## Returns

float
    The element found at the specified index.

<a id="python_solutions.split_find.split_find"></a>

#### split\_find

```python
def split_find(a, index)
```

Searches for an element with the specified index in an array
as if it was already sorted in ascending order.

This function searches for the element at the specified index in
ascending order in the input array without fully sorting the array.
It uses the _split_find function to perform the search.
If an array is already sorted this algorithm becomes Binary search.
If not - average and worst cases lead to O(n^2) time complexity
(as if you would have to perform the entire quick sort before search).

## Parameters
- **a**: list[float]

    The input array in which to search for the element.

- **index**: int

    The target index of the element to find.

## Returns

float
    The element found at the specified 'index'.

Stack Module

This module provides a Python implementation of a stack data structure. The
stack follows the Last-In-First-Out (LIFO) principle, where the last element
added is the first one to be removed. This class provides methods to
manipulate and query the stack.

Classes
-------
Stack
    A stack data structure implemented using a doubly-linked list.

<a id="python_solutions.Stack.DoubleNode"></a>

## DoubleNode

<a id="python_solutions.Stack.Stack"></a>

## Stack Objects

```python
class Stack()
```

A Python implementation of a stack data structure using
a doubly-linked list.

The stack follows the Last-In-First-Out (LIFO) principle,
where the last element added is the first one to be removed.
This class provides methods to manipulate and query the stack.

## Attributes
- **head**: DoubleNode or None

    The top (front) of the stack. Default is None.

- **tail**: DoubleNode or None

    The bottom (back) of the stack. Default is None.

- **size**: int

    The number of elements in the stack.

## Methods

__init__(self) -> None
    Initializes an empty stack.

push(self, value) -> None
    Adds a new element to the back of the stack.

pop(self) -> Any | None
    Removes and returns the back element from the stack.

back(self) -> Any | None
    Retrieves the element at the back of the stack
    without removing it.

front(self) -> Any | None
    Retrieves the element at the top of the stack.

__len__(self) -> int
    Returns the number of elements currently in the stack.

<a id="python_solutions.Stack.Stack.__init__"></a>

#### \_\_init\_\_

```python
def __init__()
```

Initializes an empty stack.

<a id="python_solutions.Stack.Stack.push"></a>

#### push

```python
def push(value)
```

Adds a new element to the back of the stack.

## Parameters
- **value**: Any

    The value to be added to the stack.

## Returns

None

<a id="python_solutions.Stack.Stack.pop"></a>

#### pop

```python
def pop()
```

Removes and returns the back element from the stack.

## Returns

Any
    The removed element from the back of the stack.

<a id="python_solutions.Stack.Stack.back"></a>

#### back

```python
def back()
```

Retrieves the element at the back of the stack
without removing it.

## Returns

Any
    The element at the back of the stack.

<a id="python_solutions.Stack.Stack.front"></a>

#### front

```python
def front()
```

Retrieves the element at the top of the stack.

## Returns

Any
    The element at the top of the stack.

<a id="python_solutions.Stack.Stack.__len__"></a>

#### \_\_len\_\_

```python
def __len__()
```

Returns the number of elements currently in the stack.

## Returns

int
    The number of elements in the stack.

Ternary Search Module
=====================

This module provides two functions, `tern_search_min` and `tern_search_max`,
for finding the minimum and maximum values of a function within a specified
range, respectively. These search algorithms are suitable for cases where
the function has only one minimum or maximum value within the given range.

Functions
---------
tern_search_min(func, start, end, eps=1e-6)
    Find the minimum value of a function within a specified range.

tern_search_max(func, start, end, eps=1e-6)
    Find the maximum value of a function within a specified range.

<a id="python_solutions.ternary_search_extremum.tern_search_min"></a>

#### tern\_search\_min

```python
def tern_search_min(func, start, end, eps=1e-6)
```

Ternary search for finding the minimum value of a function
within a specified range.

This search algorithm is suitable for cases where the function has
only one minimum value within the given range [start, end].
This ternary search algorithm works with a time complexity of O(log2(n)),
where n is the number of times the epsilon (eps) can fit in the absolute
difference between the start and end positions.
It determines the local minimum by comparing the function's values
at two points within the search interval.

## Parameters
- **func**: callable

    The function for which to find the minimum value.

- **start**: float

    The start of the range for the search.

- **end**: float

    The end of the range for the search.

- **eps**: float, optional

    The epsilon parameter controlling the accuracy
    of search. Default is 1e-6.

## Returns

float
    The approximate x-coordinate of the minimum value of the function
    within the specified range.

<a id="python_solutions.ternary_search_extremum.tern_search_max"></a>

#### tern\_search\_max

```python
def tern_search_max(func, start, end, eps=1e-6)
```

Ternary search for finding the maximum value of a function
within a specified range.

This search algorithm is suitable for cases where the function has
only one maximum value within the given range [start, end].
This ternary search algorithm works with a time complexity of O(log2(n)),
where n is the number of times the epsilon (eps) can fit in the absolute
difference between the start and end positions.
It determines the local minimum by comparing the function's values
at two points within the search interval.

## Parameters
- **func**: callable

    The function for which to find the maximum value.

- **start**: float

    The start of the range for the search.

- **end**: float

    The end of the range for the search.

- **eps**: float, optional

    The epsilon parameter controlling the accuracy of the search.
    Default is 1e-6.

## Returns

float
    The approximate x-coordinate of the maximum value of the function
    within the specified range.

<a id="python_solutions.tests.test_array_count_sort.random"></a>

## random

<a id="python_solutions.tests.test_array_count_sort.array_count_sort"></a>

## array\_count\_sort

<a id="python_solutions.tests.test_array_count_sort.test_array_count_sort_case_one_elt_with_huge_variation"></a>

#### test\_array\_count\_sort\_case\_one\_elt\_with\_huge\_variation

```python
def test_array_count_sort_case_one_elt_with_huge_variation()
```

<a id="python_solutions.tests.test_array_count_sort.test_array_count_sort_case_one_elt_in_2_dim"></a>

#### test\_array\_count\_sort\_case\_one\_elt\_in\_2\_dim

```python
def test_array_count_sort_case_one_elt_in_2_dim()
```

<a id="python_solutions.tests.test_array_count_sort.test_array_count_sort_case_one_elt_in_2_dim_some_empty"></a>

#### test\_array\_count\_sort\_case\_one\_elt\_in\_2\_dim\_some\_empty

```python
def test_array_count_sort_case_one_elt_in_2_dim_some_empty()
```

<a id="python_solutions.tests.test_array_count_sort.test_array_count_sort_case_many_elts_no_key"></a>

#### test\_array\_count\_sort\_case\_many\_elts\_no\_key

```python
def test_array_count_sort_case_many_elts_no_key()
```

<a id="python_solutions.tests.test_array_count_sort.test_array_count_sort_case_many_elts_no_key_some_empty"></a>

#### test\_array\_count\_sort\_case\_many\_elts\_no\_key\_some\_empty

```python
def test_array_count_sort_case_many_elts_no_key_some_empty()
```

<a id="python_solutions.tests.test_array_count_sort.test_array_count_sort_case_many_elts_with_key_some_empty"></a>

#### test\_array\_count\_sort\_case\_many\_elts\_with\_key\_some\_empty

```python
def test_array_count_sort_case_many_elts_with_key_some_empty()
```

<a id="python_solutions.tests.test_avl_tree.pytest"></a>

## pytest

<a id="python_solutions.tests.test_avl_tree.random"></a>

## random

<a id="python_solutions.tests.test_avl_tree.math"></a>

## math

<a id="python_solutions.tests.test_avl_tree.AVLTree"></a>

## AVLTree

<a id="python_solutions.tests.test_avl_tree.avl_tree"></a>

#### avl\_tree

```python
@pytest.fixture
def avl_tree()
```

<a id="python_solutions.tests.test_avl_tree.test_insert"></a>

#### test\_insert

```python
def test_insert(avl_tree)
```

<a id="python_solutions.tests.test_avl_tree.test_delete"></a>

#### test\_delete

```python
def test_delete(avl_tree)
```

<a id="python_solutions.tests.test_avl_tree.test_delete_with_error"></a>

#### test\_delete\_with\_error

```python
def test_delete_with_error(avl_tree)
```

<a id="python_solutions.tests.test_avl_tree.test_search"></a>

#### test\_search

```python
def test_search(avl_tree)
```

<a id="python_solutions.tests.test_avl_tree.test_random_length_and_elts"></a>

#### test\_random\_length\_and\_elts

```python
def test_random_length_and_elts()
```

<a id="python_solutions.tests.test_bin_search.random"></a>

## random

<a id="python_solutions.tests.test_bin_search.bin_search"></a>

## bin\_search

<a id="python_solutions.tests.test_bin_search.test_bin_search_no_rec"></a>

#### test\_bin\_search\_no\_rec

```python
def test_bin_search_no_rec()
```

<a id="python_solutions.tests.test_bin_search.test_bin_search_with_rec"></a>

#### test\_bin\_search\_with\_rec

```python
def test_bin_search_with_rec()
```

<a id="python_solutions.tests.test_bloom_filter.pytest"></a>

## pytest

<a id="python_solutions.tests.test_bloom_filter.Bloom_filter"></a>

## Bloom\_filter

<a id="python_solutions.tests.test_bloom_filter.test_can_create_bloom_filter"></a>

#### test\_can\_create\_bloom\_filter

```python
def test_can_create_bloom_filter()
```

<a id="python_solutions.tests.test_bloom_filter.bf"></a>

#### bf

```python
@pytest.fixture
def bf()
```

<a id="python_solutions.tests.test_bloom_filter.test_can_add_to_bloom_filter"></a>

#### test\_can\_add\_to\_bloom\_filter

```python
def test_can_add_to_bloom_filter(bf)
```

<a id="python_solutions.tests.test_bloom_filter.test_can_create_bloom_filter_jenkins"></a>

#### test\_can\_create\_bloom\_filter\_jenkins

```python
def test_can_create_bloom_filter_jenkins()
```

<a id="python_solutions.tests.test_bloom_filter.test_false_positives_less_than_5_percent"></a>

#### test\_false\_positives\_less\_than\_5\_percent

```python
def test_false_positives_less_than_5_percent(bf)
```

<a id="python_solutions.tests.test_bloom_filter.test_bloom_filter_stress"></a>

#### test\_bloom\_filter\_stress

```python
def test_bloom_filter_stress()
```

<a id="python_solutions.tests.test_bloom_filter.test_long_strings_for_advanced_jenkins"></a>

#### test\_long\_strings\_for\_advanced\_jenkins

```python
def test_long_strings_for_advanced_jenkins()
```

<a id="python_solutions.tests.test_bloom_filter.test_raises_error_when_unrecognized_hash_passed"></a>

#### test\_raises\_error\_when\_unrecognized\_hash\_passed

```python
def test_raises_error_when_unrecognized_hash_passed()
```

<a id="python_solutions.tests.test_bst.pytest"></a>

## pytest

<a id="python_solutions.tests.test_bst.random"></a>

## random

<a id="python_solutions.tests.test_bst.BinarySearchTree"></a>

## BinarySearchTree

<a id="python_solutions.tests.test_bst.test_search_none"></a>

#### test\_search\_none

```python
def test_search_none()
```

<a id="python_solutions.tests.test_bst.test_insert_and_search_and_height"></a>

#### test\_insert\_and\_search\_and\_height

```python
def test_insert_and_search_and_height()
```

<a id="python_solutions.tests.test_bst.bst"></a>

#### bst

```python
@pytest.fixture
def bst()
```

<a id="python_solutions.tests.test_bst.test_in_order_traversal"></a>

#### test\_in\_order\_traversal

```python
def test_in_order_traversal(bst)
```

<a id="python_solutions.tests.test_bst.test_successor_predecessor"></a>

#### test\_successor\_predecessor

```python
def test_successor_predecessor(bst)
```

<a id="python_solutions.tests.test_bst.test_delete"></a>

#### test\_delete

```python
def test_delete(bst)
```

<a id="python_solutions.tests.test_bst.test_delete_with_error"></a>

#### test\_delete\_with\_error

```python
def test_delete_with_error(bst)
```

<a id="python_solutions.tests.test_bst.test_search"></a>

#### test\_search

```python
def test_search(bst)
```

<a id="python_solutions.tests.test_bst.test_height_advanced"></a>

#### test\_height\_advanced

```python
def test_height_advanced(bst)
```

<a id="python_solutions.tests.test_bst.test_find_min_and_max"></a>

#### test\_find\_min\_and\_max

```python
def test_find_min_and_max()
```

<a id="python_solutions.tests.test_bst.test_random_length_and_elts"></a>

#### test\_random\_length\_and\_elts

```python
def test_random_length_and_elts()
```

<a id="python_solutions.tests.test_bst.test_local_tree"></a>

#### test\_local\_tree

```python
def test_local_tree(bst)
```

<a id="python_solutions.tests.test_CyclicLinkedList.CyclicLinkedList"></a>

## CyclicLinkedList

<a id="python_solutions.tests.test_CyclicLinkedList.DoubleNode"></a>

## DoubleNode

<a id="python_solutions.tests.test_CyclicLinkedList.pytest"></a>

## pytest

<a id="python_solutions.tests.test_CyclicLinkedList.test_can_make_cll"></a>

#### test\_can\_make\_cll

```python
def test_can_make_cll()
```

<a id="python_solutions.tests.test_CyclicLinkedList.cll"></a>

#### cll

```python
@pytest.fixture()
def cll()
```

<a id="python_solutions.tests.test_CyclicLinkedList.head"></a>

#### head

```python
@pytest.fixture()
def head()
```

<a id="python_solutions.tests.test_CyclicLinkedList.test_can_initialize_cll_given_head"></a>

#### test\_can\_initialize\_cll\_given\_head

```python
def test_can_initialize_cll_given_head(head)
```

<a id="python_solutions.tests.test_CyclicLinkedList.test_initialize_from_chain"></a>

#### test\_initialize\_from\_chain

```python
def test_initialize_from_chain(head)
```

<a id="python_solutions.tests.test_CyclicLinkedList.cll_with_node"></a>

#### cll\_with\_node

```python
@pytest.fixture()
def cll_with_node(cll, head)
```

<a id="python_solutions.tests.test_CyclicLinkedList.test_insert_in_cll"></a>

#### test\_insert\_in\_cll

```python
def test_insert_in_cll(cll)
```

<a id="python_solutions.tests.test_CyclicLinkedList.test_insert_in_the_head"></a>

#### test\_insert\_in\_the\_head

```python
def test_insert_in_the_head(cll_with_node)
```

<a id="python_solutions.tests.test_CyclicLinkedList.test_raises_when_inserting_futher_than_append_goes"></a>

#### test\_raises\_when\_inserting\_futher\_than\_append\_goes

```python
def test_raises_when_inserting_futher_than_append_goes(cll_with_node)
```

<a id="python_solutions.tests.test_CyclicLinkedList.test_update_in_cll"></a>

#### test\_update\_in\_cll

```python
def test_update_in_cll(cll_with_node)
```

<a id="python_solutions.tests.test_CyclicLinkedList.test_erase_in_cll"></a>

#### test\_erase\_in\_cll

```python
def test_erase_in_cll(cll_with_node)
```

<a id="python_solutions.tests.test_CyclicLinkedList.test_erase_by_index_not_existing"></a>

#### test\_erase\_by\_index\_not\_existing

```python
def test_erase_by_index_not_existing(cll_with_node)
```

<a id="python_solutions.tests.test_CyclicLinkedList.test_erase_head"></a>

#### test\_erase\_head

```python
def test_erase_head(cll_with_node)
```

<a id="python_solutions.tests.test_CyclicLinkedList.test_erase_by_neg_index"></a>

#### test\_erase\_by\_neg\_index

```python
def test_erase_by_neg_index(cll_with_node)
```

<a id="python_solutions.tests.test_CyclicLinkedList.test_erase_tail"></a>

#### test\_erase\_tail

```python
def test_erase_tail(cll_with_node)
```

<a id="python_solutions.tests.test_CyclicLinkedList.test_raises_when_nothing_to_erase"></a>

#### test\_raises\_when\_nothing\_to\_erase

```python
def test_raises_when_nothing_to_erase(cll)
```

<a id="python_solutions.tests.test_CyclicLinkedList.test_insert_for_many_elements"></a>

#### test\_insert\_for\_many\_elements

```python
def test_insert_for_many_elements(cll)
```

<a id="python_solutions.tests.test_CyclicLinkedList.cll_with_many_nodes"></a>

#### cll\_with\_many\_nodes

```python
@pytest.fixture()
def cll_with_many_nodes(cll)
```

<a id="python_solutions.tests.test_CyclicLinkedList.test_can_update_many_elements"></a>

#### test\_can\_update\_many\_elements

```python
def test_can_update_many_elements(cll_with_many_nodes)
```

<a id="python_solutions.tests.test_CyclicLinkedList.test_erase_works_for_many_elements"></a>

#### test\_erase\_works\_for\_many\_elements

```python
def test_erase_works_for_many_elements(cll_with_many_nodes)
```

<a id="python_solutions.tests.test_CyclicLinkedList.test_insert_using_neg_index"></a>

#### test\_insert\_using\_neg\_index

```python
def test_insert_using_neg_index(cll_with_many_nodes)
```

<a id="python_solutions.tests.test_Deque.Deque"></a>

## Deque

<a id="python_solutions.tests.test_Deque.pytest"></a>

## pytest

<a id="python_solutions.tests.test_Deque.test_can_make_deck"></a>

#### test\_can\_make\_deck

```python
def test_can_make_deck()
```

<a id="python_solutions.tests.test_Deque.d"></a>

#### d

```python
@pytest.fixture()
def d()
```

<a id="python_solutions.tests.test_Deque.test_push_front_works_for_deque"></a>

#### test\_push\_front\_works\_for\_deque

```python
def test_push_front_works_for_deque(d)
```

<a id="python_solutions.tests.test_Deque.test_push_back_works_for_deque"></a>

#### test\_push\_back\_works\_for\_deque

```python
def test_push_back_works_for_deque(d)
```

<a id="python_solutions.tests.test_Deque.test_pop_front_works_for_deque"></a>

#### test\_pop\_front\_works\_for\_deque

```python
def test_pop_front_works_for_deque(d)
```

<a id="python_solutions.tests.test_Deque.test_pop_back_works_for_deque"></a>

#### test\_pop\_back\_works\_for\_deque

```python
def test_pop_back_works_for_deque(d)
```

<a id="python_solutions.tests.test_digit_sort.random"></a>

## random

<a id="python_solutions.tests.test_digit_sort.pytest"></a>

## pytest

<a id="python_solutions.tests.test_digit_sort.restore_to_nums"></a>

## restore\_to\_nums

<a id="python_solutions.tests.test_digit_sort.to_m_based"></a>

## to\_m\_based

<a id="python_solutions.tests.test_digit_sort.number"></a>

#### number

```python
@pytest.fixture()
def number()
```

<a id="python_solutions.tests.test_digit_sort.test_to_m_based_array"></a>

#### test\_to\_m\_based\_array

```python
def test_to_m_based_array(number)
```

<a id="python_solutions.tests.test_digit_sort.test_restore_to_nums"></a>

#### test\_restore\_to\_nums

```python
def test_restore_to_nums(number)
```

<a id="python_solutions.tests.test_DoubleNode.DoubleNode"></a>

## DoubleNode

<a id="python_solutions.tests.test_DoubleNode.prev"></a>

## prev

<a id="python_solutions.tests.test_DoubleNode.pytest"></a>

## pytest

<a id="python_solutions.tests.test_DoubleNode.dn"></a>

#### dn

```python
@pytest.fixture()
def dn()
```

<a id="python_solutions.tests.test_DoubleNode.test_doublenode_prev"></a>

#### test\_doublenode\_prev

```python
def test_doublenode_prev(dn)
```

<a id="python_solutions.tests.test_DoubleNode.test_doublenode_next"></a>

#### test\_doublenode\_next

```python
def test_doublenode_next(dn)
```

<a id="python_solutions.tests.test_DoubleNode.test_doublenode_str"></a>

#### test\_doublenode\_str

```python
def test_doublenode_str(dn)
```

<a id="python_solutions.tests.test_DoubleNode.test_doublenode_initialization_without_data_gives_blank_node"></a>

#### test\_doublenode\_initialization\_without\_data\_gives\_blank\_node

```python
def test_doublenode_initialization_without_data_gives_blank_node(dn)
```

<a id="python_solutions.tests.test_DoubleNode.test_raises_error_when_init_with_wrong_next_node"></a>

#### test\_raises\_error\_when\_init\_with\_wrong\_next\_node

```python
def test_raises_error_when_init_with_wrong_next_node()
```

<a id="python_solutions.tests.test_DoubleNode.test_raises_error_when_init_with_wrong_prev_node"></a>

#### test\_raises\_error\_when\_init\_with\_wrong\_prev\_node

```python
def test_raises_error_when_init_with_wrong_prev_node()
```

<a id="python_solutions.tests.test_DoubleNode.test_raises_error_when_trying_to_assign_wrong_prev_node"></a>

#### test\_raises\_error\_when\_trying\_to\_assign\_wrong\_prev\_node

```python
def test_raises_error_when_trying_to_assign_wrong_prev_node()
```

<a id="python_solutions.tests.test_dynamic_programmimg.pytest"></a>

## pytest

<a id="python_solutions.tests.test_dynamic_programmimg.subprocess"></a>

## subprocess

<a id="python_solutions.tests.test_dynamic_programmimg.random"></a>

## random

<a id="python_solutions.tests.test_dynamic_programmimg.string"></a>

## string

<a id="python_solutions.tests.test_dynamic_programmimg.c_int"></a>

## c\_int

<a id="python_solutions.tests.test_dynamic_programmimg.POINTER"></a>

## POINTER

<a id="python_solutions.tests.test_dynamic_programmimg.CDLL"></a>

## CDLL

<a id="python_solutions.tests.test_dynamic_programmimg.c_char"></a>

## c\_char

<a id="python_solutions.tests.test_dynamic_programmimg.DynamicProgrammingProblem"></a>

## DynamicProgrammingProblem

<a id="python_solutions.tests.test_dynamic_programmimg.KnapsackProblem"></a>

## KnapsackProblem

<a id="python_solutions.tests.test_dynamic_programmimg.DamerauLevensteinDistance"></a>

## DamerauLevensteinDistance

<a id="python_solutions.tests.test_dynamic_programmimg.LongestCommonSubsequence"></a>

## LongestCommonSubsequence

<a id="python_solutions.tests.test_dynamic_programmimg.LongestIncreasingSubsequence"></a>

## LongestIncreasingSubsequence

<a id="python_solutions.tests.test_dynamic_programmimg.maxSubarraySum"></a>

## maxSubarraySum

<a id="python_solutions.tests.test_dynamic_programmimg.TravellingSalesmanProblem"></a>

## TravellingSalesmanProblem

<a id="python_solutions.tests.test_dynamic_programmimg.test_dp_class_solve_raises"></a>

#### test\_dp\_class\_solve\_raises

```python
def test_dp_class_solve_raises()
```

<a id="python_solutions.tests.test_dynamic_programmimg.generate_test_cases_with_output_for_knapsack"></a>

#### generate\_test\_cases\_with\_output\_for\_knapsack

```python
def generate_test_cases_with_output_for_knapsack(n_start=5,
                                                 n_end=100,
                                                 r_start=10,
                                                 r_end=1000,
                                                 t_start=1,
                                                 t_end=16,
                                                 i_start=0,
                                                 i_end=200,
                                                 S_start=100,
                                                 S_end=2000)
```

<a id="python_solutions.tests.test_dynamic_programmimg.generate_test_cases"></a>

#### generate\_test\_cases

```python
def generate_test_cases(function, amount=20)
```

<a id="python_solutions.tests.test_dynamic_programmimg.test_knapsack_problem"></a>

#### test\_knapsack\_problem

```python
@pytest.mark.parametrize(
    "test_input, test_output",
    generate_test_cases(generate_test_cases_with_output_for_knapsack, 20) + [
        # bounds
        (([], [], 0), 0),
        (([12], [1], 0), 0),
        (([15, 1, 12], [10000, 1, 0], 14), 1)
    ])
def test_knapsack_problem(test_input, test_output)
```

<a id="python_solutions.tests.test_dynamic_programmimg.test_damerau_levenstein_bounds"></a>

#### test\_damerau\_levenstein\_bounds

```python
def test_damerau_levenstein_bounds()
```

<a id="python_solutions.tests.test_dynamic_programmimg.generate_test_cases_with_output_for_damerau_levenstein"></a>

#### generate\_test\_cases\_with\_output\_for\_damerau\_levenstein

```python
def generate_test_cases_with_output_for_damerau_levenstein(
        str1_len=10, str2_len=10)
```

<a id="python_solutions.tests.test_dynamic_programmimg.test_damerau_levenstein"></a>

#### test\_damerau\_levenstein

```python
@pytest.mark.parametrize(
    "test_input, test_output",
    generate_test_cases(generate_test_cases_with_output_for_damerau_levenstein,
                        20) + [
                            (('', ''), 0),
                            # transpositional check
                            (('10', '01'), 1),
                            (('011', '101'), 1),
                            (('1023456789', '01wertyuio'), 9),
                            (('abcdef', 'abcfad'), 3)
                        ])
def test_damerau_levenstein(test_input, test_output)
```

<a id="python_solutions.tests.test_dynamic_programmimg.test_lcs_symmetry"></a>

#### test\_lcs\_symmetry

```python
def test_lcs_symmetry()
```

<a id="python_solutions.tests.test_dynamic_programmimg.test_some_lcs_test_cases"></a>

#### test\_some\_lcs\_test\_cases

```python
@pytest.mark.parametrize(
    'test_input, test_output',
    [
        (('workattech', 'branch'), 4),
        (('helloworld', 'playword'), 5),
        (('hello', 'hello'), 5),
        (('abc', 'def'), 0),
        # bounds
        (('', ''), 0),
        (('abc', ''), 0),
        (('', 'abc'), 0),
        (('abc', 'abc'), 3)
    ])
def test_some_lcs_test_cases(test_input, test_output)
```

<a id="python_solutions.tests.test_dynamic_programmimg.test_some_lis_test_cases"></a>

#### test\_some\_lis\_test\_cases

```python
@pytest.mark.parametrize(
    'test_input, test_output',
    [(([10, 20, 2, 5, 3, 8, 8, 25, 6]), 4),
     (([10, -63, 7, -50, 32, -9, -3]), 4), (([71, 0, 4, 42, -31, 4, -42]), 3),
     (([77, 0, -2, 25, 1, 70]), 3), (([2, 2, 1, 5, 7, -50, 80]), 4),
     (([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]), 6),
     (([5, 8, 3, 7, 9, 1]), 3), (([]), 0), (([random.randint(0, 100)]), 1),
     (([1, 0, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 10),
     ((1, 0, 2, 3, 4, 5, 6, 7, 8, 10, 9), 9)])
def test_some_lis_test_cases(test_input, test_output)
```

<a id="python_solutions.tests.test_dynamic_programmimg.arr"></a>

#### arr

<a id="python_solutions.tests.test_dynamic_programmimg.queries"></a>

#### queries

<a id="python_solutions.tests.test_dynamic_programmimg.test_max_subarray_sum_init"></a>

#### test\_max\_subarray\_sum\_init

```python
@pytest.mark.parametrize('arr, queries', [(arr, queries)])
def test_max_subarray_sum_init(arr, queries)
```

<a id="python_solutions.tests.test_dynamic_programmimg.test_max_subarray_sum_solve"></a>

#### test\_max\_subarray\_sum\_solve

```python
@pytest.mark.parametrize('arr, queries', [(arr, queries)])
def test_max_subarray_sum_solve(arr, queries)
```

<a id="python_solutions.tests.test_dynamic_programmimg.test_max_subarray_sum_empty"></a>

#### test\_max\_subarray\_sum\_empty

```python
@pytest.mark.parametrize('arr, queries', [([], [])])
def test_max_subarray_sum_empty(arr, queries)
```

<a id="python_solutions.tests.test_dynamic_programmimg.test_max_subarray_sum_one"></a>

#### test\_max\_subarray\_sum\_one

```python
@pytest.mark.parametrize('arr, queries', [([5], [(0, 0)])])
def test_max_subarray_sum_one(arr, queries)
```

<a id="python_solutions.tests.test_dynamic_programmimg.test_travelling_salesman"></a>

#### test\_travelling\_salesman

```python
def test_travelling_salesman()
```

<a id="python_solutions.tests.test_edit_distance.pytest"></a>

## pytest

<a id="python_solutions.tests.test_edit_distance.edit_distance"></a>

## edit\_distance

<a id="python_solutions.tests.test_edit_distance.jaro_distance"></a>

## jaro\_distance

<a id="python_solutions.tests.test_edit_distance.hamming_distance"></a>

## hamming\_distance

<a id="python_solutions.tests.test_edit_distance.test_jaro_distance"></a>

#### test\_jaro\_distance

```python
@pytest.mark.parametrize(
    'str1, str2, output',
    [
        ('hello', 'holla', 0.73333333),
        ('cat', 'cat', 1.0),
        ('apple', 'banana', 0.45555555),
        # bounds
        ('', 'abc', 0),
        ('abc', '', 0),
        ('', '', 0),
        ('cattatat', 'actatata', 0.7738095),
        ('abc', 'def', 0)
    ])
def test_jaro_distance(str1, str2, output)
```

<a id="python_solutions.tests.test_edit_distance.test_hamming_distance"></a>

#### test\_hamming\_distance

```python
@pytest.mark.parametrize("input1, input2, output",
                         [("karolin", "kathrin", 3),
                          ("karolina", "kathrine", 4),
                          ("1011101", "1001001", 2)])
def test_hamming_distance(input1, input2, output)
```

<a id="python_solutions.tests.test_edit_distance.test_hamming_error"></a>

#### test\_hamming\_error

```python
def test_hamming_error()
```

<a id="python_solutions.tests.test_edit_distance.test_edit_distance"></a>

#### test\_edit\_distance

```python
@pytest.mark.parametrize("input1, input2, method, expected",
                         [("hello", "holla", "jaro", 0.73333333),
                          ("apple", "banana", "jaro", 0.45555555),
                          ("karolin", "kathrin", "hamming", 3),
                          ("karolina", "kathrine", "hamming", 4),
                          ("kitten", "sitting", "dl", 3),
                          ("flaw", "lawn", "dl", 2),
                          ("kitten", "sitting", "lcs", 4),
                          ("flaw", "lawn", "lcs", 3)])
def test_edit_distance(input1, input2, method, expected)
```

<a id="python_solutions.tests.test_graph.pytest"></a>

## pytest

<a id="python_solutions.tests.test_graph.copy"></a>

## copy

<a id="python_solutions.tests.test_graph.logging"></a>

## logging

<a id="python_solutions.tests.test_graph.random"></a>

## random

<a id="python_solutions.tests.test_graph.GraphNode"></a>

## GraphNode

<a id="python_solutions.tests.test_graph.WeightedGraphNode"></a>

## WeightedGraphNode

<a id="python_solutions.tests.test_graph.Edge"></a>

## Edge

<a id="python_solutions.tests.test_graph.Graph"></a>

## Graph

<a id="python_solutions.tests.test_graph.WeightedGraph"></a>

## WeightedGraph

<a id="python_solutions.tests.test_graph.test_can_create_everything"></a>

#### test\_can\_create\_everything

```python
def test_can_create_everything()
```

<a id="python_solutions.tests.test_graph.test_undirected_graph_node_workes_well"></a>

#### test\_undirected\_graph\_node\_workes\_well

```python
def test_undirected_graph_node_workes_well()
```

<a id="python_solutions.tests.test_graph.graphs"></a>

#### graphs

```python
@pytest.fixture
def graphs()
```

<a id="python_solutions.tests.test_graph.nodes"></a>

#### nodes

```python
@pytest.fixture
def nodes()
```

<a id="python_solutions.tests.test_graph.test_graphs_can_accept_vertex"></a>

#### test\_graphs\_can\_accept\_vertex

```python
def test_graphs_can_accept_vertex(graphs, nodes)
```

<a id="python_solutions.tests.test_graph.nodes2"></a>

#### nodes2

```python
@pytest.fixture
def nodes2()
```

<a id="python_solutions.tests.test_graph.test_graphs_can_accept_two_unconnected_vertices"></a>

#### test\_graphs\_can\_accept\_two\_unconnected\_vertices

```python
def test_graphs_can_accept_two_unconnected_vertices(graphs, nodes, nodes2)
```

<a id="python_solutions.tests.test_graph.test_find_kwarg_data"></a>

#### test\_find\_kwarg\_data

```python
def test_find_kwarg_data(graphs, nodes)
```

<a id="python_solutions.tests.test_graph.test_find_kwarg_with_edges"></a>

#### test\_find\_kwarg\_with\_edges

```python
def test_find_kwarg_with_edges(graphs, nodes)
```

<a id="python_solutions.tests.test_graph.uncon2"></a>

#### uncon2

```python
@pytest.fixture
def uncon2(graphs, nodes, nodes2)
```

<a id="python_solutions.tests.test_graph.test_can_remove_vertices_by_index"></a>

#### test\_can\_remove\_vertices\_by\_index

```python
@pytest.mark.parametrize('index_rem, all_vertices, first', [(0, ['4'], '4'),
                                                            (1, ['3'], '3')])
def test_can_remove_vertices_by_index(uncon2, index_rem, all_vertices, first)
```

<a id="python_solutions.tests.test_graph.test_can_remove_vertices_by_data"></a>

#### test\_can\_remove\_vertices\_by\_data

```python
@pytest.mark.parametrize('data_rem, all_vertices, first, second, index',
                         [(3, ['4'], '4', 4, 1), (4, ['3'], '3', 3, 0)])
def test_can_remove_vertices_by_data(uncon2, data_rem, all_vertices, first,
                                     second, index)
```

<a id="python_solutions.tests.test_graph.test_raises_when_no_data_or_index_specified_in_remove"></a>

#### test\_raises\_when\_no\_data\_or\_index\_specified\_in\_remove

```python
def test_raises_when_no_data_or_index_specified_in_remove(uncon2)
```

<a id="python_solutions.tests.test_graph.test_add_edge_between_vertices_undir"></a>

#### test\_add\_edge\_between\_vertices\_undir

```python
@pytest.mark.parametrize('front, back', [(0, 1), (1, 0)])
def test_add_edge_between_vertices_undir(uncon2, front, back)
```

<a id="python_solutions.tests.test_graph.test_add_edge_between_vertices_wei"></a>

#### test\_add\_edge\_between\_vertices\_wei

```python
@pytest.mark.parametrize('direction, weight', [(0, 3), (0, []), (1, 4),
                                               (1, [])])
def test_add_edge_between_vertices_wei(uncon2, direction, weight)
```

<a id="python_solutions.tests.test_graph.test_graphs_can_accept_two_connected_vertices"></a>

#### test\_graphs\_can\_accept\_two\_connected\_vertices

```python
def test_graphs_can_accept_two_connected_vertices(graphs, nodes)
```

<a id="python_solutions.tests.test_graph.con2"></a>

#### con2

```python
@pytest.fixture
def con2(graphs)
```

<a id="python_solutions.tests.test_graph.test_remove_edge"></a>

#### test\_remove\_edge

```python
@pytest.mark.parametrize('front, back', [(0, 1), (1, 0)])
def test_remove_edge(con2, front, back)
```

<a id="python_solutions.tests.test_graph.test_remove_vertex"></a>

#### test\_remove\_vertex

```python
@pytest.mark.parametrize('params', [({
    'index': 0
}), ({
    'index': 1
}), ({
    'data': 3
}), ({
    'data': 4
})])
def test_remove_vertex(con2, params)
```

<a id="python_solutions.tests.test_graph.test_add_vertices_manipulate_edges_remove_vertices"></a>

#### test\_add\_vertices\_manipulate\_edges\_remove\_vertices

```python
def test_add_vertices_manipulate_edges_remove_vertices()
```

<a id="python_solutions.tests.test_graph.weights"></a>

#### weights

<a id="python_solutions.tests.test_graph.con5"></a>

#### con5

```python
@pytest.fixture
def con5()
```

<a id="python_solutions.tests.test_graph.bfs_graph"></a>

#### bfs\_graph

```python
@pytest.fixture
def bfs_graph()
```

<a id="python_solutions.tests.test_graph.test_bfs"></a>

#### test\_bfs

```python
def test_bfs(uncon2, con2, con5, bfs_graph)
```

<a id="python_solutions.tests.test_graph.test_adjancency_matrix"></a>

#### test\_adjancency\_matrix

```python
def test_adjancency_matrix(con5)
```

<a id="python_solutions.tests.test_graph.test_cycles_detector"></a>

#### test\_cycles\_detector

```python
def test_cycles_detector(uncon2, con5, bfs_graph)
```

<a id="python_solutions.tests.test_graph.test_topo_sort"></a>

#### test\_topo\_sort

```python
def test_topo_sort(bfs_graph)
```

<a id="python_solutions.tests.test_graph.test_single_node"></a>

#### test\_single\_node

```python
def test_single_node()
```

<a id="python_solutions.tests.test_graph.test_two_nodes_no_edge"></a>

#### test\_two\_nodes\_no\_edge

```python
def test_two_nodes_no_edge()
```

<a id="python_solutions.tests.test_graph.test_simple_cycle"></a>

#### test\_simple\_cycle

```python
def test_simple_cycle()
```

<a id="python_solutions.tests.test_graph.graph"></a>

#### graph

```python
@pytest.fixture
def graph()
```

<a id="python_solutions.tests.test_graph.test_multiple_scc"></a>

#### test\_multiple\_scc

```python
def test_multiple_scc(graph)
```

<a id="python_solutions.tests.test_graph.test_complex_graph"></a>

#### test\_complex\_graph

```python
def test_complex_graph(graph)
```

<a id="python_solutions.tests.test_graph.test_edge_cases"></a>

#### test\_edge\_cases

```python
def test_edge_cases()
```

<a id="python_solutions.tests.test_graph.test_dijkstra_undir"></a>

#### test\_dijkstra\_undir

```python
@pytest.mark.parametrize('graph_type', [Graph, WeightedGraph])
def test_dijkstra_undir(graph_type)
```

<a id="python_solutions.tests.test_graph.test_bellman_ford"></a>

#### test\_bellman\_ford

```python
def test_bellman_ford()
```

<a id="python_solutions.tests.test_graph.test_simple_flow"></a>

#### test\_simple\_flow

```python
@pytest.mark.parametrize('algo', ['dinics', 'gt'])
def test_simple_flow(graph, algo)
```

<a id="python_solutions.tests.test_graph.test_multiple_flows"></a>

#### test\_multiple\_flows

```python
@pytest.mark.parametrize('algo', ['dinics', 'gt'])
def test_multiple_flows(graph, algo)
```

<a id="python_solutions.tests.test_graph.test_no_flow"></a>

#### test\_no\_flow

```python
@pytest.mark.parametrize('algo', ['dinics', 'gt'])
def test_no_flow(algo)
```

<a id="python_solutions.tests.test_graph.test_max_flow"></a>

#### test\_max\_flow

```python
@pytest.mark.parametrize('algo', ['dinics', 'gt'])
def test_max_flow(graph, algo)
```

<a id="python_solutions.tests.test_graph.test_backflow"></a>

#### test\_backflow

```python
@pytest.mark.parametrize('algo', ['dinics', 'gt'])
def test_backflow(graph, algo)
```

<a id="python_solutions.tests.test_graph.test_algorithm_mst_correctness"></a>

#### test\_algorithm\_mst\_correctness

```python
@pytest.mark.parametrize('algo', ['prims', 'kruskals'])
def test_algorithm_mst_correctness(algo)
```

<a id="python_solutions.tests.test_graph.test_algorithm_mst_disconnected_graph"></a>

#### test\_algorithm\_mst\_disconnected\_graph

```python
@pytest.mark.parametrize('algo', ['prims'])
def test_algorithm_mst_disconnected_graph(algo)
```

<a id="python_solutions.tests.test_graph.test_algorithm_mst_empty_graph"></a>

#### test\_algorithm\_mst\_empty\_graph

```python
@pytest.mark.parametrize('algo', ['prims', 'kruskals'])
def test_algorithm_mst_empty_graph(algo)
```

<a id="python_solutions.tests.test_graph.test_algorithm_mst_uniform_weights"></a>

#### test\_algorithm\_mst\_uniform\_weights

```python
@pytest.mark.parametrize('algo', ['prims', 'kruskals'])
def test_algorithm_mst_uniform_weights(algo)
```

<a id="python_solutions.tests.test_graph.test_mst_complex_graph"></a>

#### test\_mst\_complex\_graph

```python
def test_mst_complex_graph()
```

<a id="python_solutions.tests.test_graph.test_graph_vertices_and_edges_coloring"></a>

#### test\_graph\_vertices\_and\_edges\_coloring

```python
def test_graph_vertices_and_edges_coloring()
```

<a id="python_solutions.tests.test_graph.test_complex_graph_coloring"></a>

#### test\_complex\_graph\_coloring

```python
def test_complex_graph_coloring()
```

<a id="python_solutions.tests.test_hashtable.HashTable_closed"></a>

## HashTable\_closed

<a id="python_solutions.tests.test_hashtable.gen_primes"></a>

## gen\_primes

<a id="python_solutions.tests.test_hashtable.HashTable_open"></a>

## HashTable\_open

<a id="python_solutions.tests.test_hashtable.poly_hash"></a>

## poly\_hash

<a id="python_solutions.tests.test_hashtable.random"></a>

## random

<a id="python_solutions.tests.test_hashtable.pytest"></a>

## pytest

<a id="python_solutions.tests.test_hashtable.test_gen_primes"></a>

#### test\_gen\_primes

```python
def test_gen_primes()
```

<a id="python_solutions.tests.test_hashtable.test_hashtable_closed_runs"></a>

#### test\_hashtable\_closed\_runs

```python
def test_hashtable_closed_runs()
```

<a id="python_solutions.tests.test_hashtable.ht"></a>

#### ht

```python
@pytest.fixture()
def ht()
```

<a id="python_solutions.tests.test_hashtable.test_setter_in_hashtable_for_the_first_element"></a>

#### test\_setter\_in\_hashtable\_for\_the\_first\_element

```python
def test_setter_in_hashtable_for_the_first_element(ht)
```

<a id="python_solutions.tests.test_hashtable.test_setter_in_hashtable_for_the_second_element"></a>

#### test\_setter\_in\_hashtable\_for\_the\_second\_element

```python
def test_setter_in_hashtable_for_the_second_element(ht)
```

<a id="python_solutions.tests.test_hashtable.test_ht_handles_collisions"></a>

#### test\_ht\_handles\_collisions

```python
def test_ht_handles_collisions(ht)
```

<a id="python_solutions.tests.test_hashtable.test_cannot_set_size_and_capacity_for_ht_after_init"></a>

#### test\_cannot\_set\_size\_and\_capacity\_for\_ht\_after\_init

```python
def test_cannot_set_size_and_capacity_for_ht_after_init(ht)
```

<a id="python_solutions.tests.test_hashtable.ht_with_samples"></a>

#### ht\_with\_samples

```python
@pytest.fixture()
def ht_with_samples(ht)
```

<a id="python_solutions.tests.test_hashtable.test_property_pairs_getter"></a>

#### test\_property\_pairs\_getter

```python
def test_property_pairs_getter(ht_with_samples)
```

<a id="python_solutions.tests.test_hashtable.test_property_pairs_setitem"></a>

#### test\_property\_pairs\_setitem

```python
def test_property_pairs_setitem(ht_with_samples)
```

<a id="python_solutions.tests.test_hashtable.test_property_pairs_setter"></a>

#### test\_property\_pairs\_setter

```python
def test_property_pairs_setter(ht_with_samples)
```

<a id="python_solutions.tests.test_hashtable.test_deletion_in_ht"></a>

#### test\_deletion\_in\_ht

```python
def test_deletion_in_ht(ht_with_samples)
```

<a id="python_solutions.tests.test_hashtable.test_update_in_ht"></a>

#### test\_update\_in\_ht

```python
def test_update_in_ht(ht_with_samples)
```

<a id="python_solutions.tests.test_hashtable.test_to_dict_closed"></a>

#### test\_to\_dict\_closed

```python
def test_to_dict_closed(ht_with_samples)
```

<a id="python_solutions.tests.test_hashtable.test_search_in_ht"></a>

#### test\_search\_in\_ht

```python
def test_search_in_ht(ht_with_samples)
```

<a id="python_solutions.tests.test_hashtable.test_contains_in_ht"></a>

#### test\_contains\_in\_ht

```python
def test_contains_in_ht(ht_with_samples)
```

<a id="python_solutions.tests.test_hashtable.test_getitem_raises_for_absent_element"></a>

#### test\_getitem\_raises\_for\_absent\_element

```python
def test_getitem_raises_for_absent_element(ht_with_samples)
```

<a id="python_solutions.tests.test_hashtable.test_str_and_repr"></a>

#### test\_str\_and\_repr

```python
def test_str_and_repr(ht_with_samples)
```

<a id="python_solutions.tests.test_hashtable.test_from_dict"></a>

#### test\_from\_dict

```python
def test_from_dict(ht_with_samples)
```

<a id="python_solutions.tests.test_hashtable.test_ht_with_different_hashes"></a>

#### test\_ht\_with\_different\_hashes

```python
def test_ht_with_different_hashes()
```

<a id="python_solutions.tests.test_hashtable.test_ht_with_poly_hash_as_callable"></a>

#### test\_ht\_with\_poly\_hash\_as\_callable

```python
def test_ht_with_poly_hash_as_callable()
```

<a id="python_solutions.tests.test_hashtable.test_can_create_ht_open"></a>

#### test\_can\_create\_ht\_open

```python
def test_can_create_ht_open()
```

<a id="python_solutions.tests.test_hashtable.ht_open"></a>

#### ht\_open

```python
@pytest.fixture()
def ht_open()
```

<a id="python_solutions.tests.test_hashtable.test_setitem_and_getitem_in_ht"></a>

#### test\_setitem\_and\_getitem\_in\_ht

```python
def test_setitem_and_getitem_in_ht(ht_open)
```

<a id="python_solutions.tests.test_hashtable.ht_open_with_samples"></a>

#### ht\_open\_with\_samples

```python
@pytest.fixture
def ht_open_with_samples(ht_open)
```

<a id="python_solutions.tests.test_hashtable.test_property_elements_defensive_copy"></a>

#### test\_property\_elements\_defensive\_copy

```python
def test_property_elements_defensive_copy(ht_open_with_samples)
```

<a id="python_solutions.tests.test_hashtable.test_property_elements_setitem"></a>

#### test\_property\_elements\_setitem

```python
def test_property_elements_setitem(ht_open_with_samples)
```

<a id="python_solutions.tests.test_hashtable.test_set_elements"></a>

#### test\_set\_elements

```python
def test_set_elements(ht_open_with_samples)
```

<a id="python_solutions.tests.test_hashtable.test_update_in_ht_open"></a>

#### test\_update\_in\_ht\_open

```python
def test_update_in_ht_open(ht_open_with_samples)
```

<a id="python_solutions.tests.test_hashtable.test_errors_in_update_and_getitem"></a>

#### test\_errors\_in\_update\_and\_getitem

```python
def test_errors_in_update_and_getitem(ht_open_with_samples)
```

<a id="python_solutions.tests.test_hashtable.test_search_returns_false_when_no_elements_found"></a>

#### test\_search\_returns\_false\_when\_no\_elements\_found

```python
def test_search_returns_false_when_no_elements_found(ht_open_with_samples)
```

<a id="python_solutions.tests.test_hashtable.test_to_dict_open"></a>

#### test\_to\_dict\_open

```python
def test_to_dict_open(ht_open)
```

<a id="python_solutions.tests.test_hashtable_stresses.pytest"></a>

## pytest

<a id="python_solutions.tests.test_hashtable_stresses.HashTable_closed"></a>

## HashTable\_closed

<a id="python_solutions.tests.test_hashtable_stresses.HashTable_open"></a>

## HashTable\_open

<a id="python_solutions.tests.test_hashtable_stresses.ht"></a>

#### ht

```python
@pytest.fixture()
def ht()
```

<a id="python_solutions.tests.test_hashtable_stresses.test_stress_ht_closed"></a>

#### test\_stress\_ht\_closed

```python
def test_stress_ht_closed(ht)
```

<a id="python_solutions.tests.test_hashtable_stresses.ht_open"></a>

#### ht\_open

```python
@pytest.fixture()
def ht_open()
```

<a id="python_solutions.tests.test_hashtable_stresses.test_stress_ht_open"></a>

#### test\_stress\_ht\_open

```python
def test_stress_ht_open(ht_open)
```

<a id="python_solutions.tests.test_heap.random"></a>

## random

<a id="python_solutions.tests.test_heap.logging"></a>

## logging

<a id="python_solutions.tests.test_heap.pytest"></a>

## pytest

<a id="python_solutions.tests.test_heap.Heap"></a>

## Heap

<a id="python_solutions.tests.test_heap.heap_sort"></a>

## heap\_sort

<a id="python_solutions.tests.test_heap.test_can_create_heap"></a>

#### test\_can\_create\_heap

```python
def test_can_create_heap()
```

<a id="python_solutions.tests.test_heap.test_boundary_cases"></a>

#### test\_boundary\_cases

```python
def test_boundary_cases()
```

<a id="python_solutions.tests.test_heap.test_heap_sort"></a>

#### test\_heap\_sort

```python
def test_heap_sort()
```

<a id="python_solutions.tests.test_heap.test_repr"></a>

#### test\_repr

```python
def test_repr()
```

<a id="python_solutions.tests.test_hyperloglog.pytest"></a>

## pytest

<a id="python_solutions.tests.test_hyperloglog.HyperLogLog"></a>

## HyperLogLog

<a id="python_solutions.tests.test_hyperloglog.test_can_create_hyperloglog"></a>

#### test\_can\_create\_hyperloglog

```python
def test_can_create_hyperloglog()
```

<a id="python_solutions.tests.test_hyperloglog.test_cardinality"></a>

#### test\_cardinality

```python
@pytest.mark.parametrize(
    'precision, length',
    [
        (14, 10),
        (18, 50000)  #,
        #(25, 5000000)
    ])
def test_cardinality(precision, length)
```

<a id="python_solutions.tests.test_insert_sort.random"></a>

## random

<a id="python_solutions.tests.test_insert_sort.patch"></a>

## patch

<a id="python_solutions.tests.test_insert_sort.test_import_error_for_quick"></a>

#### test\_import\_error\_for\_quick

```python
def test_import_error_for_quick()
```

<a id="python_solutions.tests.test_insert_sort.test_quick_sort_median_of_medians"></a>

#### test\_quick\_sort\_median\_of\_medians

```python
def test_quick_sort_median_of_medians()
```

<a id="python_solutions.tests.test_LinkedList.LinkedList"></a>

## LinkedList

<a id="python_solutions.tests.test_LinkedList.Node"></a>

## Node

<a id="python_solutions.tests.test_LinkedList.pytest"></a>

## pytest

<a id="python_solutions.tests.test_LinkedList.test_can_create_blank_linkedlist"></a>

#### test\_can\_create\_blank\_linkedlist

```python
def test_can_create_blank_linkedlist()
```

<a id="python_solutions.tests.test_LinkedList.blank_ll"></a>

#### blank\_ll

```python
@pytest.fixture()
def blank_ll()
```

<a id="python_solutions.tests.test_LinkedList.test_no_nodes_size_of_ll_exists"></a>

#### test\_no\_nodes\_size\_of\_ll\_exists

```python
def test_no_nodes_size_of_ll_exists(blank_ll)
```

<a id="python_solutions.tests.test_LinkedList.test_no_nodes_head_of_ll_exists"></a>

#### test\_no\_nodes\_head\_of\_ll\_exists

```python
def test_no_nodes_head_of_ll_exists(blank_ll)
```

<a id="python_solutions.tests.test_LinkedList.test_no_nodes_tail_of_ll_exists"></a>

#### test\_no\_nodes\_tail\_of\_ll\_exists

```python
def test_no_nodes_tail_of_ll_exists(blank_ll)
```

<a id="python_solutions.tests.test_LinkedList.test_can_not_modify_tail_manually"></a>

#### test\_can\_not\_modify\_tail\_manually

```python
def test_can_not_modify_tail_manually(blank_ll)
```

<a id="python_solutions.tests.test_LinkedList.test_can_not_modify_size_manually"></a>

#### test\_can\_not\_modify\_size\_manually

```python
def test_can_not_modify_size_manually(blank_ll)
```

<a id="python_solutions.tests.test_LinkedList.ll_with_node"></a>

#### ll\_with\_node

```python
@pytest.fixture()
def ll_with_node()
```

<a id="python_solutions.tests.test_LinkedList.ll_with_same_head_and_tail"></a>

#### ll\_with\_same\_head\_and\_tail

```python
@pytest.fixture()
def ll_with_same_head_and_tail()
```

<a id="python_solutions.tests.test_LinkedList.test_size_ll_with_1_node_initialized_differently"></a>

#### test\_size\_ll\_with\_1\_node\_initialized\_differently

```python
def test_size_ll_with_1_node_initialized_differently(
        ll_with_same_head_and_tail)
```

<a id="python_solutions.tests.test_LinkedList.test_head_and_tail_in_ll_with_1_node"></a>

#### test\_head\_and\_tail\_in\_ll\_with\_1\_node

```python
def test_head_and_tail_in_ll_with_1_node(ll_with_same_head_and_tail)
```

<a id="python_solutions.tests.test_LinkedList.test_one_node_ll_has_size"></a>

#### test\_one\_node\_ll\_has\_size

```python
def test_one_node_ll_has_size(ll_with_node)
```

<a id="python_solutions.tests.test_LinkedList.test_size1_ll_has_equal_head_and_tail"></a>

#### test\_size1\_ll\_has\_equal\_head\_and\_tail

```python
def test_size1_ll_has_equal_head_and_tail(ll_with_node)
```

<a id="python_solutions.tests.test_LinkedList.test_can_initialize_ll_from_chain_of_nodes_using_head"></a>

#### test\_can\_initialize\_ll\_from\_chain\_of\_nodes\_using\_head

```python
def test_can_initialize_ll_from_chain_of_nodes_using_head()
```

<a id="python_solutions.tests.test_LinkedList.ll_with_2_nodes_from_head"></a>

#### ll\_with\_2\_nodes\_from\_head

```python
@pytest.fixture()
def ll_with_2_nodes_from_head()
```

<a id="python_solutions.tests.test_LinkedList.test_size_for_ll_with_2_nodes_is_2"></a>

#### test\_size\_for\_ll\_with\_2\_nodes\_is\_2

```python
def test_size_for_ll_with_2_nodes_is_2(ll_with_2_nodes_from_head)
```

<a id="python_solutions.tests.test_LinkedList.test_head_determines_correctly_for_ll_with_2_nodes"></a>

#### test\_head\_determines\_correctly\_for\_ll\_with\_2\_nodes

```python
def test_head_determines_correctly_for_ll_with_2_nodes(
        ll_with_2_nodes_from_head)
```

<a id="python_solutions.tests.test_LinkedList.test_tail_determines_correctly_for_ll_with_2_nodes"></a>

#### test\_tail\_determines\_correctly\_for\_ll\_with\_2\_nodes

```python
def test_tail_determines_correctly_for_ll_with_2_nodes(
        ll_with_2_nodes_from_head)
```

<a id="python_solutions.tests.test_LinkedList.test_ll_from_chain_of_nodes_using_tail_leads_to_blank_ll"></a>

#### test\_ll\_from\_chain\_of\_nodes\_using\_tail\_leads\_to\_blank\_ll

```python
def test_ll_from_chain_of_nodes_using_tail_leads_to_blank_ll()
```

<a id="python_solutions.tests.test_LinkedList.ll_with_2_nodes_from_tail"></a>

#### ll\_with\_2\_nodes\_from\_tail

```python
@pytest.fixture()
def ll_with_2_nodes_from_tail()
```

<a id="python_solutions.tests.test_LinkedList.test_size_for_ll_with_2_nodes_from_tail_is_0"></a>

#### test\_size\_for\_ll\_with\_2\_nodes\_from\_tail\_is\_0

```python
def test_size_for_ll_with_2_nodes_from_tail_is_0(ll_with_2_nodes_from_tail)
```

<a id="python_solutions.tests.test_LinkedList.test_head_of_ll_with_2_nodes_from_tail_is_none"></a>

#### test\_head\_of\_ll\_with\_2\_nodes\_from\_tail\_is\_none

```python
def test_head_of_ll_with_2_nodes_from_tail_is_none(ll_with_2_nodes_from_tail)
```

<a id="python_solutions.tests.test_LinkedList.test_tail_of_ll_with_2_nodes_from_tail_is_none"></a>

#### test\_tail\_of\_ll\_with\_2\_nodes\_from\_tail\_is\_none

```python
def test_tail_of_ll_with_2_nodes_from_tail_is_none(ll_with_2_nodes_from_tail)
```

<a id="python_solutions.tests.test_LinkedList.test_iter_in_ll_works"></a>

#### test\_iter\_in\_ll\_works

```python
def test_iter_in_ll_works()
```

<a id="python_solutions.tests.test_LinkedList.test_append_in_ll_works"></a>

#### test\_append\_in\_ll\_works

```python
def test_append_in_ll_works()
```

<a id="python_solutions.tests.test_LinkedList.test_insertion_of_the_first_element_in_ll_works"></a>

#### test\_insertion\_of\_the\_first\_element\_in\_ll\_works

```python
def test_insertion_of_the_first_element_in_ll_works()
```

<a id="python_solutions.tests.test_LinkedList.test_insertion_in_the_head_in_ll_works"></a>

#### test\_insertion\_in\_the\_head\_in\_ll\_works

```python
def test_insertion_in_the_head_in_ll_works()
```

<a id="python_solutions.tests.test_LinkedList.test_append_by_insertion_in_ll_works"></a>

#### test\_append\_by\_insertion\_in\_ll\_works

```python
def test_append_by_insertion_in_ll_works()
```

<a id="python_solutions.tests.test_LinkedList.test_actual_insertion_in_ll_works"></a>

#### test\_actual\_insertion\_in\_ll\_works

```python
def test_actual_insertion_in_ll_works()
```

<a id="python_solutions.tests.test_LinkedList.ll_for_erase"></a>

#### ll\_for\_erase

```python
@pytest.fixture()
def ll_for_erase()
```

<a id="python_solutions.tests.test_LinkedList.test_delete_head_element_in_ll_works"></a>

#### test\_delete\_head\_element\_in\_ll\_works

```python
def test_delete_head_element_in_ll_works(ll_for_erase)
```

<a id="python_solutions.tests.test_LinkedList.test_delete_the_last_element_in_ll_works"></a>

#### test\_delete\_the\_last\_element\_in\_ll\_works

```python
def test_delete_the_last_element_in_ll_works(ll_for_erase)
```

<a id="python_solutions.tests.test_LinkedList.test_delete_only_element_in_ll"></a>

#### test\_delete\_only\_element\_in\_ll

```python
def test_delete_only_element_in_ll(ll_with_node)
```

<a id="python_solutions.tests.test_LinkedList.test_delete_i_th_element_in_ll_works"></a>

#### test\_delete\_i\_th\_element\_in\_ll\_works

```python
def test_delete_i_th_element_in_ll_works(ll_for_erase)
```

<a id="python_solutions.tests.test_LinkedList.test_neg_indexes_in_erase_in_ll_work"></a>

#### test\_neg\_indexes\_in\_erase\_in\_ll\_work

```python
def test_neg_indexes_in_erase_in_ll_work(ll_for_erase)
```

<a id="python_solutions.tests.test_LinkedList.test_update"></a>

#### test\_update

```python
def test_update(ll_for_erase)
```

<a id="python_solutions.tests.test_LinkedList.test_neg_index_in_update_never_works"></a>

#### test\_neg\_index\_in\_update\_never\_works

```python
def test_neg_index_in_update_never_works(ll_for_erase)
```

<a id="python_solutions.tests.test_LinkedList.test_ll_stores_nones"></a>

#### test\_ll\_stores\_nones

```python
def test_ll_stores_nones(ll_for_erase)
```

<a id="python_solutions.tests.test_LinkedList.test_ll_contains"></a>

#### test\_ll\_contains

```python
def test_ll_contains(ll_for_erase)
```

<a id="python_solutions.tests.test_LinkedList.test_ll_repr"></a>

#### test\_ll\_repr

```python
def test_ll_repr(ll_for_erase)
```

<a id="python_solutions.tests.test_LinkedList.test_indexing_with_neg_numbers_inside_insert"></a>

#### test\_indexing\_with\_neg\_numbers\_inside\_insert

```python
def test_indexing_with_neg_numbers_inside_insert(ll_for_erase)
```

<a id="python_solutions.tests.test_merge_sort.patch"></a>

## patch

<a id="python_solutions.tests.test_merge_sort.test_import_error_for_merge"></a>

#### test\_import\_error\_for\_merge

```python
def test_import_error_for_merge()
```

<a id="python_solutions.tests.test_merge_sort.test_merge_sort_easy_merge"></a>

#### test\_merge\_sort\_easy\_merge

```python
def test_merge_sort_easy_merge()
```

<a id="python_solutions.tests.test_Node.Node"></a>

## Node

<a id="python_solutions.tests.test_Node.pytest"></a>

## pytest

<a id="python_solutions.tests.test_Node.test_can_create_blank_node"></a>

#### test\_can\_create\_blank\_node

```python
def test_can_create_blank_node()
```

<a id="python_solutions.tests.test_Node.node"></a>

#### node

```python
@pytest.fixture()
def node()
```

<a id="python_solutions.tests.test_Node.test_can_assign_data_to_node"></a>

#### test\_can\_assign\_data\_to\_node

```python
def test_can_assign_data_to_node(node)
```

<a id="python_solutions.tests.test_Node.test_can_create_node_with_data"></a>

#### test\_can\_create\_node\_with\_data

```python
def test_can_create_node_with_data()
```

<a id="python_solutions.tests.test_Node.node_with_data"></a>

#### node\_with\_data

```python
@pytest.fixture()
def node_with_data()
```

<a id="python_solutions.tests.test_Node.test_node_can_show_data"></a>

#### test\_node\_can\_show\_data

```python
def test_node_can_show_data(node_with_data)
```

<a id="python_solutions.tests.test_Node.test_node_can_store_next_node"></a>

#### test\_node\_can\_store\_next\_node

```python
def test_node_can_store_next_node(node)
```

<a id="python_solutions.tests.test_Node.test_raises_error_when_next_node_is_not_node_or_none"></a>

#### test\_raises\_error\_when\_next\_node\_is\_not\_node\_or\_none

```python
def test_raises_error_when_next_node_is_not_node_or_none(node)
```

<a id="python_solutions.tests.test_Node.test_raises_error_when_initialized_with_wrong_next_node"></a>

#### test\_raises\_error\_when\_initialized\_with\_wrong\_next\_node

```python
def test_raises_error_when_initialized_with_wrong_next_node()
```

<a id="python_solutions.tests.test_Node.test_eq_for_node"></a>

#### test\_eq\_for\_node

```python
def test_eq_for_node(node_with_data)
```

<a id="python_solutions.tests.test_Node.test_repr_in_node"></a>

#### test\_repr\_in\_node

```python
def test_repr_in_node(node_with_data)
```

<a id="python_solutions.tests.test_Queue.Queue"></a>

## Queue

<a id="python_solutions.tests.test_Queue.pytest"></a>

## pytest

<a id="python_solutions.tests.test_Queue.test_can_make_queue"></a>

#### test\_can\_make\_queue

```python
def test_can_make_queue()
```

<a id="python_solutions.tests.test_Queue.q"></a>

#### q

```python
@pytest.fixture()
def q()
```

<a id="python_solutions.tests.test_Queue.test_can_push_into_queue"></a>

#### test\_can\_push\_into\_queue

```python
def test_can_push_into_queue(q)
```

<a id="python_solutions.tests.test_Queue.test_front_in_queue_works"></a>

#### test\_front\_in\_queue\_works

```python
def test_front_in_queue_works(q)
```

<a id="python_solutions.tests.test_Queue.q_with_4_elements"></a>

#### q\_with\_4\_elements

```python
@pytest.fixture()
def q_with_4_elements()
```

<a id="python_solutions.tests.test_Queue.test_can_pop_from_queue"></a>

#### test\_can\_pop\_from\_queue

```python
def test_can_pop_from_queue(q_with_4_elements)
```

<a id="python_solutions.tests.test_Queue.test_pop_until_one_element_left"></a>

#### test\_pop\_until\_one\_element\_left

```python
def test_pop_until_one_element_left(q_with_4_elements)
```

<a id="python_solutions.tests.test_Queue.test_pop_last_element"></a>

#### test\_pop\_last\_element

```python
def test_pop_last_element(q)
```

<a id="python_solutions.tests.test_real_bin_search.pytest"></a>

## pytest

<a id="python_solutions.tests.test_real_bin_search.real_bin_search"></a>

## real\_bin\_search

<a id="python_solutions.tests.test_real_bin_search.test_real_bin_search_desc"></a>

#### test\_real\_bin\_search\_desc

```python
def test_real_bin_search_desc()
```

<a id="python_solutions.tests.test_real_bin_search.test_real_bin_search_asc"></a>

#### test\_real\_bin\_search\_asc

```python
def test_real_bin_search_asc()
```

<a id="python_solutions.tests.test_real_bin_search.test_search_with_check"></a>

#### test\_search\_with\_check

```python
def test_search_with_check()
```

<a id="python_solutions.tests.test_real_bin_search.test_search_raises_error_when_result_behind_edges_when_check_enabled"></a>

#### test\_search\_raises\_error\_when\_result\_behind\_edges\_when\_check\_enabled

```python
def test_search_raises_error_when_result_behind_edges_when_check_enabled()
```

<a id="python_solutions.tests.test_red_black_tree.pytest"></a>

## pytest

<a id="python_solutions.tests.test_red_black_tree.random"></a>

## random

<a id="python_solutions.tests.test_red_black_tree.math"></a>

## math

<a id="python_solutions.tests.test_red_black_tree.RedBlackTree"></a>

## RedBlackTree

<a id="python_solutions.tests.test_red_black_tree.TreeNode"></a>

## TreeNode

<a id="python_solutions.tests.test_red_black_tree.rb_tree"></a>

#### rb\_tree

```python
@pytest.fixture
def rb_tree()
```

<a id="python_solutions.tests.test_red_black_tree.test_insert"></a>

#### test\_insert

```python
def test_insert(rb_tree)
```

<a id="python_solutions.tests.test_red_black_tree.test_rotations"></a>

#### test\_rotations

```python
def test_rotations()
```

<a id="python_solutions.tests.test_red_black_tree.test_delete"></a>

#### test\_delete

```python
def test_delete(rb_tree)
```

<a id="python_solutions.tests.test_red_black_tree.test_delete_with_error"></a>

#### test\_delete\_with\_error

```python
def test_delete_with_error(rb_tree)
```

<a id="python_solutions.tests.test_red_black_tree.test_search"></a>

#### test\_search

```python
def test_search(rb_tree)
```

<a id="python_solutions.tests.test_red_black_tree.test_random_length_and_elts"></a>

#### test\_random\_length\_and\_elts

```python
def test_random_length_and_elts()
```

<a id="python_solutions.tests.test_segment_tree.pytest"></a>

## pytest

<a id="python_solutions.tests.test_segment_tree.random"></a>

## random

<a id="python_solutions.tests.test_segment_tree.gcd"></a>

## gcd

<a id="python_solutions.tests.test_segment_tree.SegmentTree"></a>

## SegmentTree

<a id="python_solutions.tests.test_segment_tree.SegmentTreeOptimized"></a>

## SegmentTreeOptimized

<a id="python_solutions.tests.test_segment_tree.data1"></a>

#### data1

<a id="python_solutions.tests.test_segment_tree.data2"></a>

#### data2

<a id="python_solutions.tests.test_segment_tree.data"></a>

#### data

<a id="python_solutions.tests.test_segment_tree.test_build_tree"></a>

#### test\_build\_tree

```python
@pytest.mark.parametrize('data', data)
def test_build_tree(data)
```

<a id="python_solutions.tests.test_segment_tree.test_query_sum"></a>

#### test\_query\_sum

```python
@pytest.mark.parametrize('data', data)
def test_query_sum(data)
```

<a id="python_solutions.tests.test_segment_tree.test_query_min"></a>

#### test\_query\_min

```python
@pytest.mark.parametrize('data', data)
def test_query_min(data)
```

<a id="python_solutions.tests.test_segment_tree.test_query_max"></a>

#### test\_query\_max

```python
@pytest.mark.parametrize('data', data)
def test_query_max(data)
```

<a id="python_solutions.tests.test_segment_tree.test_query_gcd"></a>

#### test\_query\_gcd

```python
@pytest.mark.parametrize('data', data)
def test_query_gcd(data)
```

<a id="python_solutions.tests.test_segment_tree.test_update"></a>

#### test\_update

```python
@pytest.mark.parametrize('data', data)
def test_update(data)
```

<a id="python_solutions.tests.test_segment_tree.test_new_action"></a>

#### test\_new\_action

```python
@pytest.mark.parametrize('data', data)
def test_new_action(data)
```

<a id="python_solutions.tests.test_segment_tree.test_build_new_action"></a>

#### test\_build\_new\_action

```python
@pytest.mark.parametrize('data', data)
def test_build_new_action(data)
```

<a id="python_solutions.tests.test_sorts_and_searches.math"></a>

## math

<a id="python_solutions.tests.test_sorts_and_searches.logging"></a>

## logging

<a id="python_solutions.tests.test_sorts_and_searches.pytest"></a>

## pytest

<a id="python_solutions.tests.test_sorts_and_searches.random"></a>

## random

<a id="python_solutions.tests.test_sorts_and_searches.Matrix2dim"></a>

## Matrix2dim

<a id="python_solutions.tests.test_sorts_and_searches.array_count_sort"></a>

## array\_count\_sort

<a id="python_solutions.tests.test_sorts_and_searches.count_sort"></a>

## count\_sort

<a id="python_solutions.tests.test_sorts_and_searches.insert_sort"></a>

## insert\_sort

<a id="python_solutions.tests.test_sorts_and_searches.insert_sort_opt"></a>

## insert\_sort\_opt

<a id="python_solutions.tests.test_sorts_and_searches.merge_sort"></a>

## merge\_sort

<a id="python_solutions.tests.test_sorts_and_searches.merge_sort_parallel"></a>

## merge\_sort\_parallel

<a id="python_solutions.tests.test_sorts_and_searches.quick_sort"></a>

## quick\_sort

<a id="python_solutions.tests.test_sorts_and_searches.digit_sort"></a>

## digit\_sort

<a id="python_solutions.tests.test_sorts_and_searches.digit_sort_opt"></a>

## digit\_sort\_opt

<a id="python_solutions.tests.test_sorts_and_searches.two_dim_array_count_sort"></a>

## two\_dim\_array\_count\_sort

<a id="python_solutions.tests.test_sorts_and_searches.bin_search"></a>

## bin\_search

<a id="python_solutions.tests.test_sorts_and_searches.real_bin_search"></a>

## real\_bin\_search

<a id="python_solutions.tests.test_sorts_and_searches.tern_search_max"></a>

## tern\_search\_max

<a id="python_solutions.tests.test_sorts_and_searches.tern_search_min"></a>

## tern\_search\_min

<a id="python_solutions.tests.test_sorts_and_searches.lower_bound"></a>

## lower\_bound

<a id="python_solutions.tests.test_sorts_and_searches.upper_bound"></a>

## upper\_bound

<a id="python_solutions.tests.test_sorts_and_searches.split_find"></a>

## split\_find

<a id="python_solutions.tests.test_sorts_and_searches.random_1_dim_array"></a>

#### random\_1\_dim\_array

```python
def random_1_dim_array(elts_range=(-100, 100),
                       size_of_1_dim_range=(100, 1000))
```

<a id="python_solutions.tests.test_sorts_and_searches.whole_1_dim_array"></a>

#### whole\_1\_dim\_array

```python
def whole_1_dim_array(elts_range=(-100, 100), size_of_1_dim_range=(100, 1000))
```

<a id="python_solutions.tests.test_sorts_and_searches.whole_2_dim_array"></a>

#### whole\_2\_dim\_array

```python
def whole_2_dim_array(elts_range=(-10, 10),
                      size_of_1_dim_range=(1, 10),
                      size_of_2_dim_range=(10, 100))
```

<a id="python_solutions.tests.test_sorts_and_searches.test_size_range"></a>

#### test\_size\_range

<a id="python_solutions.tests.test_sorts_and_searches.num_range"></a>

#### num\_range

<a id="python_solutions.tests.test_sorts_and_searches.test_sorts"></a>

#### test\_sorts

```python
@pytest.mark.parametrize('function, array, params, sorted_params', [
    (array_count_sort,
     whole_2_dim_array(elts_range=num_range,
                       size_of_1_dim_range=test_size_range,
                       size_of_2_dim_range=test_size_range), {}, {
                           'key': lambda a: a[0]
                       }),
    (insert_sort,
     random_1_dim_array(elts_range=num_range,
                        size_of_1_dim_range=test_size_range), {}, {}),
    (insert_sort_opt,
     random_1_dim_array(elts_range=num_range,
                        size_of_1_dim_range=test_size_range), {}, {}),
    (merge_sort,
     random_1_dim_array(elts_range=num_range,
                        size_of_1_dim_range=test_size_range), {
                            'opt': False
                        }, {}),
    (merge_sort,
     random_1_dim_array(elts_range=num_range, size_of_1_dim_range=(1, 1)), {
         'opt': False
     }, {}),
    (merge_sort_parallel,
     random_1_dim_array(elts_range=num_range,
                        size_of_1_dim_range=(32, 100)), {}, {}),
    (merge_sort_parallel, [0], {}, {}),
    (merge_sort,
     random_1_dim_array(elts_range=num_range,
                        size_of_1_dim_range=(101, 1000)), {}, {}),
    (merge_sort,
     random_1_dim_array(elts_range=num_range,
                        size_of_1_dim_range=(10, 60)), {}, {}),
    (quick_sort,
     random_1_dim_array(elts_range=num_range,
                        size_of_1_dim_range=test_size_range), {}, {}),
    (quick_sort,
     random_1_dim_array(elts_range=num_range,
                        size_of_1_dim_range=test_size_range), {
                            'no_recursion': True
                        }, {}),
    (quick_sort,
     random_1_dim_array(elts_range=num_range,
                        size_of_1_dim_range=test_size_range), {
                            'pivot_str': 'clst_avg',
                            'no_recursion': True
                        }, {}),
    (quick_sort,
     random_1_dim_array(elts_range=num_range,
                        size_of_1_dim_range=test_size_range), {
                            'pivot_str': 'm3',
                            'no_recursion': True
                        }, {}), (quick_sort, [0], {}, {}),
    (quick_sort,
     random_1_dim_array(elts_range=num_range,
                        size_of_1_dim_range=test_size_range), {
                            'pivot_str': 'clst_avg'
                        }, {}),
    (quick_sort,
     random_1_dim_array(elts_range=num_range,
                        size_of_1_dim_range=test_size_range), {
                            'pivot_str': 'm3'
                        }, {}),
    (quick_sort, [1000] + random_1_dim_array(
        elts_range=num_range, size_of_1_dim_range=test_size_range) + [-1000], {
            'pivot_str': 'm3'
        }, {}),
    (quick_sort,
     random_1_dim_array(elts_range=num_range,
                        size_of_1_dim_range=test_size_range), {
                            'pivot_str': 'mm'
                        }, {}), (quick_sort, [], {}, {}),
    (two_dim_array_count_sort,
     whole_2_dim_array(elts_range=num_range,
                       size_of_1_dim_range=test_size_range,
                       size_of_2_dim_range=test_size_range), {}, {}),
    (two_dim_array_count_sort,
     whole_2_dim_array(elts_range=num_range,
                       size_of_1_dim_range=test_size_range,
                       size_of_2_dim_range=test_size_range), {
                           'keys': [0, 1, 2]
                       }, {
                           'key': lambda x: (x[0], x[1], x[2])
                       }),
    (two_dim_array_count_sort,
     whole_2_dim_array(elts_range=num_range,
                       size_of_1_dim_range=test_size_range,
                       size_of_2_dim_range=test_size_range), {
                           'keys': 2
                       }, {
                           'key': lambda x: x[2]
                       }),
    (count_sort,
     whole_1_dim_array(elts_range=num_range,
                       size_of_1_dim_range=test_size_range), {}, {}),
    (digit_sort,
     whole_1_dim_array(elts_range=num_range,
                       size_of_1_dim_range=test_size_range), {
                           'base': 16
                       }, {}),
    (digit_sort_opt,
     whole_1_dim_array(elts_range=num_range,
                       size_of_1_dim_range=test_size_range), {
                           'base': 16
                       }, {})
])
def test_sorts(function, array, params, sorted_params)
```

<a id="python_solutions.tests.test_sorts_and_searches.test_errors_in_sorts"></a>

#### test\_errors\_in\_sorts

```python
@pytest.mark.parametrize(
    'function, array, params',
    [(two_dim_array_count_sort,
      whole_2_dim_array(elts_range=num_range,
                        size_of_1_dim_range=test_size_range,
                        size_of_2_dim_range=test_size_range), {
                            'keys': ''
                        }),
     (quick_sort,
      random_1_dim_array(elts_range=num_range,
                         size_of_1_dim_range=test_size_range), {
                             'pivot_str': 'mm',
                             'no_recursion': True
                         }),
     (quick_sort,
      random_1_dim_array(elts_range=num_range,
                         size_of_1_dim_range=test_size_range), {
                             'pivot_str': 'cool'
                         })])
def test_errors_in_sorts(function, array, params)
```

<a id="python_solutions.tests.test_sorts_and_searches.test_bin_search"></a>

#### test\_bin\_search

```python
@pytest.mark.parametrize('array', [
    random_1_dim_array(elts_range=num_range,
                       size_of_1_dim_range=test_size_range),
    random_1_dim_array(elts_range=num_range,
                       size_of_1_dim_range=test_size_range),
])
def test_bin_search(array)
```

<a id="python_solutions.tests.test_sorts_and_searches.func"></a>

#### func

```python
def func(x)
```

<a id="python_solutions.tests.test_sorts_and_searches.test_real_bin_search"></a>

#### test\_real\_bin\_search

```python
def test_real_bin_search()
```

<a id="python_solutions.tests.test_sorts_and_searches.test_min_max_tern_search"></a>

#### test\_min\_max\_tern\_search

```python
def test_min_max_tern_search()
```

<a id="python_solutions.tests.test_sorts_and_searches.test_bounds"></a>

#### test\_bounds

```python
@pytest.mark.parametrize('array', [
    whole_1_dim_array(size_of_1_dim_range=(1000, 2000)),
    whole_1_dim_array(size_of_1_dim_range=(100, 2000))
])
def test_bounds(array)
```

<a id="python_solutions.tests.test_sorts_and_searches.test_split_search"></a>

#### test\_split\_search

```python
@pytest.mark.parametrize('array', [
    whole_1_dim_array(elts_range=(-10, 10)),
    whole_1_dim_array(elts_range=(-10, 10))
])
def test_split_search(array)
```

<a id="python_solutions.tests.test_sparse_table.pytest"></a>

## pytest

<a id="python_solutions.tests.test_sparse_table.SparseTable"></a>

## SparseTable

<a id="python_solutions.tests.test_sparse_table.sample_data"></a>

#### sample\_data

<a id="python_solutions.tests.test_sparse_table.sparse_table_instance"></a>

#### sparse\_table\_instance

```python
@pytest.fixture
def sparse_table_instance()
```

<a id="python_solutions.tests.test_sparse_table.test_query_min"></a>

#### test\_query\_min

```python
def test_query_min(sparse_table_instance)
```

<a id="python_solutions.tests.test_sparse_table.test_query_max"></a>

#### test\_query\_max

```python
def test_query_max(sparse_table_instance)
```

<a id="python_solutions.tests.test_sparse_table.test_query_sum"></a>

#### test\_query\_sum

```python
def test_query_sum(sparse_table_instance)
```

<a id="python_solutions.tests.test_sparse_table.test_append_and_extend_raise_errors"></a>

#### test\_append\_and\_extend\_raise\_errors

```python
def test_append_and_extend_raise_errors(sparse_table_instance)
```

<a id="python_solutions.tests.test_Stack.Stack"></a>

## Stack

<a id="python_solutions.tests.test_Stack.pytest"></a>

## pytest

<a id="python_solutions.tests.test_Stack.test_can_make_stack"></a>

#### test\_can\_make\_stack

```python
def test_can_make_stack()
```

<a id="python_solutions.tests.test_Stack.st"></a>

#### st

```python
@pytest.fixture()
def st()
```

<a id="python_solutions.tests.test_Stack.test_can_push_to_stack"></a>

#### test\_can\_push\_to\_stack

```python
def test_can_push_to_stack(st)
```

<a id="python_solutions.tests.test_Stack.test_can_access_stack_back"></a>

#### test\_can\_access\_stack\_back

```python
def test_can_access_stack_back(st)
```

<a id="python_solutions.tests.test_Stack.test_can_access_stack_front"></a>

#### test\_can\_access\_stack\_front

```python
def test_can_access_stack_front(st)
```

<a id="python_solutions.tests.test_Stack.st_with_3_elements"></a>

#### st\_with\_3\_elements

```python
@pytest.fixture()
def st_with_3_elements()
```

<a id="python_solutions.tests.test_Stack.test_can_pop_from_stack"></a>

#### test\_can\_pop\_from\_stack

```python
def test_can_pop_from_stack(st_with_3_elements)
```

<a id="python_solutions.tests.test_Stack.test_pop_until_one_element_left"></a>

#### test\_pop\_until\_one\_element\_left

```python
def test_pop_until_one_element_left(st_with_3_elements)
```

<a id="python_solutions.tests.test_Stack.test_pop_last_element"></a>

#### test\_pop\_last\_element

```python
def test_pop_last_element(st_with_3_elements)
```

<a id="python_solutions.tests.test_Stack.test_can_not_pop_when_zero_elements"></a>

#### test\_can\_not\_pop\_when\_zero\_elements

```python
def test_can_not_pop_when_zero_elements(st)
```

<a id="python_solutions.tests.test_Stack.test_can_not_pop_when_less_than_zero_elements"></a>

#### test\_can\_not\_pop\_when\_less\_than\_zero\_elements

```python
def test_can_not_pop_when_less_than_zero_elements(st)
```

<a id="python_solutions.tests.test_vector.pytest"></a>

## pytest

<a id="python_solutions.tests.test_vector.vector"></a>

## vector

<a id="python_solutions.tests.test_vector.test_can_create_vector_and_len_exists"></a>

#### test\_can\_create\_vector\_and\_len\_exists

```python
def test_can_create_vector_and_len_exists()
```

<a id="python_solutions.tests.test_vector.test_set_and_get_item"></a>

#### test\_set\_and\_get\_item

```python
def test_set_and_get_item()
```

<a id="python_solutions.tests.test_vector.test_insertion"></a>

#### test\_insertion

```python
def test_insertion()
```

<a id="python_solutions.tests.test_vector.test_erase"></a>

#### test\_erase

```python
def test_erase()
```

<a id="python_solutions.tests.test_vector.test_vector_with_cap_lt_size"></a>

#### test\_vector\_with\_cap\_lt\_size

```python
def test_vector_with_cap_lt_size()
```

<a id="python_solutions.tests.test_vector.test_cap_lt_0"></a>

#### test\_cap\_lt\_0

```python
def test_cap_lt_0()
```

<a id="python_solutions.tests.test_vector.test_size_lt_0"></a>

#### test\_size\_lt\_0

```python
def test_size_lt_0()
```

<a id="python_solutions.tests.test_vector.test_vector_pop"></a>

#### test\_vector\_pop

```python
def test_vector_pop()
```

<a id="python_solutions.tests.test_vector.test_empty_vector_extend"></a>

#### test\_empty\_vector\_extend

```python
def test_empty_vector_extend()
```

<a id="python_solutions.tests.test_vector.test_vector_extend"></a>

#### test\_vector\_extend

```python
def test_vector_extend()
```

<a id="python_solutions.tests.test_vector.test_vector_iter"></a>

#### test\_vector\_iter

```python
def test_vector_iter()
```

tests
-----

This module contains unit tests for the algorithms
and data structures implemented in the 'python_solutions' module.

Contents
--------
- Tests for helper-functions for sorts
  - test_array_count_sort.py
  - test_digit_sort.py
  - test_speed_analysis.py
- Tests for helper-functions for searches
  - test_bin_search.py
  - test_real_bin_search.py
- Tests for structures
  - test_bloom_filter.py
  - test_CyclicLinkedList.py
  - test_Deque.py
  - test_DoubleNode.py
  - test_hashtable.py
  - test_heap.py
  - test_LinkedList.py
  - test_Node.py
  - test_Queue.py
  - test_Stack.py
  - test_vector.py
- Tests for performance measurements
  - test_sorts_and_searches.py

Two-Dimensional Array Count Sort Module

This module provides a function, `two_dim_array_count_sort`, for sorting a
2-dimensional array consisting of whole numbers. The function can sort the
1-dimensional arrays inside a 2-dimensional array in ascending order by all
indexes (by default) or by exact indexes in the order they are presented.

Functions
---------
two_dim_array_count_sort(a: list[list[int]], keys: str | list | int = 'all')
    Sorts a 2-dimensional array consisting of whole numbers.

<a id="python_solutions.two_dim_array_count_sort.array_count_sort"></a>

## array\_count\_sort

<a id="python_solutions.two_dim_array_count_sort.two_dim_array_count_sort"></a>

#### two\_dim\_array\_count\_sort

```python
def two_dim_array_count_sort(
- **a**: list[list[int]],

- **keys**: str | list[int] | int = 'all') -> list[list[int]]

```

Sorts a 2-dimensional array consisting of whole numbers.

This function sorts the 1-dimensional arrays inside a 2-dimensional array
in ascending order by all indexes (by default) or by exact indexes
in the order they are presented. Be mindful that this sort populates
an array with absent places in each row's key position with sentinel
values (-inf). In this case the ascending sort will always lead to rows
with absent values being put higher than ones without them.

## Parameters
- **a**: list[list[int]]

    The 2-dimensional array to be sorted.

- **keys**: 'all', list of int, or int, optional

    Specifies the indexes to sort by. If 'all', it sorts by all indexes
    (default). If a list of integers is provided, it sorts by the exact
    indexes in the specified order. If an integer is provided,
    it sorts by a single index.

## Returns

list[list[int]]
    The sorted 2-dimensional array.

## Raises

TypeError
    Raised if the 'keys' argument is of an unsupported type.

Vector Class Module
===================

This module defines a Python class, `Vector`, which implements a
self-expanding array, also known as a dynamic array. A dynamic array can
resize itself to accommodate additional elements as needed.

Class
-----
Vector
    A self-expanding array implementation.

<a id="python_solutions.vector.copy"></a>

## copy

<a id="python_solutions.vector.Any"></a>

## Any

<a id="python_solutions.vector.Generator"></a>

## Generator

<a id="python_solutions.vector.Iterable"></a>

## Iterable

<a id="python_solutions.vector.Sized"></a>

## Sized

<a id="python_solutions.vector.Vector"></a>

## Vector Objects

```python
class Vector()
```

A self-expanding array implementation, also known as a dynamic array.

This class defines a vector by specifying its starting capacity
(and optional initial elements). The vector can dynamically resize
itself to accommodate additional elements when needed.

## Attributes
- **elements**: list or None, optional

    An optional list of initial elements for the vector,
    by default None.

- **size**: int, optional

    The initial size of the vector, by default 0.

- **capacity**: int, optional

    The initial capacity of the vector, by default 1.

## Methods

__init__(self, elements: list[Any] | None = None, size: int = 0,
- **capacity**: int = 1) -> None

    Initializes a new Vector instance with optional initial elements,
    size, and capacity.

__len__(self) -> int
    Returns the number of elements in the vector.

__contains__(self, x: Any) -> bool
    Checks if a given element is present in the vector.

__setitem__(self, i: int, x: Any) -> None
    Sets the element at the specified index in the vector.

__getitem__(self, i: int) -> Any
    Retrieves the element at the specified index from the vector.

__delitem__(self, i: int) -> None
    Deletes the element at the specified index from the vector.

copy_to_new_vector(self) -> None
    Creates a new vector and copies elements from the current vector
    to the new one.

increase_capacity(self) -> None
    Increases the capacity of the vector and copies elements
    to the new vector.

decrease_capacity(self) -> None
    Decreases the capacity of the vector and copies elements
    to the new vector.

erase(self, i: int) -> None
    Removes the element at the specified index from the vector.

append(self, x: Any) -> None
    Appends an element to the end of the vector.

insert(self, x: Any, i: int) -> None
    Inserts an element at the specified index in the vector.

pop(self) -> Any
    Pops the last element from the vector.

extend(self, elements: Sized and Iterable) -> None
    Appends to the vector all elements provided in `elements`.

__iter__(self) -> Generator
    Iterates over all elements in the vector.

<a id="python_solutions.vector.Vector.__init__"></a>

#### \_\_init\_\_

```python
def __init__(elements: list[Any] | None = None,
- **size**: int = 0,

- **capacity**: int = 1) -> None

```

Creates an instance of vector.

## Parameters
- **elements**: list or None, optional

    An optional list of initial elements for the vector,
    by default None.

- **size**: int, optional

    The initial size of the vector, by default 0.

- **capacity**: int, optional

    The initial capacity of the vector, by default 1.

## Raises

NotImplementedError
    Raised if the specified `capacity` is less than `size` or
    if invalid `capacity` or `size` values are provided.

<a id="python_solutions.vector.Vector.__len__"></a>

#### \_\_len\_\_

```python
def __len__() -> int
```

Returns the number of elements in the vector.

## Returns

int
    The number of elements in the vector.

<a id="python_solutions.vector.Vector.__contains__"></a>

#### \_\_contains\_\_

```python
def __contains__(x: Any) -> bool
```

Checks if a given element is present in the vector.

## Parameters
- **x**: Any

    The element to check for in the vector.

## Returns

bool
    True if the element is found, False otherwise.

<a id="python_solutions.vector.Vector.__setitem__"></a>

#### \_\_setitem\_\_

```python
def __setitem__(i: int, x: Any) -> None
```

Sets the element at the specified index in the vector.

## Parameters
- **i**: int

    The index at which to set the element.

- **x**: Any

    The element to set.

## Returns

None

## Raises

IndexError
    Raised if the index is out of range.

<a id="python_solutions.vector.Vector.__getitem__"></a>

#### \_\_getitem\_\_

```python
def __getitem__(i: int) -> Any
```

Retrieves the element at the specified index from the vector.

## Parameters
- **i**: int

    The index of the element to retrieve.

## Returns

Any
    The element at the specified index.

## Raises

IndexError
    Raised if the index is out of range.

<a id="python_solutions.vector.Vector.__delitem__"></a>

#### \_\_delitem\_\_

```python
def __delitem__(i: int) -> None
```

Deletes the element at the specified index from the vector.

## Parameters
- **i**: int

    The index of the element to delete.

## Returns

None

<a id="python_solutions.vector.Vector.copy_to_new_vector"></a>

#### copy\_to\_new\_vector

```python
def copy_to_new_vector() -> None
```

Change the size of the vector and copies elements from the current
vector to the new one.

## Returns

None

<a id="python_solutions.vector.Vector.increase_capacity"></a>

#### increase\_capacity

```python
def increase_capacity() -> None
```

Increases the capacity of the vector and copies elements
to the new vector.

## Returns

None

<a id="python_solutions.vector.Vector.decrease_capacity"></a>

#### decrease\_capacity

```python
def decrease_capacity() -> None
```

Decreases the capacity of the vector and copies elements
to the new vector.

## Returns

None

<a id="python_solutions.vector.Vector.erase"></a>

#### erase

```python
def erase(i: int) -> None
```

Removes the element at the specified index from the vector.

If the size of the vector becomes less than or equal to one-fourth
of its capacity after removal, the capacity is decreased.

## Parameters
- **i**: int

    The index of the element to remove.

## Returns

None

## Raises

IndexError
    Raised if the index is out of range.

<a id="python_solutions.vector.Vector.append"></a>

#### append

```python
def append(x: Any) -> None
```

Appends an element to the end of the vector.

If the size of the vector becomes equal to its capacity
after appending, the capacity is increased.

## Parameters
- **x**: Any

    The element to append to the vector.

## Returns

None

<a id="python_solutions.vector.Vector.insert"></a>

#### insert

```python
def insert(x: Any, i: int) -> None
```

Inserts an element at the specified index in the vector.

If the size of the vector becomes equal to its capacity
after insertion, the capacity is increased.

## Parameters
- **x**: Any

    The element to insert into the vector.

- **i**: int

    The index at which to insert the element.

## Returns

None

## Raises

IndexError
    Raised if the index is out of range.

<a id="python_solutions.vector.Vector.pop"></a>

#### pop

```python
def pop() -> Any
```

Pops the last element in the vector.

## Returns

Any
    The popped element.

<a id="python_solutions.vector.Vector.extend"></a>

#### extend

```python
def extend(elements: Sized and Iterable) -> None
```

Appends all provided elements.

## Parameters
- **elements**: Sized and Iterable

    Data structure supporting slices and containing elements
    to be appended

## Returns

None

<a id="python_solutions.vector.Vector.__iter__"></a>

#### \_\_iter\_\_

```python
def __iter__() -> Generator
```

Iterates over all vector's elements.

## Returns

Generator

<a id="python_solutions.weighted_graph.heapq"></a>

## heapq

<a id="python_solutions.weighted_graph.random"></a>

## random

<a id="python_solutions.weighted_graph.WeightedGraphNode"></a>

## WeightedGraphNode

<a id="python_solutions.weighted_graph.Graph"></a>

## Graph

<a id="python_solutions.weighted_graph.WeightedGraph"></a>

## WeightedGraph Objects

```python
class WeightedGraph(Graph)
```

<a id="python_solutions.weighted_graph.WeightedGraph.__init__"></a>

#### \_\_init\_\_

```python
def __init__()
```

<a id="python_solutions.weighted_graph.WeightedGraph.add_vertex"></a>

#### add\_vertex

```python
def add_vertex(*args, **kwargs)
```

<a id="python_solutions.weighted_graph.WeightedGraph.add_edge"></a>

#### add\_edge

```python
def add_edge(u: int, v: int, *args, **kwargs)
```

<a id="python_solutions.weighted_graph.WeightedGraph.add_weight"></a>

#### add\_weight

```python
def add_weight(u: int, v: int, u_to_v_weight: float = 1)
```

<a id="python_solutions.weighted_graph.WeightedGraph.remove_edge"></a>

#### remove\_edge

```python
def remove_edge(u: int, v: int)
```

<a id="python_solutions.weighted_graph.WeightedGraph.calculate_element"></a>

#### calculate\_element

```python
def calculate_element(vertex, neighbor)
```

<a id="python_solutions.weighted_graph.WeightedGraph.prims_algorithm_mst"></a>

#### prims\_algorithm\_mst

```python
def prims_algorithm_mst()
```

<a id="python_solutions.weighted_graph.WeightedGraph.find"></a>

#### find

```python
def find(parent, i)
```

<a id="python_solutions.weighted_graph.WeightedGraph.union"></a>

#### union

```python
def union(parent, rank, x, y)
```

<a id="python_solutions.weighted_graph.WeightedGraph.kruskals_mst"></a>

#### kruskals\_mst

```python
def kruskals_mst()
```