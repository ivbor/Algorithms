"""
Binary Heap and Sort
====================

A module for implementing a binary tree-based min-heap data structure and
heap sort algorithm. This module contains classes and functions for working
with binary tree-based min-heaps and performing heap sort.
A binary tree-based min-heap is a data structure where the minimum value is
stored at the root, and each parent node contains elements smaller than
its children.

Classes
-------
Heap
    A binary tree-based min-heap that extends the Vector class to represent
    the heap. It provides methods for insertion, removal of the minimum
    element, and other heap-related operations.

Functions
---------
heap_sort(array: list[float]) -> list[float]
    Sorts an array in ascending order using the heap sort algorithm.
    Heap sort is an efficient comparison-based sorting algorithm that uses
    a binary heap to perform the sorting.

sift_up(array: list[float], element_index: int, size: int) -> None
    Performs the sift-up operation to maintain the heap property.

sift_down(array: list[float], element_index: int) -> None
    Performs the sift-down operation to maintain the heap property.

"""


from Algorithms.python_solutions.vector import Vector


class Heap(Vector):
    """
    A binary tree-based min-heap data structure.

    This class extends the Vector class to represent a binary
    tree-based min-heap, where the minimum value is stored at the root,
    and each parent node contains elements smaller than its children.

    Attributes
    ----------
    elements : list or None, optional
        An optional list of initial elements for the heap,
        by default None.

    size : int, optional
        The initial size of the heap, by default 0.

    capacity : int, optional
        The initial capacity of the heap, by default 1.

    Methods
    -------
    __init__(self, elements: list[float] | None = None,
             size: int = 0, capacity: int = 1) -> None
        Initialize the heap.

    append(self, x: float) -> None
        Append an element to the heap.

    get_children(self, i: int) -> tuple(float, float) or float or None
        Get the children of a node at the specified index.

    height(self) -> int
        Calculate the height of the heap.

    insert(self, x: float) -> None
        Insert an element into the heap.

    remove_min(self) -> float
        Remove and return the minimum element from the heap.

    __repr__(self) -> str
        Return a string representation of the heap.

    erase(self) -> float
        Alias for `remove_min`.

    """

    def __init__(self, elements: list[float] | None = None,
                 size: int = 0, capacity: int = 1) -> None:
        """
        Initialize a new Heap instance.

        Parameters
        ----------
        elements : list or None, optional
            An optional list of initial elements for the heap,
            by default None.

        size : int, optional
            The initial size of the heap, by default 0.

        capacity : int, optional
            The initial capacity of the heap, by default 1.

        Returns
        -------
        None

        """
        self.size = size
        self.capacity = capacity
        self.elements = []
        if elements is not None:
            for i in elements:
                self.insert(i)

    def append(self, x: float) -> None:
        """
        Append an element to the heap.

        This method is an alias for `insert`.

        Parameters
        ----------
        x : float
            The element to append to the heap.

        Returns
        -------
        None

        """
        self.insert(x)

    def get_children(self, i: int) -> tuple[float, float] | float | None:
        """
        Get the children of a node at the specified index.

        Parameters
        ----------
        i : int
            The index of the node for which to retrieve children.

        Returns
        -------
        tuple or float or None
            A tuple containing the left and right children of the node
            if both exist, the left child if only the left child exists,
            or None if the node has no children.

        """
        if self.size > 2 * i + 2:
            return (self.elements[2*i+1], self.elements[2*i+2])
        elif self.size > 2 * i + 1:
            return self.elements[2 * i + 1]
        else:
            return None

    def height(self) -> int:
        """
        Calculate the height of the heap.

        Returns
        -------
        int
            The height of the heap.

        """
        size = self.size
        high = 0
        while (int(size) != 0):
            size //= 2
            high += 1
        return high

    def insert(self, x: float) -> None:
        """
        Insert an element into the heap.

        If the size of the heap becomes equal to its capacity after
        insertion, the capacity is increased.

        Parameters
        ----------
        x : Any
            The element to insert into the heap.

        Returns
        -------
        None

        """
        if self.size + 1 >= self.capacity:
            self.increase_capacity()

        i = self.size
        self.elements[i] = x
        self.size += 1

        sift_up(self.elements, i)

    def remove_min(self) -> float:
        """
        Remove and return the minimum element from the heap.

        If the size of the heap becomes less than or equal to one-fourth
        of its capacity after removal, the capacity is decreased.

        Returns
        -------
        float
            The minimum element in the heap.

        Raises
        ------
        IndexError
            Raised if the heap is empty.

        """
        if self.size <= self.capacity / 4:
            self.decrease_capacity()

        if self.size == 0:
            raise IndexError('list assignment index out of range')

        self.elements[0], self.elements[self.size - 1] = \
            self.elements[self.size - 1], self.elements[0]
        _return = self.elements[self.size - 1]
        del self.elements[self.size - 1]
        self.size -= 1
        i = 0

        sift_down(self.elements, i, self.size)

        return _return

    def __repr__(self) -> str:
        """
        Return a string representation of the heap.

        Returns
        -------
        str
            A string representation of the heap in a tree-like format.

        """
        string_to_print = ''
        index_of_element_to_print = 0
        current_height = 0
        while (current_height < self.height() + 1):

            # 2**cur_str - amount of numbers in current str
            string_on_current_height = ''
            for _ in range(2**current_height):
                if index_of_element_to_print < self.size:
                    string_on_current_height += \
                        (f'({index_of_element_to_print + 1})' +
                         f'{self.elements[index_of_element_to_print]:8.2e}') \
                        if \
                        self.elements[index_of_element_to_print] is not None \
                        else ' '
                    string_on_current_height += ' '
                    index_of_element_to_print += 1
            string_on_current_height += '\n\n'
            string_to_print += string_on_current_height
            current_height += 1

        return string_to_print

    def erase(self) -> float:
        """
        Alias for `remove_min`.

        Returns
        -------
        float
            The minimum element in the heap.

        """
        return self.remove_min()


