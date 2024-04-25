# segment_tree_module

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