"""
Cyclic Linked List Module
=========================

This module defines a cyclic linked list, which is a variation of a linked list
where the tail node is connected to the head node, creating a closed loop.

Classes
-------
CyclicLinkedList
    Represents a cyclic linked list and provides additional
    methods and behavior specific to cyclic linked lists.
"""


from Algorithms_Python.DoubleNode import DoubleNode
from Algorithms_Python.LinkedList import LinkedList


class CyclicLinkedList(LinkedList):

    """
    Represents a cyclic linked list, which is a variation of a linked list
    where the tail node is connected to the head node, creating a closed loop.

    This class inherits from the LinkedList class and provides additional
    methods and behavior specific to cyclic linked lists. This means that
    operations like list traversal and iteration will continue
    indefinitely in a loop.

    Attributes
    ----------
    _head: DoubleNode or None
        The head node of the cyclic linked list. Default is None.

    _tail: DoubleNode or None
        The tail node of the cyclic linked list. Default is None.

    _size: int
        The number of elements in the cyclic linked list. Default is None.

    Methods
    -------
    __init__(self, head=None, tail=None) -> None
        Initializes empty cyclic linked list.

    list_all(self) -> List[Unknown]
        Returns a list containing all the elements in the cyclic linked list.

    search(self, i) -> tuple(DoubleNode | None, DoubleNode | None)
        Searches for the i-th element in the cyclic linked list and returns
        the previous and current nodes before the i-th element.

    insert(self, i, x) -> None
        Inserts a new element x at the specified index i in
        the cyclic linked list.

    erase(self, i) -> None
        Removes the element at the specified index i from
        the cyclic linked list.

    update(self, i, x) -> None
        Updates the element at the specified index i in
        the cyclic linked list with x.

    """

    def __init__(self, head=None, tail=None):
        """
        Initializes an empty cyclic linked list.

        Parameters
        ----------
        head: DoubleNode or None, optional
            The head node of the cyclic linked list. Default is None.

        tail: DoubleNode or None, optional
            The tail node of the cyclic linked list. Default is None.

        Returns
        -------
        None
        """
        super().__init__(head, tail)
        if self._tail is not None:
            self._tail.next_node = self._head

    def list_all(self):
        """
        Returns a list containing all the elements in the cyclic linked list.

        Returns
        -------
        List[Unknown]
            A list containing all the elements in the cyclic linked list.
        """
        ret = list()
        ctr = 0
        for i in self:
            ret.append(i)
            ctr += 1
            if ctr == self._size:
                break
        return ret

    def search(self, i):
        """
        Searches for the i-th element in the cyclic linked list and returns
        the node before the i-th element (previous)
        and the node with i-th element (current).

        Parameters
        ----------
        i: int
            The index of the element to search for.

        Returns
        -------
        tuple(DoubleNode | None, DoubleNode | None)
            A tuple containing the previous and current nodes if they exist.
        """
        previous = self._head
        current = previous.next_node
        index_of_current_element = 1
        while index_of_current_element < i:
            previous = current
            current = previous.next_node
            index_of_current_element += 1
        return (previous, current)

    def insert(self, i, x):
        """
        Inserts a new element x at the specified index i
        in the cyclic linked list.

        Parameters
        ----------
        i: int
            The index at which to insert the new element.

        x: Unknown
            The element to insert.

        Returns
        -------
        None
        """
        # for the first element
        if not isinstance(self._head, DoubleNode):
            newNode = DoubleNode(x, None, None)
            self._head = newNode
            self._tail = self._head
            self._head.next_node = self._tail
            self._head.prev_node = self._tail
            self._tail.next_node = self._head
            self._tail.prev_node = self._head
        # insert in the head or tail
        elif i == 0 or i == self._size:
            newNode = DoubleNode(x, self._tail, self._head)
            self._head.prev_node = newNode
            self._tail.next_node = newNode
            if i == self._size:
                self._tail = newNode
            else:
                self._head = newNode
        elif i < 0:
            self.insert(self._size + i + 1, x)
            # no element addition - size should not change
            self._size -= 1
        elif i > self._size:
            raise IndexError('CyclicLinkedList index out of range')
        # otherwise - dig for i-th element
        else:
            previous, current = self.search(i)

            # insert i-th element
            newNode = DoubleNode(x, previous, current)
            previous.next_node = newNode
            newNode.next_node = current
        self._size += 1

    def erase(self, i):
        """
        Removes the element at the specified index i
        from the cyclic linked list.

        Parameters
        ----------
        i: int
            The index of the element to remove.

        Returns
        -------
        None
        """
        if self._size != 0:
            if i / self._size > 1:
                raise IndexError('CyclicLinkedList index out if range')
        else:
            raise IndexError('Nothing to erase')
        # for the last element
        if self._size == 1:
            del self._head
            del self._tail
            self._head = None
            self._tail = None
            self._size -= 1
        # if head is to erase
        elif i == 0:
            cur = self._head.next_node
            cur.prev_node = self._tail
            cur.prev_node.next_node = cur
            del self._head
            self._head = cur
            self._size -= 1
        # if tail is to erase
        elif i == self._size:
            cur = self._tail.prev_node
            cur.next_node = self._head
            cur.next_node.prev_node = cur
            del self._tail
            self._tail = cur
            self._size -= 1
        elif i < 0:
            self.erase(self._size + i)
        # otherwise - dig for i-th element
        else:
            cur = self._head
            j = 0
            while j < i:
                cur = cur.next_node
                j += 1
            # and do erasing
            cur.next_node.prev_node = cur.prev_node
            cur.prev_node.next_node = cur.next_node
            del cur
            self._size -= 1

    def update(self, i, x):
        """
        Updates the element at the specified index i
        in the cyclic linked list with x.

        Parameters
        ----------
        i: int
            The index of the element to update.

        x: Unknown
            The new value to update the element with.

        Returns
        -------
        None
        """
        previous, current = self.search(i)
        previous.data = x
