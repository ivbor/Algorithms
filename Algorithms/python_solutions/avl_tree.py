"""
AVL Tree Module
===============

This module implements an AVL tree, a self-balancing binary search tree.
This tree has very fixed height, which is smaller than that of RedBlackTree,
and is between log2(size) and 2*log2(size).

Classes
-------
AVLNode
    A class representing a node in an AVL tree, extending TreeNode.

AVLTree
    A class representing an AVL tree,
    extending RedBlackTree and BinarySearchTree.

"""


from Algorithms.python_solutions.bst import BinarySearchTree, TreeNode
from Algorithms.python_solutions.red_black_tree import RedBlackTree


class AVLNode(TreeNode):
    """
    Node for AVL Tree

    Represents a node in an AVL tree. Inherits from TreeNode and provides
    methods to calculate height and balance factor.

    Attributes
    ----------
    data: any
        The data stored in the node.

    Methods
    -------
    __init__(self, data: int | float) -> None
        Initialize an AVLNode.

    height(self) -> int
        Calculate the height of the node.

    balance_factor(self) -> int
        Calculate the balance factor of the node.

    """

    def __init__(self, data: int | float) -> None:
        """
        Initialize an AVLNode object with data.

        Parameters
        ----------
        data : int | float
            The data to be stored in the node.

        Returns
        -------
        None

        """

        super().__init__(data=data)

    def height(self) -> int:
        """
        Calculate the height of the node.

        Returns
        -------
        int
            The height of the node.

        """

        if self.children[0] is not None:
            if self.children[1] is not None:
                return 1 + max(self.children[0].height(),
                               self.children[1].height())
            return 1 + self.children[0].height()
        else:
            if self.children[1] is not None:
                return 1 + self.children[1].height()
            return 1

    def balance_factor(self) -> int:
        """
        Calculate the balance factor of the node.

        Returns
        -------
        int
            The balance factor of the node.

        """

        height0 = 0 if self.children[0] is None \
            else self.children[0].height()
        height1 = 0 if self.children[1] is None \
            else self.children[1].height()
        return height0 - height1


class AVLTree(RedBlackTree, BinarySearchTree):
    """
    AVL Tree Implementation

    Represents an AVL tree, a self-balancing binary search tree.

    Methods
    -------
    __init__(self) -> None
        Initialize an AVLTree object.

    insert(self, key: int | float) -> None
        Insert a key into the AVL tree.

    _insert(root: AVLNode, new_node: AVLNode)
        Helper method to insert a new node into the AVL tree.

    delete(self, key: int | float) -> None
        Delete a key from the AVL tree.

    _delete(node: AVLNode) -> None
        Helper method to delete a node from the AVL tree.

    """

    def __init__(self) -> None:
        """
        Initialize an AVLTree object.

        Returns
        -------
        None

        """

        RedBlackTree.__init__(self)
        self.node_class = AVLNode

    def insert(self, key: int | float) -> None:
        """
        Insert a key into the AVL tree.

        Parameters
        ----------
        key : int | float
            The key to be inserted into the AVL tree.

        Returns
        -------
        None

        """

        BinarySearchTree.insert(self, key)

    def _insert(self, root: AVLNode, new_node: AVLNode) -> None:
        """
        Helper method to insert a new node into the AVL tree.

        Parameters
        ----------
        root : AVLNode
            The root node of the AVL tree.

        new_node : AVLNode
            The new node to be inserted into the AVL tree.

        Returns
        -------
        None

        """

        BinarySearchTree._insert(self, root, new_node)

        balance = root.balance_factor()

        # Left heavy
        if balance > 1:
            # Left-Left case
            if new_node.data <= root.children[0].data:
                self._right_rotate(root)
            # Left-Right case
            else:
                self._left_rotate(root.children[0])
                self._right_rotate(root)

        # Right heavy
        if balance < -1:
            # Right-Right case
            if new_node.data >= root.children[1].data:
                self._left_rotate(root)
            # Right-Left case
            else:
                self._right_rotate(root.children[1])
                self._left_rotate(root)

    def delete(self, key: int | float) -> None:
        """
        Delete a key from the AVL tree.

        Parameters
        ----------
        key : int | float
            The key to be deleted from the AVL tree.

        Returns
        -------
        None

        """

        BinarySearchTree.delete(self, key)

    def _delete(self, node: AVLNode) -> None:
        """
        Helper method to delete a node from the AVL tree.

        Parameters
        ----------
        node : AVLNode
            The node to be deleted from the AVL tree.

        Returns
        -------
        None

        """

        BinarySearchTree._delete(self, node)
