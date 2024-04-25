# cyclic_linked_list_module

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