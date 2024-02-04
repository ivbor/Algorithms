import logging

from Algorithms.python_solutions.bst import BinarySearchTree, TreeNode
from Algorithms.python_solutions.red_black_tree import RedBlackTree


class AVLNode(TreeNode):

    def __init__(self, data):
        super().__init__(data=data)

    def height(self):

        if self.children[0] is not None:
            if self.children[1] is not None:
                return 1 + max(self.children[0].height(),
                               self.children[1].height())
            return 1 + self.children[0].height()
        else:
            if self.children[1] is not None:
                return 1 + self.children[1].height()
            return 1

    def balance_factor(self):

        height0 = 0 if self.children[0] is None \
            else self.children[0].height()
        height1 = 0 if self.children[1] is None \
            else self.children[1].height()
        return height0 - height1


class AVLTree(RedBlackTree, BinarySearchTree):

    def __init__(self):
        RedBlackTree.__init__(self)
        self.node_class = AVLNode

    def insert(self, key):
        BinarySearchTree.insert(self, key)

    def _insert(self, root: AVLNode, new_node: AVLNode):

        BinarySearchTree._insert(self, root, new_node)

        balance = root.balance_factor()

        # Left heavy
        if balance > 1:
            # Left-Left case
            if new_node.data <= root.children[0].data:
                logging.debug('going ll')
                logging.debug(f'root before rotation: {root}')
                self._right_rotate(root)
                logging.debug(f'root after rotation: {root}')
            # Left-Right case
            else:
                logging.debug('going lr')
                logging.debug(f'root before rotation: {root}')
                self._left_rotate(root.children[0])
                logging.debug(f'root after rotation: {root}')
                self._right_rotate(root)
                logging.debug(f'root after rotation: {root}')

        # Right heavy
        if balance < -1:
            # Right-Right case
            if new_node.data >= root.children[1].data:
                logging.debug('going rr')
                logging.debug(f'root before rotation: {root}')
                self._left_rotate(root)
                logging.debug(f'root after rotation: {root}')
            # Right-Left case
            else:
                logging.debug('going rl')
                logging.debug(f'root before rotation: {root}')
                self._right_rotate(root.children[1])
                logging.debug(f'root after rotation: {root}')
                self._left_rotate(root)
                logging.debug(f'root after rotation: {root}')

        logging.debug(f'at the end current root is {root}')
        logging.debug(f'at the end current self.root is {self.root}')

    def delete(self, key):
        logging.debug(f'element {key} to be deleted')
        if key is not None:
            count_key = len(
                [elt for elt in self.in_order_traversal() if elt == int(key)])
            logging.debug(
                f'how many elements {key} is in the tree: {count_key}')
        BinarySearchTree.delete(self, key)

    def _delete(self, node):
        BinarySearchTree._delete(self, node)
