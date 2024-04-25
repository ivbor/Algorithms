# linked_list_module

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