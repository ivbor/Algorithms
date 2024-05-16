"""
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
prev(obj: object with defined prev() method) -> Any
    Retrieve the previous object connected to the given DoubleNode object or
    return None if there is no previous object.
"""


from typing import Any
from Algorithms.python_solutions.Node import Node


# import this too if you want to have the same syntax
# for prev as for built-in next():
# prev(DoubleNode()) instead of DoubleNode().prev()


def prev(obj) -> Any:
    """
    Function-helper for easier calling for previous DoubleNode.

    Works as analog for built-in function next().
    This function retrieves the previous node connected
    to the given DoubleNode object or None if there is no previous node.

    Parameters
    ----------
    obj: object with defined prev() method
        Object for which to retrieve the previous object.

    Returns
    -------
    Any
        The previous object or None if no previous object exists.

    """
    return obj.prev()


class DoubleNode(Node):

    """
    Two-Way Linked List Node Class

    The DoubleNode class represents a node in a two-way linked list.
    It has the same functionality as a regular Node, but it can also
    access the previous node stored into the added attribute
    using the prev() method.

    Methods
    -------
    __init__(self, data=None, prev_node=None, next_node=None)
        Initialize a DoubleNode object.

    prev(self)
        Get the previous node of the DoubleNode.

    """

    def __init__(self, data=None, prev_node=None, next_node=None):
        """
        Initialize a DoubleNode object with optional data,
        previous node, and next node.

        Parameters
        ----------
        data: any, optional
            The data to be stored in the DoubleNode. Default is None.
        prev_node: DoubleNode or None, optional
            The previous node in the linked list. Default is None.
        next_node: DoubleNode or None, optional
            The next node in the linked list. Default is None.

        Returns
        -------
        None

        Raises
        ------
        TypeError
            If the provided prev_node or next_node is of the wrong type.

        """
        self._data = data

        # DoubleNodes can only be connected with DoubleNodes or Nones
        if next_node.__class__.__name__ == \
                self.__class__.__name__ or next_node is None:
            self._next_node = next_node
        else:
            raise TypeError('Wrong type of next_node')

        if (prev_node.__class__.__name__ == self.__class__.__name__)\
           or (prev_node is None):
            self._prev_node = prev_node
        else:
            raise TypeError('Wrong type of prev node')

    @property
    def prev_node(self):
        """
        Get the previous node of the DoubleNode.

        Returns
        -------
        DoubleNode or None
            The previous DoubleNode object or None if no previous node exists.

        """
        return self._prev_node

    @prev_node.setter
    def prev_node(self, prev_node):
        """
        Set the previous node of the DoubleNode.

        Parameters
        ----------
        prev_node: DoubleNode or None
            The previous node to be set for the DoubleNode.

        Raises
        ------
        TypeError
            If the provided prev_node is of the wrong type.

        """
        if prev_node.__class__.__name__ == \
                self.__class__.__name__ or prev_node is None:
            self._prev_node = prev_node
        else:
            raise TypeError('Wrong type of next_node')

    def prev(self):
        """
        This method is defined for providing the same access option
        for the previous node as for the next node
        (to make possible the same call as for built-in function)

        Parameters
        ----------
        prev_node: DoubleNode or None
            The previous node to be set for the DoubleNode.

        Raises
        ------
        TypeError
            If the provided prev_node is of the wrong type.

        """
        return self.prev_node
