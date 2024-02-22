"""
Red-Black Tree Module
=========================

This module defines a Red-Black Tree class which represents balanced
binary search tree. By coloring nodes it is possible to maintain
the height of O(logn), here in particular it is 3*log2n.

Classes
-------
TreeNode
    A class representing a node in the Red-Black Tree.

BinarySearchTree
    A class representing a Red-Black Tree.

"""

import logging

from Algorithms.python_solutions.bst import TreeNode, BinarySearchTree


class RBTreeNode(TreeNode):
    """
    Red-Black Tree Node Class

    This class represents a node in a red-black tree.
    It extends the TreeNode class.

    Attributes
    ----------
    color: str
        The color of the node, either 'red' or 'black'.

    """
    def __init__(self, data, color):
        """
        Initialize a Red-Black Tree Node.

        Parameters
        ----------
        data: any
            The data to be stored in the node.

        color: str
            The color of the node, either 'red' or 'black'.

        Returns
        -------
        None

        """
        super().__init__(data)
        self.color = color


class RedBlackTree(BinarySearchTree):
    """
    Red-Black Tree Class

    This class represents a red-black tree,
    which is a self-balancing binary search tree.

    Attributes
    ----------
    node_class: RBTreeNode
        The class to use for creating nodes in the tree.

    Methods
    -------
    __init__(self) -> None
        Initialize a RedBlackTree object.

    insert(self, key: int | float) -> None
        Insert key into RedBlackTree.

    handle_rb(self, new_node: RBTreeNode) -> None
        The function managing insertion into RedBlackTree.

    recolor(self, node: RBTreeNode, uncle: RBTreeNode) -> None
        The function handling the case when only recoloring is needed.

    rotate_and_recolor(self, node: RBTreeNode, right: bool) -> None
        The function handling the case when both rotation and recoloring
        have to be done.

    _left_rotate(self, node: RBTreeNode) -> None
        The function performing left rotation with node being moved to its
        left child place and the right child of the node moved to the
        node's place.

    _right_rotate(self, node: RBTreeNode) -> None
        The function performing right rotation with node being moved to its
        right child place and the left child of the node moved to the
        node's place.

    _delete(self, node: RBTreeNode) -> None
        The function performing deletion of the node.

    _fix_double_black(self, node: RBTreeNode) -> None
        The function handling the double black violation case
        (parent and child are black) when deleting node.

    """

    def __init__(self) -> None:
        """
        Initialize a Red-Black Tree.

        Returns
        -------
        None

        """
        super().__init__()
        self.node_class = RBTreeNode

    def insert(self, key: int | float) -> None:
        """
        Insert a key into the red-black tree.

        Parameters
        ----------
        key: int | float
            The key to insert into the tree.

        Returns
        -------
        None

        """
        new_node = self.node_class(data=key, color='red')
        self.size += 1

        # if no root - insert to the root
        if self.root is None:
            self.root = new_node
            self.root.color = 'black'
            return

        # basic insert to bst with red color
        self._insert(self.root, new_node)
        self.handle_rb(new_node)

    def handle_rb(self, new_node: RBTreeNode) -> None:
        """
        Handle red-black tree properties after inserting a node.

        Parameters
        ----------
        new_node: RBTreeNode
            The newly inserted node.

        Returns
        -------
        None

        """

        # if there is root - check the parent color
        # if black - do nothing
        if new_node.parent.color == 'red':

            # find uncle and check its color
            if new_node.parent == new_node.parent.parent.children[0] \
                    and new_node.parent.parent.children[1] is not None:
                uncle = new_node.parent.parent.children[1]
                right_uncle = True
                logging.debug(
                    f'''uncle: {uncle},
                        right_uncle: {right_uncle},
                        parent: {new_node.parent},
                        new_node: {new_node},
                        grandparent: {new_node.parent.parent}''')

            elif new_node.parent == new_node.parent.parent.children[1] \
                    and new_node.parent.parent.children[0] is not None:
                uncle = new_node.parent.parent.children[0]
                right_uncle = False
                logging.debug(
                    f'''uncle: {uncle},
                        right_uncle: {right_uncle},
                        parent: {new_node.parent},
                        new_node: {new_node},
                        grandparent: {new_node.parent.parent}''')

            # no uncle
            else:

                # rotate

                #   G (b)
                #    \                P (b)
                #     P (r)    ->    /    \
                #      \          G (r) node (r)
                #      node (r)

                if new_node.parent.data <= new_node.data and \
                        new_node.parent.parent.data <= new_node.parent.data:

                    logging.debug(
                        f'''parent: {new_node.parent},
                            new_node: {new_node},
                            grandparent: {new_node.parent.parent},
                            left''')
                    new_node.parent.color = 'black'
                    logging.debug(self.root.color)
                    new_node.parent.parent.color = 'red'
                    logging.debug(self.root.color)
                    self._left_rotate(new_node.parent.parent)

                #   G (b)           G (b)
                #    \               \                  node (b)
                #     P (r)    ->    node (r)           /    \
                #     /                \             G (r)   P (r)
                #   node (r)           P (r)

                elif new_node.parent.data >= new_node.data and \
                        new_node.parent.parent.data <= new_node.parent.data:

                    logging.debug(
                        f'''parent: {new_node.parent},
                            new_node: {new_node},
                            grandparent: {new_node.parent.parent},
                            right-left''')
                    new_node.color = 'black'
                    logging.debug(self.root.color)
                    new_node.parent.parent.color = 'red'
                    logging.debug(self.root.color)
                    self._right_rotate(new_node.parent)
                    self._left_rotate(new_node.parent)

                #     G (b)          G (b)
                #     /              /               node (b)
                #   P (r)    ->    node (r) ->       /    \
                #     \            /              P (r)  G (r)
                #     node (r)   P (r)

                elif new_node.parent.data <= new_node.data and \
                        new_node.parent.parent.data >= new_node.parent.data:

                    logging.debug(
                        f'''parent: {new_node.parent},
                            new_node: {new_node},
                            grandparent: {new_node.parent.parent},
                            left-right''')
                    new_node.color = 'black'
                    logging.debug(self.root.color)
                    new_node.parent.parent.color = 'red'
                    logging.debug(self.root.color)
                    self._left_rotate(new_node.parent)
                    self._right_rotate(new_node.parent)

                #      G (b)
                #      /            P (b)
                #    P (r)    ->   /    \
                #    /        node (r) G (r)
                # node (r)

                else:

                    logging.debug(
                        f'''parent: {new_node.parent},
                            new_node: {new_node},
                            grandparent: {new_node.parent.parent},
                            right''')
                    new_node.parent.color = 'black'
                    logging.debug(self.root.color)
                    new_node.parent.parent.color = 'red'
                    logging.debug(self.root.color)
                    self._right_rotate(new_node.parent.parent)

                return

            if uncle.color == 'red':
                self.recolor(new_node, uncle)

            else:
                self.rotate_and_recolor(new_node, right_uncle)

    def recolor(self, node: RBTreeNode, uncle: RBTreeNode) -> None:
        """
        Recolor nodes in the red-black tree after insertion.

        Parameters
        ----------
        node: RBTreeNode
            The newly inserted node.

        uncle: RBTreeNode
            The uncle node of the newly inserted node.

        Returns
        -------
        None

        """

        logging.debug('recoloring')
        node.parent.color = 'black'
        logging.debug(self.root.color)
        uncle.color = 'black'
        logging.debug(self.root.color)
        if node.parent.parent is not self.root:
            node.parent.parent.color = 'red'
            logging.debug(self.root.color)
            self.handle_rb(node.parent.parent)

    def rotate_and_recolor(self, node: RBTreeNode, right: bool) -> None:
        """
        Rotate and recolor nodes in the red-black tree after insertion.

        Parameters
        ----------
        node: RBTreeNode
            The newly inserted node.

        right: bool
            Flag indicating if the uncle of the newly inserted node is on
            the right (in this case is True) or on the left (False).

        Returns
        -------
        None

        """

        logging.debug('recoloring and rotating')
        # grandparent to red
        node.parent.parent.color = 'red' \
            if node.parent.parent is not self.root \
            else 'black'
        logging.debug(self.root.color)
        # uncle to black
        node.parent.parent.children[1].color = 'black'
        logging.debug(self.root.color)

        # 2 cases if uncle is right_uncle
        if right:

            # either node is left_child
            if node is node.parent.children[0]:

                # node to red
                node.color = 'red'
                logging.debug(self.root.color)
                # parent to black
                node.parent.color = 'black'
                logging.debug(self.root.color)

            # or right_child
            else:

                # node to black
                node.color = 'black'
                logging.debug(self.root.color)
                # parent to red
                node.parent.color = 'red'
                logging.debug(self.root.color)

                if node.parent is not None:
                    self._left_rotate(node.parent)

            if node.parent.parent is not None:
                self._right_rotate(node.parent)

        # same stuff for left uncle case
        else:

            # left_child
            if node is node.parent.children[0]:

                # node to red
                node.color = 'red'
                logging.debug(self.root.color)
                # parent to black
                node.parent.color = 'black'
                logging.debug(self.root.color)

                if node.parent is not None:
                    self._right_rotate(node.parent)

            # right_child
            else:

                # node to black
                node.color = 'black'
                logging.debug(self.root.color)
                # parent to red
                node.parent.color = 'red'
                logging.debug(self.root.color)

            if node.parent.parent is not None:
                self._left_rotate(node.parent)

    def _left_rotate(self, node: RBTreeNode) -> None:
        """
        Perform a left rotation on the red-black tree.

        Parameters
        ----------
        node: RBTreeNode
            The node around which the rotation is performed.

        Returns
        -------
        None

        """

        # around the node - right_child0 bond
        #
        #            P                                    P
        #            |                                    |
        #           node                             right_child0
        #          /   \                 ->            /   \
        # left_child0  right_child0                  node  right_child1
        #               /    \                       /  \
        #      left_child1   right_child1  left_child0   left_child1
        #

        logging.debug(f'left rotating on {node}')

        # move right_child0 and left_child1
        right_child0 = node.children[1]
        left_child1 = right_child0.children[0]
        node.children[1] = left_child1
        if left_child1 is not None:
            left_child1.parent = node

        # reassign parent to node and right_child0
        right_child0.parent = node.parent
        if node.parent is None:
            self.root = right_child0
        elif node == node.parent.children[0]:
            node.parent.children[0] = right_child0
        else:
            node.parent.children[1] = right_child0
        right_child0.children[0] = node
        node.parent = right_child0

    def _right_rotate(self, node: RBTreeNode) -> None:
        """
        Perform a right rotation on the red-black tree.

        Parameters
        ----------
        node: RBTreeNode
            The node around which the rotation is performed.

        Returns
        -------
        None

        """

        # around the node - left_child0 bond
        #
        #                P                                  P
        #                |                                  |
        #               node                            left_child0
        #              /   \               ->             /   \
        #     left_child0  right_child0         left_child1   node
        #         /    \                                      /  \
        # left_child1 right_child1                  right_child1 right_child0
        #

        logging.debug(f'right rotating on {node}')

        # move left_child0 and right_child1
        left_child0 = node.children[0]
        right_child1 = left_child0.children[1]
        node.children[0] = right_child1
        if right_child1 is not None:
            right_child1.parent = node

        # reassign parent to node and left_child0
        left_child0.parent = node.parent
        if node.parent is None:
            self.root = left_child0
        elif node == node.parent.children[1]:
            node.parent.children[1] = left_child0
        else:
            node.parent.children[0] = left_child0
        left_child0.children[1] = node
        node.parent = left_child0

    def _delete(self, node: RBTreeNode) -> None:
        """
        Delete a node from the red-black tree.

        Parameters
        ----------
        node: RBTreeNode
            The node to be deleted.

        Returns
        -------
        None

        """

        # simple case, both non-Nones
        if node.children[0] is not None and node.children[1] is not None:
            successor = node.children[1]
            while successor.children[0] is not None:
                successor = successor.children[0]
            node.data, successor.data = successor.data, node.data
            self._delete(successor)
        # only one is None
        elif node.children[0] is not None or node.children[1] is not None:
            child = node.children[0] if node.children[0] is not None \
                else node.children[1]
            if node.parent is None:
                self.root = child
            elif node == node.parent.children[0]:
                node.parent.children[0] = child
            else:
                node.parent.children[1] = child
            child.parent = node.parent
            if node.color == 'black':
                if child.color == 'red':
                    child.color = 'black'
                else:
                    self._fix_double_black(child)
        # both Nones
        else:
            if node.parent is not None:
                node.parent.color = 'black'
                if node.parent.children[0] is node:
                    node.parent.children[0] = None
                elif node.parent.children[1] is node:
                    node.parent.children[1] = None
            else:
                self.root.data = None

    def _fix_double_black(self, node: RBTreeNode) -> None:
        """
        Fix double black violation in the red-black tree.

        Parameters
        ----------
        node: TreeNode
            The node causing the double black violation.

        Returns
        -------
        None

        """

        while node != self.root and node.color == 'black':
            if node is node.parent.children[0] \
                    and node.parent.children[1] is not None:
                sibling = node.parent.children[1]
                if sibling.color == 'red':
                    sibling.color = 'black'
                    node.parent.color = 'red'
                    self._left_rotate(node.parent)
                    sibling = node.parent.children[1]
                if sibling is not None:
                    if sibling.children[1] is not None \
                            and sibling.children[0] is not None:
                        if sibling.children[0].color == 'black' and \
                                sibling.children[1].color == 'black':
                            sibling.color = 'red'
                            node = node.parent
                        else:
                            if sibling.children[1].color == 'black':
                                sibling.children[0].color = 'black'
                                sibling.color = 'red'
                                self._right_rotate(sibling)
                                sibling = node.parent.children[1]
                            sibling.color = node.parent.color
                            node.parent.color = 'black'
                            sibling.children[1].color = 'black'
                            self._left_rotate(node.parent)
                            node = self.root
                    else:
                        break
            elif node is node.parent.children[1] \
                    and node.parent.children[0] is not None:
                sibling = node.parent.children[0]
                if sibling.color == 'red':
                    sibling.color = 'black'
                    node.parent.color = 'red'
                    self._right_rotate(node.parent)
                    sibling = node.parent.children[0]
                if sibling is not None:
                    if sibling.children[1] is not None \
                            and sibling.children[0] is not None:
                        if sibling.children[1].color == 'black' and \
                                sibling.children[0].color == 'black':
                            sibling.color = 'red'
                            node = node.parent
                        else:
                            if sibling.children[0].color == 'black':
                                sibling.children[1].color = 'black'
                                sibling.color = 'red'
                                self._left_rotate(sibling)
                                sibling = node.parent.children[0]
                            sibling.color = node.parent.color
                            node.parent.color = 'black'
                            sibling.children[0].color = 'black'
                            self._right_rotate(node.parent)
                            node = self.root
                    else:
                        break
            else:
                break
        node.color = 'black'
