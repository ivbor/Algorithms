class Node:
    """
    Simple One-Way Node Class

    The Node class represents a simple one-way node that can store data and
    have a reference to the next node in a linked list. It supports basic
    operations like getting the next node and printing the data.

    Attributes
    ----------
    _next_node: Node or None
        Reference to the next node if it exists.

    _data: any
        Data stored inside the node.

    Methods
    -------
    __init__(self, data=None, next_node=None)
        Initialize a Node object with optional data and next node.

    __str__(self)
        Return a string representation of the data stored in the node.

    __next__(self)
        Get the reference to the next node.

    __repr__(self)
        Return a string representation of the node.

    __eq__(self, other)
        Compare if two nodes are the same (reference equality).

    """

    def __init__(self, data=None, next_node=None):
        """
        Initialize a Node object with optional data and next node.

        Parameters
        ----------
        data: any, optional
            The data to be stored in the node. Default is None.

        next_node: Node or None, optional
            The next node in the linked list. Default is None.

        Returns
        -------
        None

        Raises
        ------
        TypeError
            If the provided next_node is of the wrong type.

        """
        self._data = data

        # Nodes can only be connected with nodes or Nones
        if (next_node.__class__.__name__ == self.__class__.__name__)\
           or (next_node is None):
            self._next_node = next_node
        else:
            raise TypeError('Wrong type of next node')

    def __str__(self):
        """
        Return a string representation of the data stored in the node.

        Returns
        -------
        str
            The string representation of the data.

        """
        return str(self._data)

    def __next__(self):
        """
        Get the reference to the next node.

        Returns
        -------
        Node or None
            The reference to the next node or None if it doesn't exist.

        """
        return self._next_node

    def __repr__(self):
        """
        Return a string representation of the node.

        Returns
        -------
        str
            The string representation of the node.

        """
        return self.__str__()

    def __eq__(self, other):
        """
        Compare if two nodes are the same (reference equality).

        Parameters
        ----------
        other: any
            The other object to compare with.

        Returns
        -------
        bool
            True if both nodes are the same, False otherwise.

        """
        return self is other

    @property
    def next_node(self):
        """
        Get the reference to the next node.

        Returns
        -------
        Node or None
            The reference to the next node or None if it doesn't exist.

        """
        return self._next_node

    @next_node.setter
    def next_node(self, next_node):
        """
        Set the reference to the next node.

        Parameters
        ----------
        next_node: Node or None
            The next node to be set for the current node.

        Raises
        ------
        TypeError
            If the provided next_node is of the wrong type.

        """
        if (next_node.__class__.__name__ == self.__class__.__name__)\
           or (next_node is None):
            self._next_node = next_node
        else:
            raise TypeError('Wrong type of next node')

    @property
    def data(self):
        """
        Get or set the data stored in the node.

        Returns
        -------
        any
            The data stored in the node.

        """
        ret = self._data
        return ret

    @data.setter
    def data(self, data):
        """
        Set the data stored in the node.

        Parameters
        ----------
        data: any
            The data to be stored in the node.

        """
        self._data = data
