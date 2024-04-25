# vector_class_module

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