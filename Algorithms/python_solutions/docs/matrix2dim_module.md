# matrix2dim_module

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