from Algorithms.python_solutions.Node import Node


class LinkedList:
    '''
        Linked List class, connects one-way nodes
        Can be initiated by head or by head and tail

        makes possible creation not only from
        absence of nodes, but from chain of
        any length, provided head and tail

        automatically checks, if there is
        a connection between head and tail
    '''

    def __init__(self, head=None, tail=None):

        # save the head if exists
        self._head = head

        # check a connection between head and tail
        # if they both are mentioned

        # check whether head is available
        if (head is not None):

            # check if there is only 1 node
            if head != tail:

                # if not - dump first node,
                node = self._head

                # get ready to move tail,
                self._tail = self._head

                # and increase size to 1
                self._size = 1

                # move tail until the end of the
                # chain is reached
                while (node is not None):
                    if next(node) is not None:
                        node = next(node)
                    else:
                        self._tail = node
                        break
                    self._size += 1
            else:
                self._size = 1
                self._tail = self._head
        else:
            self._tail = self._head
            self._size = 0

    @property
    def head(self):
        return self._head

    @head.setter
    def head(self, head):
        self._head = head
        if self._size == 0:
            self._size += 1
            self._tail = self._head

    @property
    def tail(self):
        return self._tail

    @tail.setter
    def tail(self, tail):
        raise NotImplementedError('assigning tail is only possible' +
                                  ' through insert or initialization' +
                                  '\n' +
                                  f'use {self.__name__}.insert({tail})')

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        raise NotImplementedError('can not set size, ' +
                                  'it is calculated automatically')

    def __contains__(self, x):

        if x in self.list_all():
            return True
        else:
            return False

    def __iter__(self):

        cur = self._head
        while True:

            # protection from Attr error
            if cur is not None:
                yield cur.data
            else:
                break

            # protection from Type error
            if isinstance(cur.next_node, Node):
                cur = next(cur)

            # if the end is reached
            else:
                break

    def list_all(self):
        ret = list()
        for i in self:
            ret.append(i)
        return ret

    def __str__(self):
        return str(self.list_all())

    def __repr__(self):
        return str(self)

    def append(self, x):

        # for the first element
        if self._size == 0:
            newNode = Node(x, None)
            self._head = newNode
            self._tail = self._head
            self._size += 1
        # for other elements
        else:
            newNode = Node(x, None)
            self._tail.next_node = newNode
            self._tail = newNode
            self._size += 1

    def search(self, i):
        previous = self._head
        current = previous.next_node
        index_of_current_element = 1
        while index_of_current_element < i:
            previous = current
            current = previous.next_node
            index_of_current_element += 1
        return (previous, current)

    def insert(self, i, x):

        # for the first element
        if not isinstance(self._head, Node):
            newNode = Node(x, None)
            self._head = newNode
            self._tail = self._head
        # insert in the head
        elif i == 0:
            newNode = Node(x, None)
            newNode.next_node = self._head
            self._head = newNode
        # append using insert
        elif i == self._size + 1:
            self.append(x)
        # throw index error, insertion
        # with negative indexing is
        # an undefined operation
        elif i < 0:
            raise IndexError('Indexing is' +
                             ' only possible with non-negative' +
                             ' numbers')
        # otherwise - dig for i-th element
        else:
            previous, current = self.search(i)

            # insert i-th element
            newNode = Node(x, None)
            previous.next_node = newNode
            newNode.next_node = current
        self._size += 1

    def erase(self, i):

        # if head is to erase
        if i == 0:

            # if the list has only one Node
            if self._size == 1:
                del self._head
                self._head = None
                del self._tail
                self._tail = None
            else:
                buff = self._head.next_node
                del self._head
                self._head = buff

        # if index is negative and
        # to get to i one does not
        # have to go multiple (2 or more)
        # times to the tail,
        # no more than once
        elif i < 0 and abs(i) < self._size:

            # in this case we prevent
            # users from abusing
            # negative indexes
            # but generally allow them
            self.erase(self._size + i)

        # otherwise - dig for i-th element
        else:
            previous, current = self.search(i)

            # delete i-th element
            buff = current.next_node
            del current
            previous.next_node = buff

            # if i-th element is tail - reassign tail
            if i == self._size - 1:
                self._tail = previous
        self._size -= 1

    def update(self, i, x):

        if i < 0:
            raise IndexError('Indexing is' +
                             ' only possible with non-negative' +
                             ' numbers')
        previous, current = self.search(i)
        current.data = x
