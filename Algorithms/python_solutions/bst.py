from Algorithms.python_solutions.Node import Node


class TreeNode(Node):
    def __init__(self, data):
        super().__init__(data=data)
        self.left = None
        self.right = None


class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def insert(self, data):
        new_node = TreeNode(data=data)
        if self.root is None:
            self.root = new_node
        else:
            self._insert(self.root, new_node)
        self.size += 1

    def _insert(self, root, new_node):
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

    def delete(self, data, is_rb=False):
        if self.size == 0:
            raise IndexError('Tree is empty')
        node = self._search(self.root, data)
        if node is not None:
            if is_rb:
                self._delete_rb(node)
            else:
                self._delete(node)
        self.size -= 1

    def _delete(self, node):
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

    def search(self, data):
        return self._search(self.root, data)

    def _search(self, root, data):
        if root is None or root.data == data:
            return root
        if data < root.data:
            return self._search(root.left, data)
        return self._search(root.right, data)

    def in_order_traversal(self):
        result = []
        self._in_order_traversal_rec(self.root, result)
        return result if result != [None] else []

    def _in_order_traversal_rec(self, root, result):
        if root:
            self._in_order_traversal_rec(root.left, result)
            result.append(root.data)
            self._in_order_traversal_rec(root.right, result)

    def find_min(self):
        if self.root is None:
            return None
        return self._min_value_node(self.root).data

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def find_max(self):
        if self.root is None:
            return None
        return self._max_value_node(self.root).data

    def _max_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.right
        return current

    # after data in traversal
    def find_successor(self, data):
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
    def find_predecessor(self, data):
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

    def is_empty(self):
        return self.root is None
