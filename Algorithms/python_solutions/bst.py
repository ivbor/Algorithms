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
        # left is 0, right is 1
        self.children = [None, None]
        self.parent = self.next_node


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

    delete(self, data: int | float) -> None
        Deletes the node with the specified data from the Binary Search Tree.

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

    max_height(self) -> int
        Finds the maximum height of the tree.

    local_tree(self, node: TreeNode, b: int = 2, deepness: int = 1)
        -> list[int | float]
        Returns the local tree with the node being root and the required
        deepness. Nodes' data is loaded into the list down from root from
        the left to the right. Deepness 1 equals root and its children.
        b is the order of the tree, for the binary it is 2.

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
        self.node_class = TreeNode

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
        new_node = self.node_class(data=data)
        self.size += 1

        if self.root is None:
            self.root = new_node
            return

        self._insert(self.root, new_node)

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
            if root.children[0] is not None:
                self._insert(root.children[0], new_node)
                return
            else:
                root.children[0] = new_node
        else:
            if root.children[1] is not None:
                self._insert(root.children[1], new_node)
                return
            else:
                root.children[1] = new_node
        new_node.parent = root

    def delete(self, data: int | float) -> None:
        """
        Deletes the node with the specified data from the Binary Search Tree.

        Parameters
        ----------
        data: int | float
            The data which contains the node to be deleted.

        Returns
        -------
        None

        """
        if self.size == 0:
            raise IndexError('Tree is empty')
        node = self._search(self.root, data)
        if node is not None:
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
        if node.children[0] is not None and node.children[1] is not None:
            successor = node.children[1]
            while successor.children[0] is not None:
                successor = successor.children[0]
            node.data, successor.data = successor.data, node.data
            self._delete(successor)
        elif node.children[0] is not None or node.children[1] is not None:
            child = node.children[0] \
                if node.children[0] is not None \
                else node.children[1]
            if node.parent is None:
                self.root = child
            elif node == node.parent.children[0]:
                node.parent.children[0] = child
            else:
                node.parent.children[1] = child
            child.parent = node.parent
        else:
            if node.parent is not None:
                if node.parent.children[0] is node:
                    node.parent.children[0] = None
                elif node.parent.children[1] is node:
                    node.parent.children[1] = None
            else:
                self.root.data = None

    def search(self, data: int | float) -> TreeNode | None:
        """
        Searches for a node with the specified data in the Binary Search Tree.
        In case of value duplicate returns only one node at random.

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
            return self._search(root.children[0], data)
        return self._search(root.children[1], data)

    def node_height(self, node: TreeNode) -> int:
        """
        Finds the height of the node with value.

        Parameters
        ----------
        value: int
            Node data.

        Returns
        -------
        int
            Node height.
        """
        height = 1
        while node.parent is not None:
            height += 1
            node = node.parent
        return height

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
            self._in_order_traversal_rec(root.children[0], result)
            result.append(root.data)
            self._in_order_traversal_rec(root.children[1], result)

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
        while current.children[0] is not None:
            current = current.children[0]
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
        while current.children[1] is not None:
            current = current.children[1]
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
        if node and node.children[1]:
            return self._min_value_node(node.children[1]).data
        successor = None
        current = self.root
        while current:
            if data < current.data:
                successor = current
                current = current.children[0]
            elif data > current.data:
                current = current.children[1]
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
        if node.children[1]:
            if node.children[1].data == node.data:
                return node.data
        if node and node.children[0]:
            return self._max_value_node(node.children[0]).data
        predecessor = None
        current = self.root
        while current:
            if data > current.data:
                predecessor = current
                current = current.children[1]
            elif data < current.data:
                current = current.children[0]
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

    def max_height(self) -> int:
        """
        The maximum height of the tree.

        Returns
        -------
        int
            The height of the tree.

        """

        node_list = []
        if self.root is not None:
            curr_height = 0
            node_list.append(self.root)
        else:
            return 0

        while len(node_list) != 0:
            curr_height += 1
            curr_len_node_list = len(node_list)
            for node_num in range(curr_len_node_list):
                for child in node_list[node_num].children:
                    if child is not None:
                        node_list.append(child)
            node_list = node_list[curr_len_node_list:]

        return curr_height

    def local_tree(self, node: TreeNode, b: int = 2, deepness: int = 1) \
            -> list[int | float]:
        """
        Returns the local tree with the node being root and the required
        deepness. Nodes' data is loaded into the list down from root from
        the left to the right. Deepness 1 equals root and its children.
        b is the order of the tree, for binary it is 2.

        Parameters
        ----------
        node: TreeNode
            Node to be considered the root one.

        b: int
            The order of the tree. Default is 2.

        deepness: int
            The deepness of the local tree.

        Returns
        -------
        list[int | float]
            List containing the tree nodes' data.

        """
        nodes_to_check = [node]
        result = []
        for power in range(deepness + 1):
            extension_list = []
            for node_to_check in nodes_to_check:
                if node_to_check is not None:
                    result.append(node_to_check.data)
                    extension_list.extend(
                        [child for child in node_to_check.children])
                else:
                    result.append(None)
                    extension_list.extend([None, None])
            nodes_to_check.extend(extension_list)
            nodes_to_check = nodes_to_check[int(b ** power):]
        return result
