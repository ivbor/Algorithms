# counting_sort_module

This module provides an implementation of the counting sort algorithm
for sorting an array of whole numbers.

The counting sort algorithm counts the occurrences of each whole number
in the input array and uses this information to create a sorted array.
It is particularly efficient when the range of values is small compared
to the array size.

Functions
---------
count_sort(array: list[int]) -> list[int]
    Sorts an array of whole numbers using the counting sort algorithm.

<a id="python_solutions.count_sort.count_sort"></a>

#### count\_sort

```python
def count_sort(array: list[int]) -> list[int]
```

This function implements counting sort on the array of whole numbers.

The algorithm of counting sort employs the basic counting
of the whole numbers inside array. It creates another array with
(max - min + 1) size, and counts, how many elements with each number
are inside the array to be sorted.
- **Time to work**: O(size of array + difference between the biggest and

the smallest elements)

## Parameters
- **array**: list[int]

    array to be sorted consisting of whole numbers

## Returns

list[int]
    sorted array