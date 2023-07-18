from Algorithms.python_solutions.DoubleNode import DoubleNode
from Algorithms.python_solutions.LinkedList import LinkedList


class CyclicLinkedList(LinkedList):

    '''
        Works like LL, except it is cycled
        which means connection between tail
        and head with all consequences:
        list_all(), __iter__() work differently
        append does not work since it can not be
        defined correctly
    '''

    def __init__(self, head=None, tail=None):
        super().__init__(head, tail)
        if self._tail is not None:
            self._tail.next_node = self._head

    def list_all(self):
        ret = list()
        ctr = 0
        for i in self:
            ret.append(i)
            ctr += 1
            if ctr == self._size:
                break
        return ret

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
        if not isinstance(self._head, DoubleNode):
            newNode = DoubleNode(x, None, None)
            self._head = newNode
            self._tail = self._head
            self._head.next_node = self._tail
            self._head.prev_node = self._tail
            self._tail.next_node = self._head
            self._tail.prev_node = self._head
        # insert in the head or tail
        elif i == 0 or i == self._size:
            newNode = DoubleNode(x, self._tail, self._head)
            self._head.prev_node = newNode
            self._tail.next_node = newNode
            if i == self._size:
                self._tail = newNode
            else:
                self._head = newNode
        elif i < 0:
            self.insert(self._size + i + 1, x)
            # no element addition - size should not change
            self._size -= 1
        elif i > self._size:
            raise IndexError('CyclicLinkedList index out of range')
        # otherwise - dig for i-th element
        else:
            previous, current = self.search(i)

            # insert i-th element
            newNode = DoubleNode(x, previous, current)
            previous.next_node = newNode
            newNode.next_node = current
        self._size += 1

    def erase(self, i):
        if self._size != 0:
            if i / self._size > 1:
                raise IndexError('CyclicLinkedList index out if range')
        else:
            raise IndexError('Nothing to erase')
        # for the last element
        if self._size == 1:
            del self._head
            del self._tail
            self._head = None
            self._tail = None
            self._size -= 1
        # if head is to erase
        elif i == 0:
            cur = self._head.next_node
            cur.prev_node = self._tail
            cur.prev_node.next_node = cur
            del self._head
            self._head = cur
            self._size -= 1
        # if tail is to erase
        elif i == self._size:
            cur = self._tail.prev_node
            cur.next_node = self._head
            cur.next_node.prev_node = cur
            del self._tail
            self._tail = cur
            self._size -= 1
        elif i < 0:
            self.erase(self._size + i)
        # otherwise - dig for i-th element
        else:
            cur = self._head
            j = 0
            while j < i:
                cur = cur.next_node
                j += 1
            # and do erasing
            cur.next_node.prev_node = cur.prev_node
            cur.prev_node.next_node = cur.next_node
            del cur
            self._size -= 1

    def update(self, i, x):
        previous, current = self.search(i)
        previous.data = x
