# real_binary_search_module

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