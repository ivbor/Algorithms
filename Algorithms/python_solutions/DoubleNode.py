from Algorithms.python_solutions.Node import Node

# import this too if you want to have the same syntax
# for prev as for built-in next():
# prev(DoubleNode()) instead of DoubleNode().prev()


def prev(obj):
    return obj.prev()


class DoubleNode(Node):

    '''
        Two-ways Node
        Same as Node but
        works prev() for previous node
    '''

    def __init__(self, data=None, prev_node=None, next_node=None):
        self._data = data

        # DoubleNodes can only be connected with DoubleNodes or Nones
        if next_node.__class__.__name__ == \
                self.__class__.__name__ or next_node is None:
            self._next_node = next_node
        else:
            raise TypeError('Wrong type of next_node')

        if (prev_node.__class__.__name__ == self.__class__.__name__)\
           or (prev_node is None):
            self._prev_node = prev_node
        else:
            raise TypeError('Wrong type of prev node')

    @property
    def prev_node(self):
        return self._prev_node

    @prev_node.setter
    def prev_node(self, prev_node):
        if prev_node.__class__.__name__ == \
                self.__class__.__name__ or prev_node is None:
            self._prev_node = prev_node
        else:
            raise TypeError('Wrong type of next_node')

    def prev(self):
        return self.prev_node
