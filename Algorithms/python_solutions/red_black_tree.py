import logging

from Algorithms.python_solutions.bst import TreeNode, BinarySearchTree


class RBTreeNode(TreeNode):
    def __init__(self, data, color):
        super().__init__(data)
        self.color = color


class RedBlackTree(BinarySearchTree):

    def __init__(self):
        super().__init__()
        self.node_class = RBTreeNode

    def insert(self, key):

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

    def handle_rb(self, new_node):

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

    def recolor(self, node, uncle):
        logging.debug('recoloring')
        node.parent.color = 'black'
        logging.debug(self.root.color)
        uncle.color = 'black'
        logging.debug(self.root.color)
        if node.parent.parent is not self.root:
            node.parent.parent.color = 'red'
            logging.debug(self.root.color)
            self.handle_rb(node.parent.parent)

    def rotate_and_recolor(self, node, right):

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

    def _left_rotate(self, node):

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

    def _right_rotate(self, node):

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

    def _delete(self, node):

        if node.children[0] is not None and node.children[1] is not None:
            successor = node.children[1]
            while successor.children[0] is not None:
                successor = successor.children[0]
            node.data, successor.data = successor.data, node.data
            self._delete(successor)
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
        else:
            if node.parent is not None:
                node.parent.color = 'black'
                if node.parent.children[0] is node:
                    node.parent.children[0] = None
                elif node.parent.children[1] is node:
                    node.parent.children[1] = None
            else:
                self.root.data = None

    def _fix_double_black(self, node: TreeNode):
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
