# sparse_table_module

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