# insertion_sort

A module with Insertion Sort algorithm to sort a list of elements.

Insertion Sort is a simple sorting algorithm that works by iterating through
the input list and, for each element, comparing it with the elements to its
left and inserting it into its correct position within the already sorted
portion of the list. This process continues until the entire list is sorted.

Functions
---------
insert_sort(array: list[float]) -> list[float]
    Sorts a list of elements using the Insertion Sort algorithm.

insert_sort_opt(array: list[float]) -> list[float]
    Sorts a list of elements using the optimized Insertion Sort algorithm.
    This version uses binary search to find the correct position for each
    element, reducing the number of comparisons and improving efficiency.

<a id="python_solutions.insert_sort.insert_sort"></a>

#### insert\_sort

```python
def insert_sort(array: list[float]) -> list[float]
```

This function implements the Insertion Sort algorithm
to sort a list of elements in-place.

The Insertion Sort algorithm works by iterating through the input list,
and for each element, it compares it with the elements
to its left and inserts it into its correct position within
the already sorted portion of the list.
This process continues until the entire list is sorted.
Worst and average cases time complexity - O(n^2).
Space complexity - O(1) as sorting is done in-place.

## Parameters
- **array**: list

    The input list to be sorted.

## Returns

list
    A list containing the elements of the input list in sorted order.

<a id="python_solutions.insert_sort.bin_search_fl"></a>

#### bin\_search\_fl

```python
def bin_search_fl(array: list[float], value: float, start: int,
- **end**: int) -> int

```

<a id="python_solutions.insert_sort.insert_sort_opt"></a>

#### insert\_sort\_opt

```python
def insert_sort_opt(array: list[float]) -> list[float]
```

This function implements the in-place Insertion sort algorithm
enhanced by binary search.

Sorts a list of elements using the optimized Insertion Sort algorithm.
This version uses binary search to find the correct position for each
element, reducing the number of comparisons and improving efficiency.

## Parameters
- **array**: list

    The input list to be sorted.

## Returns

list
    A list containing the elements of the input list in sorted order.