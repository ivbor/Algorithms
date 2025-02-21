"""
Deque Module
============

This module defines a Double-ended Queue (Deque) class, which represents
a data structure that allows elements to be added or removed from both ends.

Classes
-------
Deque
    Represents a Double-ended Queue (Deque) and provides methods for adding,
    removing, and accessing elements from both ends.
"""


from Algorithms_Python.DoubleNode import DoubleNode
from Algorithms_Python.Stack import Stack
from Algorithms_Python.Queue import Queue


class Deque(Queue, Stack):  # <(out)-(in)> Deck <(out)-(in)>
    """
    Double-ended Queue (Deque) Class

    The Deque class represents a double-ended queue,
    which is a data structure that allows elements
    to be added or removed from both ends.

    Methods
    -------
    push_back(self, value)
        Add an element to the back (left) end of the deque,
        equivalent to enqueue in a queue.

    pop_front(self)
        Remove and return the element from the front (right) end of the deque,
        equivalent to dequeue in a queue.

    pop_back(self)
        Remove and return the element from the back (left) end of the deque,
        equivalent to pop in a stack.

    push_front(self, value)
        Add an element to the front (right) end of the deque.

    """
    # push from Queue
    def push_back(self, value):
        """
        Add an element to the back (left) end of the deque.

        Parameters
        ----------
        value: any
            The element to be added to the deque.

        Returns
        -------
        None

        """
        Queue.push(self, value)

    # pop from Queue
    def pop_front(self):
        """
        Remove and return the element from the front (right) end of the deque.

        Returns
        -------
        any
            The element removed from the front of the deque.

        """
        Queue.pop(self)

    # pop from Stack
    def pop_back(self):
        """
        Remove and return the element from the back (left) end of the deque.

        Returns
        -------
        any
            The element removed from the back of the deque.

        """
        Stack.pop(self)

    def push_front(self, value):
        """
        Add an element to the front (right) end of the deque.

        Parameters
        ----------
        value: any
            The element to be added to the front of the deque.

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
            newNode = DoubleNode(value, None, self.head)
            self.head.prev_node = newNode
            self.head = self.head.prev_node
            self.size += 1
