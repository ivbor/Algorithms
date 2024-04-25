# merge_sort_module

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