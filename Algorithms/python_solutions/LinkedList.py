"""
Linked List Module
======================

A module for implementing a one-way linked list data structure.

This module contains the `LinkedList` class, which represents a one-way
linked list data structure. The `LinkedList` class allows for the creation
and manipulation of a linked list, including appending, inserting, erasing,
and searching for elements.

Classes
-------
LinkedList
    A one-way linked list data structure.

"""
from Algorithms.python_solutions.Node import Node


class LinkedList:
    '''
    Linked List Implementation.

    The LinkedList class represents a one-way linked list data structure.
    It allows for the creation and manipulation of a linked list, including
    appending, inserting, erasing, and searching for elements.

    Attributes
    ----------
    head: Node or None
        The first node of the linked list.

    tail: Node or None
        The last node of the linked list.

    size: int
        The number of elements in the linked list.

    Methods
    -------
    __init__(self, head=None, tail=None) -> None
        Creates an instance of the LinkedList class.
        It is important to note, that if there already is some
        connection between head and tail nodes - this method will
        effectively parse it.

    append(self, x) -> None
        Add an element to the end of the linked list.

    insert(self, i, x) -> None
        Insert an element at a specific index.

    erase(self, i) -> None
        Remove the element at a specific index.

    __contains__(self, x) -> bool
        Check if an element exists in the linked list.

    __iter__(self) -> Generator
        Iterate through the elements of the linked list.

    list_all(self) -> List[]
        Return a list of all elements in the linked list.

    __str__(self) -> str
        Return a string representation of the linked list.

    __repr__(self) -> str
        Print method for the linked list.

    '''

    def __init__(self, head=None, tail=None):

        '''
        Initialize a Linked List.

        Parameters
        ----------
        head: Node or None, optional
            The first node of the linked list.
            Default is None.

        tail: Node or None, optional
            The last node of the linked list.
            Default is None.

        Returns
        -------
        None
        '''

        # save the head if exists
        self._head = head

        # check a connection between head and tail
        # if they both are mentioned

        # check whether head is available
        if (head is not None):

            # check if there is only 1 node
            if head != tail:

                # if not - dump first node,
                node = self._head

                # get ready to move tail,
                self._tail = self._head

                # and increase size to 1
                self._size = 1

                # move tail until the end of the
                # chain is reached
                while (node is not None):
                    if next(node) is not None:
                        node = next(node)
                    else:
                        self._tail = node
                        break
                    self._size += 1
            else:
                self._size = 1
                self._tail = self._head
        else:
            self._tail = self._head
            self._size = 0

    @property
    def head(self):
        '''
        Get the head of the linked list.

        Returns
        -------
        Node or None
            The head of the linked list.
        '''

        return self._head

    @head.setter
    def head(self, head):
        '''
        Set the head of the linked list.

        Parameters
        ----------
        head: Node or None
            The new head of the linked list.

        Returns
        -------
        None
        '''
        self._head = head
        if self._size == 0:
            self._size += 1
            self._tail = self._head

    @property
    def tail(self):
        '''
        Get the tail of the linked list.

        Returns
        -------
        Node or None
            The tail of the linked list.
        '''
        return self._tail

    @tail.setter
    def tail(self, tail):
        '''
        Raise NotImplementedError when trying to set the tail.
        The tail should be set through insert or initialization methods.

        Parameters
        ----------
        tail: Node or None
            The new tail of the linked list.

        Raises
        ------
        NotImplementedError
            When trying to set the tail directly.
        '''
        raise NotImplementedError('assigning tail is only possible' +
                                  ' through insert or initialization' +
                                  '\n' +
                                  f'use {self.__name__}.insert({tail})')

    @property
    def size(self):
        '''
        Get the size of the linked list.

        Returns
        -------
        int
            The size of the linked list.
        '''
        return self._size

    @size.setter
    def size(self, size):
        '''
        Raise NotImplementedError when trying to set the size.
        The size is calculated automatically.

        Parameters
        ----------
        size: int
            The new size of the linked list.

        Raises
        ------
        NotImplementedError
            When trying to set the size directly.
        '''
        raise NotImplementedError('can not set size, ' +
                                  'it is calculated automatically')

    def __contains__(self, x):
        '''
        Check if a given element is present in the linked list.

        Parameters
        ----------
        x: any
            The element to check for in the linked list.

        Returns
        -------
        bool
            True if the element is found, False otherwise.
        '''
        if x in self.list_all():
            return True
        else:
            return False

    def __iter__(self):
        '''
        Iterate through the elements of the linked list.

        Returns
        -------
        generator
            A generator to iterate through the elements.
        '''
        cur = self._head
        while True:

            # protection from Attr error
            if cur is not None:
                yield cur.data
            else:
                break

            # protection from Type error
            if isinstance(cur.next_node, Node):
                cur = next(cur)

            # if the end is reached
            else:
                break

    def list_all(self):
        '''
        Return a list of all elements in the linked list.

        Returns
        -------
        list
            A list containing all elements of the linked list.
        '''
        ret = list()
        for i in self:
            ret.append(i)
        return ret

    def __str__(self):
        '''
        Return a string representation of the linked list.

        Returns
        -------
        str
            A string representation of the linked list.
        '''
        return str(self.list_all())

    def __repr__(self):
        '''
        Return a string representation of the linked list.

        Returns
        -------
        str
            A string representation of the linked list.
        '''
        return str(self)

    def append(self, x):
        '''
        Append an element to the end of the linked list.

        Parameters
        ----------
        x: any
            The element to append to the linked list.

        Returns
        -------
        None
        '''
        # for the first element
        if self._size == 0:
            newNode = Node(x, None)
            self._head = newNode
            self._tail = self._head
            self._size += 1
        # for other elements
        else:
            newNode = Node(x, None)
            self._tail.next_node = newNode
            self._tail = newNode
            self._size += 1

    def search(self, i):
        '''
        Search for nodes at a given index in the linked list.

        Parameters
        ----------
        i: int
            The index at which to search for nodes.

        Returns
        -------
        tuple
            A tuple containing the previous and current nodes.
        '''
        previous = self._head
        current = previous.next_node
        index_of_current_element = 1
        while index_of_current_element < i:
            previous = current
            current = previous.next_node
            index_of_current_element += 1
        return (previous, current)

    def insert(self, i, x):
        '''
        Insert an element at a given index in the linked list.

        Parameters
        ----------
        i: int
            The index at which to insert the element.

        x: any
            The element to insert into the linked list.

        Raises
        ------
        IndexError
            When trying to insert with negative indexing.
            Negative indexing is an undefined operation.

        Returns
        -------
        None
        '''
        # for the first element
        if not isinstance(self._head, Node):
            newNode = Node(x, None)
            self._head = newNode
            self._tail = self._head
        # insert in the head
        elif i == 0:
            newNode = Node(x, None)
            newNode.next_node = self._head
            self._head = newNode
        # append using insert
        elif i == self._size + 1:
            self.append(x)
        # throw index error, insertion
        # with negative indexing is
        # an undefined operation
        elif i < 0:
            raise IndexError('Indexing is' +
                             ' only possible with non-negative' +
                             ' numbers')
        # otherwise - dig for i-th element
        else:
            previous, current = self.search(i)

            # insert i-th element
            newNode = Node(x, None)
            previous.next_node = newNode
            newNode.next_node = current
        self._size += 1

    def erase(self, i):
        '''
        Remove an element at the specified index in the linked list.

        Parameters
        ----------
        i: int
            The index at which to remove the element.

        Raises
        ------
        IndexError
            If the index is out of bounds or negative.

        Returns
        -------
        None
        '''
        # if head is to erase
        if i == 0:

            # if the list has only one Node
            if self._size == 1:
                del self._head
                self._head = None
                del self._tail
                self._tail = None
            else:
                buff = self._head.next_node
                del self._head
                self._head = buff

        # if index is negative and
        # to get to i one does not
        # have to go multiple (2 or more)
        # times to the tail,
        # no more than once
        elif i < 0 and abs(i) < self._size:

            # in this case we prevent
            # users from abusing
            # negative indexes
            # but generally allow them
            self.erase(self._size + i)

        # otherwise - dig for i-th element
        else:
            previous, current = self.search(i)

            # delete i-th element
            buff = current.next_node
            del current
            previous.next_node = buff

            # if i-th element is tail - reassign tail
            if i == self._size - 1:
                self._tail = previous
        self._size -= 1

    def update(self, i, x):
        '''
        Update the element at the specified index in the linked list.

        Parameters
        ----------
        i: int
            The index at which to update the element.
        x: any
            The new value to assign to the element.

        Raises
        ------
        IndexError
            If the index is negative.

        Returns
        -------
        None
        '''
        if i < 0:
            raise IndexError('Indexing is' +
                             ' only possible with non-negative' +
                             ' numbers')
        previous, current = self.search(i)
        current.data = x
