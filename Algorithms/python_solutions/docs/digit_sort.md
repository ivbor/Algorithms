# digit_sort

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