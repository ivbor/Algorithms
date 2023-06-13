class Node:

    '''
        Simple one-way Node
        Can store data in self.data
        Can store next node in self.next_node
        Works next() for next node
        Works print() (and str()) for self.data
    '''

    def __init__(self, data = None, next_node = None):
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

    def __init__(self, head = None, tail = None):

        # save the head if exists
        self.head = head

        # check a connection between head and tail
        # if they both are mentioned

        # check whether head is available
        if (head != None):

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
                while (node != None):
                    if next(node) != None:
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
            if type(cur.next_node) == Node:
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
        if type(self.head) != Node:
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


class CyclicLinkedList(LinkedList):

    '''
        Works like LL, except it is cycled
        which means connection between tail
        and head with all consequences:
        list_all(), __iter__() work differently
        append deos not work since it can not be
        defined correctly
    '''

    def __init__(self):
        super().__init__(self)
        if self.tail is not None:
            self.tail.next_node = self.head

    def list_all(self):
        ret = list()
        ctr = 0
        for i in self:
            ret.append(i)
            ctr += 1
            if ctr == self.size:
                break
        return ret

    def insert(self, x, i):
        if i < 0:
            return None
        # for the first element
        if self.size == 0:
            newNode = DoubleNode(x, None, None)
            self.head = newNode
            self.tail = self.head
            self.head.next_node = self.tail
            self.head.prev_node = self.tail
            self.tail.next_node = self.head
            self.tail.prev_node = self.head
            self.size += 1
        # insert in the head = append
        elif i == 0:
            newNode = DoubleNode(x, self.tail, self.head)
            self.head.prev_node = newNode
            self.tail.next_node = newNode
            self.head = newNode
            self.size += 1
        # insert in the tail = append
        elif i == self.size:
            newNode = DoubleNode(x, self.tail, self.head)
            self.head.prev_node = newNode
            self.tail.next_node = newNode
            self.tail = newNode
            self.size += 1
        # otherwise - dig for i-th element
        else:
            cur = self.head # i=0
            j = 0
            while j < i:
                cur = cur.next_node
                j += 1
            # and do insert
            newNode = DoubleNode(x, cur.prev_node, cur)
            cur.prev_node.next_node = newNode
            cur.prev_node = newNode
            cur = newNode
            self.size += 1

    def erase(self, i):
        if i < 0:
            return None
        # for the last element
        if self.size == 1:
            del self.head
            del self.tail
            self.head = None
            self.tail = None
        # if head is to erase
        elif i % self.size == 0:
           cur = self.head
           cur = cur.next_node
           cur.prev_node = self.tail
           cur.prev_node.next_node = cur
           del self.head
           self.head = cur
        # if tail is to erase
        elif i % self.size == self.size - 1:
           cur = self.tail
           cur = cur.prev_node
           cur.next_node = self.head
           cur.next_node.prev_node = cur
           del self.tail
           self.tail = cur
        # otherwise - dig for i-th element
        else:
            cur = self.head # i=0
            j = 0
            while j < i:
                cur = cur.next_node
                j += 1
            # copy links to buff
            buff_next = cur.next_node
            buff_prev = cur.prev_node
            # delete i-th element and
            del cur
            # change cur pointer
            cur = buff_next
            # assign new links
            cur.prev_node = buff_prev
            cur.prev_node.next_node = cur
        self.size -= 1
