"""
Stack Module
============

This module provides a Python implementation of a stack data structure. The
stack follows the Last-In-First-Out (LIFO) principle, where the last element
added is the first one to be removed. This class provides methods to
manipulate and query the stack.

Classes
-------
Stack
    A stack data structure implemented using a doubly-linked list.

"""


from Algorithms_Python.DoubleNode import DoubleNode


class Stack:  # (LIFO)   <(out)-(in)> Stack |
    """
    A Python implementation of a stack data structure using
    a doubly-linked list.

    The stack follows the Last-In-First-Out (LIFO) principle,
    where the last element added is the first one to be removed.
    This class provides methods to manipulate and query the stack.

    Attributes
    ----------
    head: DoubleNode or None
        The top (front) of the stack. Default is None.

    tail: DoubleNode or None
        The bottom (back) of the stack. Default is None.

    size: int
        The number of elements in the stack.

    Methods
    -------
    __init__(self) -> None
        Initializes an empty stack.

    push(self, value) -> None
        Adds a new element to the back of the stack.

    pop(self) -> Any | None
        Removes and returns the back element from the stack.

    back(self) -> Any | None
        Retrieves the element at the back of the stack
        without removing it.

    front(self) -> Any | None
        Retrieves the element at the top of the stack.

    __len__(self) -> int
        Returns the number of elements currently in the stack.

    """
    def __init__(self) -> None:
        """
        Initializes an empty stack.

        Returns
        -------
        None

        """
        self.head = None
        self.tail = None
        self.size = 0

    def push(self, value):
        """
        Adds a new element to the back of the stack.

        Parameters
        ----------
        value: Any
            The value to be added to the stack.

        Returns
        -------
        None
        """
        # for the first element
        if self.size == 0:
            newNode = DoubleNode(value, None, None)
            self.head = newNode
            self.tail = self.head
            self.size += 1
        # for other elements
        else:
            newNode = DoubleNode(value, self.tail, None)
            self.tail.next_node = newNode
            self.tail = self.tail.next_node
            self.size += 1

    def pop(self):
        """
        Removes and returns the back element from the stack.

        Returns
        -------
        Any
            The removed element from the back of the stack.
        """
        if self.size <= 0:
            raise ValueError('nothing to pop')
        # for the last element
        if self.size == 1:
            _return = self.head.data
            del self.tail
            del self.head
        # for other elements
        else:
            _return = self.tail.data
            buff = self.tail.prev_node
            del self.tail
            self.tail = buff
        self.size -= 1
        return _return

    def back(self):
        """
        Retrieves the element at the back of the stack
        without removing it.

        Returns
        -------
        Any
            The element at the back of the stack.
        """
        return self.tail.data if self.tail is not None else None

    def front(self):
        """
        Retrieves the element at the top of the stack.

        Returns
        -------
        Any
            The element at the top of the stack.
        """
        return self.head.data if self.head is not None else None

    def __len__(self):
        """
        Returns the number of elements currently in the stack.

        Returns
        -------
        int
            The number of elements in the stack.
        """
        return self.size
