from Algorithms.python_solutions.bst import TreeNode, BinarySearchTree


class RBTreeNode(TreeNode):
    def __init__(self, data, color):
        super().__init__(data)
        self.color = color
        self.left = None
        self.right = None


class RedBlackTree(BinarySearchTree):
    def __init__(self):
        super().__init__()

    def insert(self, key):
        new_node = RBTreeNode(data=key, color='red')
        if self.root is None:
            self.root = new_node
            self.root.color = 'black'
        else:
            self._insert(self.root, new_node)
            self._fix_violation(new_node)
        self.size += 1

    # current is parent
    def _insert(self, current, new_node):
        super()._insert(current, new_node)

    def _fix_violation(self, node):
        if node.next_node is not None:
            while node != self.root and node.next_node.color == 'red':
                if node.next_node == node.next_node.next_node.left \
                   and node.next_node.next_node.right is not None:
                    uncle = node.next_node.next_node.right
                    if uncle.color == 'red':
                        node.next_node.color = 'black'
                        uncle.color = 'black'
                        node.next_node.next_node.color = 'red'
                        node = node.next_node.next_node
                    else:
                        if node == node.next_node.right:
                            node = node.next_node
                            self._left_rotate(node)
                        node.next_node.color = 'black'
                        node.next_node.next_node.color = 'red'
                        self._right_rotate(node.next_node.next_node)
                elif node.next_node.next_node.left is not None:
                    uncle = node.next_node.next_node.left
                    if uncle.color == 'red':
                        node.next_node.color = 'black'
                        uncle.color = 'black'
                        node.next_node.next_node.color = 'red'
                        node = node.next_node.next_node
                    else:
                        if node == node.next_node.left:
                            node = node.next_node
                            self._right_rotate(node)
                        node.next_node.color = 'black'
                        node.next_node.next_node.color = 'red'
                        self._left_rotate(node.next_node.next_node)
                else:
                    break
        self.root.color = 'black'

    def _left_rotate(self, node):
        right_child = node.right
        node.right = right_child.left
        if right_child.left is not None:
            right_child.left.next_node = node
        right_child.next_node = node.next_node
        if node.next_node is None:
            self.root = right_child
        elif node == node.next_node.left:
            node.next_node.left = right_child
        else:
            node.next_node.right = right_child
        right_child.left = node
        node.next_node = right_child

    def _right_rotate(self, node):
        left_child = node.left
        node.left = left_child.right
        if left_child.right is not None:
            left_child.right.next_node = node
        left_child.next_node = node.next_node
        if node.next_node is None:
            self.root = left_child
        elif node == node.next_node.right:
            node.next_node.right = left_child
        else:
            node.next_node.left = left_child
        left_child.right = node
        node.next_node = left_child

    def delete(self, key):
        super().delete(data=key, is_rb=True)

    def _delete_rb(self, node):

        if node.left is not None and node.right is not None:
            successor = node.right
            while successor.left is not None:
                successor = successor.left
            node.data, successor.data = successor.data, node.data
            self._delete_rb(successor)
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
            if node.color == 'black':
                if child.color == 'red':
                    child.color = 'black'
                else:
                    self._fix_double_black(child)
        else:
            if node.next_node is not None:
                node.next_node.color = 'black'
                if node.next_node.left is node:
                    node.next_node.left = None
                elif node.next_node.right is node:
                    node.next_node.right = None
            else:
                self.root.data = None

    def _fix_double_black(self, node: TreeNode):
        while node != self.root and node.color == 'black':
            if node is node.next_node.left \
                    and node.next_node.right is not None:
                sibling = node.next_node.right
                if sibling.color == 'red':
                    sibling.color = 'black'
                    node.next_node.color = 'red'
                    self._left_rotate(node.next_node)
                    sibling = node.next_node.right
                if sibling is not None:
                    if sibling.right is not None and sibling.left is not None:
                        if sibling.left.color == 'black' and \
                                sibling.right.color == 'black':
                            sibling.color = 'red'
                            node = node.next_node
                        else:
                            if sibling.right.color == 'black':
                                sibling.left.color = 'black'
                                sibling.color = 'red'
                                self._right_rotate(sibling)
                                sibling = node.next_node.right
                            sibling.color = node.next_node.color
                            node.next_node.color = 'black'
                            sibling.right.color = 'black'
                            self._left_rotate(node.next_node)
                            node = self.root
                    else:
                        break
            elif node is node.next_node.right \
                    and node.next_node.left is not None:
                sibling = node.next_node.left
                if sibling.color == 'red':
                    sibling.color = 'black'
                    node.next_node.color = 'red'
                    self._right_rotate(node.next_node)
                    sibling = node.next_node.left
                if sibling is not None:
                    if sibling.right is not None and sibling.left is not None:
                        if sibling.right.color == 'black' and \
                                sibling.left.color == 'black':
                            sibling.color = 'red'
                            node = node.next_node
                        else:
                            if sibling.left.color == 'black':
                                sibling.right.color = 'black'
                                sibling.color = 'red'
                                self._left_rotate(sibling)
                                sibling = node.next_node.left
                            sibling.color = node.next_node.color
                            node.next_node.color = 'black'
                            sibling.left.color = 'black'
                            self._right_rotate(node.next_node)
                            node = self.root
                    else:
                        break
            else:
                break
        node.color = 'black'
