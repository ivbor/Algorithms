# deque_module

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