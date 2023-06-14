class Node:

    '''
        Simple one-way Node
        Can store data in self.data
        Can store next node in self.next_node
        Works next() for next node
        Works print() (and str()) for self.data
    '''

    def __init__(self, data=None, next_node=None):
        self.data = data

        # Nodes can only be connected with nodes or Nones
        if (next_node.__class__.__name__ == self.__class__.__name__)\
           or (next_node is None):
            self.next_node = next_node
        else:
            raise TypeError('Wrong type of next node')

    def __str__(self):
        return str(self.data)

    def __next__(self):
        return self.next_node

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        return self is other


class LinkedList:

    '''
        Linked List class, connects one-way nodes
        Can be initiated by head or by head and tail

    '''

    # makes possible creation not only from
    # absence of nodes, but from chain of
    # any length, provided head and tail

    # automatically checks, if there is
    # a connection between head and tail

    def __init__(self, head=None, tail=None):

        # save the head if exists
        self.head = head

        # check a connection between head and tail
        # if they both are mentioned

        # check whether head is available
        if (head is not None):

            # check if there is only 1 node
            if head != tail:

                # if not - dump first node,
                node = self.head

                # get ready to move tail,
                self.tail = self.head

                # and increase size to 1
                self.size = 1

                # move tail until the end of the
                # chain is reached
                while (node is not None):
                    if next(node) is not None:
                        node = next(node)
                    else:
                        self.tail = node
                        break
                    self.size += 1
            else:
                self.size = 1
                self.tail = self.head
        else:
            self.tail = self.head
            self.size = 0

    def contains(self, x):

        if x in self.list_all():
            return True

    # works fine if launched O(1) times
    def __iter__(self):

        cur = self.head
        while True:

            # protection from Attr error
            if cur is not None:
                yield cur.data
            else:
                break

            # protection from Type error
            if isinstance(cur.next_node, Node):
                cur = cur.next_node

            # if the end is reached
            else:
                break

    # can't use iter there due to
    # calculative inefficiency
    def __repr__(self):
        self.list_all()

    # repr restrictions apply here too
    # instead of calling everytime iter
    # better write list_all() method to
    # write everything to the memory once
    # and then use it where necessary
    def list_all(self):
        ret = list()
        for i in self:
            ret.append(i)
        return ret

    def __str__(self):
        return str(self.list_all())

    def append(self, x):

        # for the first element
        if self.size == 0:
            newNode = Node(x, None)
            self.head = newNode
            self.tail = self.head
            self.size += 1
        # for other elements
        else:
            newNode = Node(x, None)
            self.tail.next_node = newNode
            self.tail = newNode
            self.size += 1

    # x for value, i for index
    def insert(self, x, i):

        # for the first element
        if not isinstance(self.head, Node):
            newNode = Node(x, None)
            self.head = newNode
            self.tail = self.head
            self.size += 1
        # insert in the head
        elif i == 0:
            newNode = Node(x, None)
            newNode.next_node = self.head
            self.head = newNode
            self.size += 1
        # append using insert
        elif i == self.size + 1:
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
            prev = self.head
            cur = prev.next_node
            j = 1
            while j < i:
                prev = cur
                cur = prev.next_node
                j += 1
            # list[i] = prev
            # list[i+1] = cur
            newNode = Node(x, None)
            prev.next_node = newNode
            newNode.next_node = cur
            self.size += 1

    def erase(self, i):

        # if head is to erase
        if i == 0:

            # if the list has only one Node
            if self.size == 1:
                del self.head
                self.head = None
                del self.tail
                self.tail = None
            else:
                buff = self.head.next_node
                del self.head
                self.head = buff

        # if index is negative and
        # to get to i one does not
        # have to go multiple (2 or more)
        # times to the tail,
        # no more than once
        elif i < 0 and abs(i) < self.size:

            # in this case we prevent
            # users from abusing
            # negative indexes
            # but generally allow them
            self.erase(self.size + i)

        # otherwise - dig for i-th element
        else:
            prev = self.head
            cur = prev.next_node
            j = 1
            while j < i:
                prev = cur
                cur = prev.next_node
                j += 1

            # delete i-th element
            buff = cur.next_node
            del cur
            prev.next_node = buff

            # if i-th element is tail - reassign tail
            if i == self.size - 1:
                self.tail = prev
        self.size -= 1

    def update(self, x, i):

        if i < 0:
            raise IndexError('Indexing is' +
                             ' only possible with non-negative' +
                             ' numbers')
        self.erase(i)
        self.insert(x, i)
