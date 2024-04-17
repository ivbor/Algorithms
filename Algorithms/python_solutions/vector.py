"""
Vector Class Module
===================

This module defines a Python class, `Vector`, which implements a
self-expanding array, also known as a dynamic array. A dynamic array can
resize itself to accommodate additional elements as needed.

Class
-----
Vector
    A self-expanding array implementation.
"""


import copy


from typing import Any, Generator, Iterable, Sized


class Vector:
    """
    A self-expanding array implementation, also known as a dynamic array.

    This class defines a vector by specifying its starting capacity
    (and optional initial elements). The vector can dynamically resize
    itself to accommodate additional elements when needed.

    Attributes
    ----------
    elements : list or None, optional
        An optional list of initial elements for the vector,
        by default None.

    size : int, optional
        The initial size of the vector, by default 0.

    capacity : int, optional
        The initial capacity of the vector, by default 1.

    Methods
    -------
    __init__(self, elements: list[Any] | None = None, size: int = 0,
             capacity: int = 1) -> None
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

    """
    # self-expanding array
    # define a vector by defining its starting capacity
    # (and elements in list-like form if necessary)
    def __init__(self, elements: list[Any] | None = None,
                 size: int = 0, capacity: int = 1) -> None:
        """
        Creates an instance of vector.

        Parameters
        ----------
        elements : list or None, optional
            An optional list of initial elements for the vector,
            by default None.

        size : int, optional
            The initial size of the vector, by default 0.

        capacity : int, optional
            The initial capacity of the vector, by default 1.

        Raises
        ------
        NotImplementedError
            Raised if the specified `capacity` is less than `size` or
            if invalid `capacity` or `size` values are provided.
        """

        if capacity < size:
            raise NotImplementedError('Capacity of array cannot be' +
                                      'less than its size')

        if capacity <= 0 or size < 0:
            raise NotImplementedError('Impossible memory allocation')

        if elements is not None:
            if len(elements) != 0:
                self.size = len(elements)
                self.capacity = self.size * 2
                self.elements = elements
                for _ in range(self.size):
                    self.elements.append(None)
        else:
            self.size = size
            self.capacity = capacity
            self.elements = [None] * self.capacity

    # len in its essential will not lead to expected result
    # since by default vector is organized with non-null
    # length and one None element and list is not

    # using self.size instead of length will still cover
    # usual cases, but for explained above it is manually
    # corrected to recognize vector's size as expected
    # inside __init__
    def __len__(self) -> int:
        """
        Returns the number of elements in the vector.

        Returns
        -------
        int
            The number of elements in the vector.

        """
        return self.size

    def __contains__(self, x: Any) -> bool:
        """
        Checks if a given element is present in the vector.

        Parameters
        ----------
        x : Any
            The element to check for in the vector.

        Returns
        -------
        bool
            True if the element is found, False otherwise.

        """
        if x in self.elements:
            return True
        else:
            return False

    def __setitem__(self, i: int, x: Any) -> None:
        """
        Sets the element at the specified index in the vector.

        Parameters
        ----------
        i : int
            The index at which to set the element.

        x : Any
            The element to set.

        Returns
        -------
        None

        Raises
        ------
        IndexError
            Raised if the index is out of range.

        """
        # handle wrong indexes and prevent from error
        # raised because of null size
        if abs(i) >= self.capacity and (i != 0 and self.size == 0):
            raise IndexError('list index out of range')

        # handle negative indexes
        if i < 0:
            i = self.size + i

        # main changes to the vector while setting an item
        self.elements[i] = x
        self.size += 1

        # some memory work
        if self.size + 1 >= self.capacity:
            self.increase_capacity()

    def __getitem__(self, i: int) -> Any:
        """
        Retrieves the element at the specified index from the vector.

        Parameters
        ----------
        i : int
            The index of the element to retrieve.

        Returns
        -------
        Any
            The element at the specified index.

        Raises
        ------
        IndexError
            Raised if the index is out of range.

        """
        # handle wrong indexes
        if abs(i) >= self.capacity:
            raise IndexError('list index out of range')

        # handle negative indexes
        if i < 0:
            return self.elements[self.size + i]
        return self.elements[i]

    def __delitem__(self, i: int) -> None:
        """
        Deletes the element at the specified index from the vector.

        Parameters
        ----------
        i : int
            The index of the element to delete.

        Returns
        -------
        None

        """
        del self.elements[i]

    def copy_to_new_vector(self) -> None:
        """
        Change the size of the vector and copies elements from the current
        vector to the new one.

        Returns
        -------
        None
        """
        self.elements = self.elements[:self.size] + \
            [None] * (self.capacity - self.size)

    def increase_capacity(self) -> None:
        """
        Increases the capacity of the vector and copies elements
        to the new vector.

        Returns
        -------
        None
        """
        self.capacity *= 2
        self.copy_to_new_vector()

    def decrease_capacity(self) -> None:
        """
        Decreases the capacity of the vector and copies elements
        to the new vector.

        Returns
        -------
        None

        """
        self.capacity //= 2
        self.copy_to_new_vector()

    def erase(self, i: int) -> None:
        """
        Removes the element at the specified index from the vector.

        If the size of the vector becomes less than or equal to one-fourth
        of its capacity after removal, the capacity is decreased.

        Parameters
        ----------
        i : int
            The index of the element to remove.

        Returns
        -------
        None

        Raises
        ------
        IndexError
            Raised if the index is out of range.

        """
        if self.size <= self.capacity / 4:
            self.decrease_capacity()
        if i < 0 or i >= self.size:
            raise IndexError('list index out of range')
        self.size -= 1
        if self.size != 0:
            del self[i]

    def append(self, x: Any) -> None:
        """
        Appends an element to the end of the vector.

        If the size of the vector becomes equal to its capacity
        after appending, the capacity is increased.

        Parameters
        ----------
        x : Any
            The element to append to the vector.

        Returns
        -------
        None

        """
        if self.size + 1 >= self.capacity:
            self.increase_capacity()
        self.elements[self.size] = x
        self.size += 1

    def insert(self, x: Any, i: int) -> None:
        """
        Inserts an element at the specified index in the vector.

        If the size of the vector becomes equal to its capacity
        after insertion, the capacity is increased.

        Parameters
        ----------
        x : Any
            The element to insert into the vector.

        i : int
            The index at which to insert the element.

        Returns
        -------
        None

        Raises
        ------
        IndexError
            Raised if the index is out of range.

        """
        # handle wrong indexes
        if i < 0 or i > self.size:
            raise IndexError('list index out of range')

        # append using insertion
        if i == self.size:
            self.append(x)
            return

        # insertion in its essential
        # some memory work
        if self.size + 1 >= self.capacity or i + 1 == self.size:
            self.increase_capacity()
        # Move elements to make space for the new item
        self.elements[i+1:self.size+1] = self.elements[i:self.size]
        # insert by index
        self.elements[i] = x
        self.size += 1

    def pop(self) -> Any:
        """
        Pops the last element in the vector.

        Returns
        -------
        Any
            The popped element.

        """
        to_pop = copy.deepcopy(self.elements[self.size - 1])
        self.erase(self.size - 1)
        return to_pop

    def extend(self, elements: Sized and Iterable) -> None:
        """
        Appends all provided elements.

        Parameters
        ----------
        elements: Sized and Iterable
            Data structure supporting slices and containing elements
            to be appended

        Returns
        -------
        None

        """
        while self.size + len(elements) >= self.capacity:
            self.increase_capacity()
        self.elements[self.size:self.size + len(elements)] = elements

    def __iter__(self) -> Generator:
        """
        Iterates over all vector's elements.

        Returns
        -------
        Generator

        """
        for i in self.elements[:self.size]:
            yield i