def sift_up(a: list[float], i: int) -> None:
    """
    Perform the sift-up operation to maintain heap property.

    Parameters
    ----------
    a : list
        The list representing the elements of the heap.

    i : int
        The index at which the sift-up operation is performed.

    Returns
    -------
    None
    """
    while i > 0:
        parent = int((i-1)/2)
        if a[i] < a[parent]:
            a[i], a[parent] = a[parent], a[i]
            i = parent
        else:
            break


def sift_down(a: list[float], i: int, size: int) -> None:
    """
    Perform the sift-down operation to maintain heap property.

    Parameters
    ----------
    a : list
        The list representing the elements of the heap.

    i : int
        The index at which the sift-down operation is performed.

    size : int
        The size of the heap.

    Returns
    -------
    None

    """
    while True:
        right_child = 2 * i + 2
        left_child = 2 * i + 1
        if size > right_child:
            if (a[i] > a[right_child] and a[left_child] >= a[right_child]):
                a[i], a[right_child] = a[right_child], a[i]
                i = right_child
            elif (a[i] > a[left_child] and a[right_child] >= a[left_child]):
                a[i], a[left_child] = a[left_child], a[i]
                i = left_child
            else:
                break
        elif size > left_child:
            if a[i] > a[left_child]:
                a[i], a[left_child] = a[left_child], a[i]
                break
            break
        else:
            break


def heap_sort(array: list[float]) -> list[float]:
    """
    Sort an array in ascending order using the heap sort algorithm.
    Heap sort is a comparison-based sorting algorithm that builds a binary
    heap data structure and repeatedly extracts the minimum element from the
    heap. The sorted elements are stored in the original array. This algorithm
    has a time complexity of O(n log n) in the worst case, making it efficient
    for large datasets. However, it is not an in-place sorting algorithm since
    it requires additional space for the heap, making its O(n) space
    complexity.
    The heap sort algorithm consists of two main phases: heapify and sorting.
    The "heapify" phase builds a binary heap from the input array,
    ensuring that the heap property is maintained (parent nodes have smaller
    values than their children).
    The "sorting" phase repeatedly removes the minimum element from the heap
    and places it at the end of the array until the heap is empty.

    Parameters
    ----------
    array : list
        The list to be sorted.

    Returns
    -------
    list
        The sorted list in ascending order.

    """
    heap = Heap()
    length = len(array)
    for i in range(length):
        heap.insert(array[i])
    for i in range(length):
        array[i] = heap.erase()
    return array
