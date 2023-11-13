"""
Binary Search Tree Module
=========================

This module defines a Binary Search Tree (BST) class that allows the
insertion, deletion, and search of elements. It also provides methods for
traversing the tree in-order, finding the minimum and maximum values, and
determining the successor and predecessor of a given element.

Classes
-------
TreeNode
    A class representing a node in the Binary Search Tree.

BinarySearchTree
    A class representing a Binary Search Tree.

"""

from Algorithms.python_solutions.Node import Node


class TreeNode(Node):
    """
    A class representing a node in the Binary Search Tree.
    Also a basic class to inherit from for more complicated tree nodes.

    Attributes
    ----------
    left: TreeNode | None, optional
        The left child of the node if present, else - None. Default is None.

    right: TreeNode | None, optional
        The right child of the node if present, else - None. Default is None.

    """

    def __init__(self, data: int | float) -> None:
        """
        Initializes a new instance of the TreeNode class with the specified
        data.

        Parameters
        ----------
        data: int | float
            Data to be put into the TreeNode.

        Returns
        -------
        None

        """
        super().__init__(data=data)
        self.left = None
        self.right = None


class BinarySearchTree:
    """
    A class representing a Binary Search Tree.

    Attributes
    ----------
    root: TreeNode | None
        The root node of the tree if exists, else None.

    size: int
        The size of the tree.

    Methods
    -------
    __init__(self) -> None
        Initializes a new instance of the BinarySearchTree class.

    insert(self, data: int | float) -> None
        Inserts a new element with the specified data into the Binary Search
        Tree.

    _insert(self, root: TreeNode, new_node: TreeNode) -> None
        Recursively inserts a new node into the Binary Search Tree.

    delete(self, data: int | float, is_rb: bool = False) -> None
        Deletes the node with the specified data from the Binary Search Tree.
        If method is called by RedBlackTree class (with is_rb=True) - then
        redirects to the _delete_rb() method from RedBlackTree.

    _delete(self, node: TreeNode) -> None
        Recursively deletes the specified node from the Binary Search Tree.

    search(self, data: int | float) -> TreeNode
        Searches for a node with the specified data in the Binary Search Tree.

    _search(self, root: TreeNode, data: int | float) -> TreeNode
        Recursively searches for a node with the specified data in the
        Binary Search Tree.

    in_order_traversal(self) -> list[int | float]
        Performs an in-order traversal of the Binary Search Tree and returns
        a list of elements.

    _in_order_traversal_rec(self, root: TreeNode, result: list) -> None
        Recursively performs an in-order traversal of the Binary Search Tree.

    find_min(self) -> int | float
        Finds the minimum value in the Binary Search Tree.

    _min_value_node(self, node: TreeNode) -> TreeNode
        Finds the node with the minimum value in the Binary Search Tree.

    find_max(self) -> int | float
        Finds the maximum value in the Binary Search Tree.

    _max_value_node(self, node: TreeNode) -> TreeNode
        Finds the node with the maximum value in the Binary Search Tree.

    find_successor(self, data: int | float) -> int | float
        Finds the successor of the node with the specified data in the
        Binary Search Tree.

    find_predecessor(self, data: int | float) -> int | float
        Finds the predecessor of the node with the specified data in the
        Binary Search Tree.

    is_empty(self) -> bool
        Checks if the Binary Search Tree is empty.

    """

    def __init__(self) -> None:
        """
        Initializes a new instance of the BinarySearchTree class.

        Returns
        -------
        None
        """
        self.root = None
        self.size = 0

    def insert(self, data: int | float) -> None:
        """
        Inserts a new element with the specified data into the Binary
        Search Tree.

        Parameters
        ----------
        data: int | float
            The data to be inserted.

        Returns
        -------
        None

        """
        new_node = TreeNode(data=data)
        if self.root is None:
            self.root = new_node
        else:
            self._insert(self.root, new_node)
        self.size += 1

    def _insert(self, root: TreeNode, new_node: TreeNode) -> None:
        """
        Recursively inserts a new node into the Binary Search Tree.

        Parameters
        ----------
        root: TreeNode
            Current TreeNode.

        new_node: TreeNode
            The node with the data to be inserted.

        Returns
        -------
        None

        """
        if new_node.data < root.data:
            if root.left is not None:
                self._insert(root.left, new_node)
                return
            else:
                root.left = new_node
        else:
            if root.right is not None:
                self._insert(root.right, new_node)
                return
            else:
                root.right = new_node
        new_node.next_node = root

    def delete(self, data: int | float, is_rb: bool = False) -> None:
        """
        Deletes the node with the specified data from the Binary Search Tree.

        Parameters
        ----------
        data: int | float
            The data which contains the node to be deleted.

        is_rb: bool
            Parameter to handle the call from RBTree. Default is False.

        Returns
        -------
        None

        """
        if self.size == 0:
            raise IndexError('Tree is empty')
        node = self._search(self.root, data)
        if node is not None:
            if is_rb:
                self._delete_rb(node)
            else:
                self._delete(node)
        self.size -= 1

    def _delete(self, node: TreeNode) -> None:
        """
        Recursively deletes the specified node from the Binary Search Tree.

        Parameters
        ----------
        node: TreeNode
            The node to be deleted.

        Returns
        -------
        None

        """
        if node.left is not None and node.right is not None:
            successor = node.right
            while successor.left is not None:
                successor = successor.left
            node.data, successor.data = successor.data, node.data
            self._delete(successor)
        elif node.left is not None or node.right is not None:
            child = node.left if node.left is not None \
                else node.right
            if node.next_node is None:
                self.root = child
            elif node == node.next_node.left:
                node.next_node.left = child
            else:
                node.next_node.right = child
            child.next_node = node.next_node
        else:
            if node.next_node is not None:
                if node.next_node.left is node:
                    node.next_node.left = None
                elif node.next_node.right is node:
                    node.next_node.right = None
            else:
                self.root.data = None

    def search(self, data: int | float) -> TreeNode | None:
        """
        Searches for a node with the specified data in the Binary Search Tree.

        Parameters
        ----------
        data: int | float
            The data which contains inside the node to be searched.

        Returns
        -------
        TreeNode | None
            TreeNode containing the data required or None if such TreeNode
            was not found.

        """
        return self._search(self.root, data)

    def _search(self, root: TreeNode, data: int | float) -> TreeNode | None:
        """
        Recursively searches for a node with the specified data in the
        Binary Search Tree.

        Parameters
        ----------
        root: TreeNode
            Current TreeNode.

        data: int | float
            The data which contains inside the node to be searched.

        Returns
        -------
        TreeNode | None
            TreeNode containing the data required or None if such TreeNode
            was not found.

        """
        if root is None or root.data == data:
            return root
        if data < root.data:
            return self._search(root.left, data)
        return self._search(root.right, data)

    def in_order_traversal(self) -> list[int | float]:
        """
        Performs an in-order traversal of the Binary Search Tree and returns
        a list of elements.

        Returns
        -------
        list[int | float]
            The list of elements in increasing order.

        """
        result = []
        self._in_order_traversal_rec(self.root, result)
        return result if result != [None] else []

    def _in_order_traversal_rec(
            self, root: TreeNode, result: list[int | float | None]) -> None:
        """
        Recursively performs an in-order traversal of the Binary Search Tree.

        Parameters
        ----------
        root: TreeNode
            Current TreeNode.

        result: list[int | float | None]
            The list to store result from traversal.

        Returns
        -------
        None

        """
        if root:
            self._in_order_traversal_rec(root.left, result)
            result.append(root.data)
            self._in_order_traversal_rec(root.right, result)

    def find_min(self) -> int | float | None:
        """
        Finds the minimum value in the Binary Search Tree.

        Returns
        -------
        int | float | None
            The min if it was found, None otherwise.

        """

        if self.root is None:
            return None
        return self._min_value_node(self.root).data

    def _min_value_node(self, node: TreeNode) -> TreeNode:
        """
        Finds the node with the minimum value in the Binary Search Tree.

        Parameters
        ----------
        node: TreeNode
            The root if the BST.

        Returns
        -------
        TreeNode
            TreeNode containing the minimum value.

        """

        current = node
        while current.left is not None:
            current = current.left
        return current

    def find_max(self) -> int | float | None:
        """
        Finds the maximum value in the Binary Search Tree.

        Returns
        -------
        int | float | None
            The maximum value if it was found, None otherwise.

        """
        if self.root is None:
            return None
        return self._max_value_node(self.root).data

    def _max_value_node(self, node: TreeNode) -> TreeNode:
        """
        Finds the node with the maximum value in the Binary Search Tree.

        Parameters
        ----------
        node: TreeNode
            The root of the BST.

        Returns
        -------
        TreeNode
            The node containing the maximum value.

        """
        current = node
        while current.right is not None:
            current = current.right
        return current

    # after data in traversal
    def find_successor(self, data: int | float) -> int | float | None:
        """
        Finds the successor of the node with the specified data in the
        Binary Search Tree.

        Parameters
        ----------
        data: int | float
            The data, successor to which is to be found.

        Returns
        -------
        int | float | None
            The successor to the data.

        """
        node = self._search(self.root, data)
        if node and node.right:
            return self._min_value_node(node.right).data
        successor = None
        current = self.root
        while current:
            if data < current.data:
                successor = current
                current = current.left
            elif data > current.data:
                current = current.right
            else:
                break
        return successor.data if successor else None

    # before data in traversal
    def find_predecessor(self, data: int | float) -> int | float | None:
        """
        Finds the predecessor of the node with the specified data in the
        Binary Search Tree.

        Parameters
        ----------
        data: int | float
            The data, predecessor to which is to be found.

        Returns
        -------
        int | float | None
            The predecessor to the data.

        """
        node = self._search(self.root, data)
        if node and node.left:
            return self._max_value_node(node.left).data
        predecessor = None
        current = self.root
        while current:
            if data > current.data:
                predecessor = current
                current = current.right
            elif data < current.data:
                current = current.left
            else:
                break
        return predecessor.data if predecessor else None

    def is_empty(self) -> bool:
        """
        Checks if the Binary Search Tree is empty.

        Returns
        -------
        bool
            True if the BST is empty, False otherwise.

        """
        return self.root is None
