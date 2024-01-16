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
        new_node.children = [None, None]
        if self.root is None:
            self.root = new_node
            self.root.color = 'black'
        else:
            self._insert(self.root, new_node)
            self._fix_violation(new_node)
        self.size += 1

    def _fix_violation(self, node):
        if node.parent is not None:
            while node != self.root and node.parent.color == 'red':
                if node.parent == node.parent.parent.children[0] \
                   and node.parent.parent.children[1] is not None:
                    uncle = node.parent.parent.children[1]
                    if uncle.color == 'red':
                        node.parent.color = 'black'
                        uncle.color = 'black'
                        node.parent.parent.color = 'red'
                        node = node.parent.parent
                    else:
                        if node == node.parent.children[1]:
                            node = node.parent
                            self._left_rotate(node)
                        node.parent.color = 'black'
                        node.parent.parent.color = 'red'
                        self._right_rotate(node.parent.parent)
                elif node.parent.parent.children[0] is not None:
                    uncle = node.parent.parent.children[0]
                    if uncle.color == 'red':
                        node.parent.color = 'black'
                        uncle.color = 'black'
                        node.parent.parent.color = 'red'
                        node = node.parent.parent
                    else:
                        if node == node.parent.children[0]:
                            node = node.parent
                            self._right_rotate(node)
                        node.parent.color = 'black'
                        node.parent.parent.color = 'red'
                        self._left_rotate(node.parent.parent)
                else:
                    break
        self.root.color = 'black'

    def _left_rotate(self, node):
        right_child = node.children[1]
        node.children[1] = right_child.children[0]
        if right_child.children[0] is not None:
            right_child.children[0].parent = node
        right_child.parent = node.parent
        if node.parent is None:
            self.root = right_child
        elif node == node.parent.children[0]:
            node.parent.children[0] = right_child
        else:
            node.parent.children[1] = right_child
        right_child.children[0] = node
        node.parent = right_child

    def _right_rotate(self, node):
        left_child = node.children[0]
        node.children[0] = left_child.children[1]
        if left_child.children[1] is not None:
            left_child.children[1].parent = node
        left_child.parent = node.parent
        if node.parent is None:
            self.root = left_child
        elif node == node.parent.children[1]:
            node.parent.children[1] = left_child
        else:
            node.parent.children[0] = left_child
        left_child.children[1] = node
        node.parent = left_child

    def delete(self, key):
        super().delete(data=key, is_rb=True)

    def _delete_rb(self, node):

        if node.children[0] is not None and node.children[1] is not None:
            successor = node.children[1]
            while successor.children[0] is not None:
                successor = successor.children[0]
            node.data, successor.data = successor.data, node.data
            self._delete_rb(successor)
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
