"""
Queue Module

This module defines a Queue class representing a queue data structure with
a first-in-first-out (FIFO) ordering of elements. Elements are enqueued
to the back and dequeued from the front of the queue.

Classes
-------
Queue
    A class representing a queue data structure with enqueue and dequeue
    operations.

"""


from Algorithms_Python.DoubleNode import DoubleNode
from Algorithms_Python.Stack import Stack


class Queue(Stack):  # (FIFO) -(in)> Queue -(out)>
    """
    Queue class

    The Queue class represents a queue data structure
    with a first-in-first-out (FIFO) ordering of elements.
    Elements are added to the back (enqueued) and
    removed from the front (dequeued) of the queue.

    Methods
    -------
    push(self, value)
        Enqueue an element to the back of the queue.

    pop(self)
        Dequeue and return the element from the front of the queue.

    """
    def push(self, value):
        """
        Enqueue an element to the back of the queue.

        Parameters
        ----------
        value: any
            The element to be added to the back of the queue.

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
        Dequeue and return the element from the front of the queue.

        Returns
        -------
        any
            The element removed from the front of the queue.

        """
        # for the last element
        if self.size == 1:
            _return = self.head.data
            del self.tail
            del self.head
        # for other elements
        else:
            _return = self.head.data
            buff = self.head.next_node
            del self.head
            self.head = buff
        self.size -= 1
        return _return
