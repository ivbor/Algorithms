class Node:
    '''
        Simple one-way Node
        Can store data in self.data
        Can store next node in self.next_node
        Works next() for next node
        Works print() (and str()) for self.data
    '''

    def __init__(self, data=None, next_node=None):
        self._data = data

        # Nodes can only be connected with nodes or Nones
        if (next_node.__class__.__name__ == self.__class__.__name__)\
           or (next_node is None):
            self._next_node = next_node
        else:
            raise TypeError('Wrong type of next node')

    def __str__(self):
        return str(self._data)

    def __next__(self):
        return self._next_node

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self is other

    @property
    def next_node(self):
        return self._next_node

    @next_node.setter
    def next_node(self, next_node):
        if (next_node.__class__.__name__ == self.__class__.__name__)\
           or (next_node is None):
            self._next_node = next_node
        else:
            raise TypeError('Wrong type of next node')

    @property
    def data(self):
        ret = self._data
        return ret

    @data.setter
    def data(self, data):
        self._data = data
