from Algorythms.python_solutions import Nodes
from Algorythms.python_solutions.Nodes import LinkedList

# import this too if you want to have the same syntax
# for prev as for built-in next():
# prev(DoubleNode()) instead of DoubleNode().prev()


def prev(obj):
    return obj.prev()


class DoubleNode(Nodes.Node):

    '''
        Two-ways Node
        Same as Node but
        works prev() for previous node
    '''

    def __init__(self, data=None, prev_node=None, next_node=None):
        super().__init__(data, next_node)

        # DoubleNodes can only be connected with DoubleNodes or Nones
        if (prev_node.__class__.__name__ == self.__class__.__name__)\
           or (prev_node is None):
            self.prev_node = prev_node
        else:
            raise TypeError('Wrong type of prev node')

    def prev(self):
        return self.prev_node


class Stack:
    # (LIFO) based on not implemented DoubleLinkedList  <(out)-(in)> Stack |

    def __init__(self):

        self.head = None
        self.tail = None
        self.size = 0

    def push(self, x):
        # for the first element
        if self.size == 0:
            newNode = DoubleNode(x, None, None)
            self.head = newNode
            self.tail = self.head
            self.size += 1
        # for other elements
        else:
            newNode = DoubleNode(x, self.tail, None)
            self.tail.next_node = newNode
            self.tail = self.tail.next_node
            self.size += 1

    def pop(self):
        # for the last element
        if self.size == 1:
            _return = self.head.data
            del self.tail
            del self.head
        # for other elements
        else:
            _return = self.tail.data
            buff = self.tail.prev_node
            del self.tail
            self.tail = buff
        self.size -= 1
        return _return

    def back(self):
        '''
            Back of Stack is from where
            elements are popped
        '''
        return self.tail.data

    def front(self):
        '''
            Front of Stack is from where
            elements are inaccessible
        '''
        return self.head.data

    def __len__(self):
        return self.size


class Queue(Stack):  # (FIFO) -(in)> Queue -(out)>

    def push(self, x):
        # for the first element
        if self.size == 0:
            newNode = DoubleNode(x, None, None)
            self.head = newNode
            self.tail = self.head
            self.size += 1
        # for other elements
        else:
            newNode = DoubleNode(x, self.tail, None)
            self.tail.next_node = newNode
            self.tail = self.tail.next_node
            self.size += 1

    def pop(self):
        # for the last element
        if self.size == 1:
            _return = self.head.data
            del self.tail
            del self.head
        # for other elements
        else:
            _return = self.head.data
            buff = self.head.next_node
            del self.head
            self.head = buff
        self.size -= 1
        return _return


class Deck(Queue, Stack):  # <(out)-(in)> Deck <(out)-(in)>

    # push from Queue
    def push_back(self, x):
        Queue.push(self, x)

    # pop from Queue
    def pop_front(self):
        Queue.pop(self)

    # pop from Stack
    def pop_back(self):
        Stack.pop(self)

    def push_front(self, x):
        # for the first element
        if self.size == 0:
            newNode = DoubleNode(x, None, None)
            self.head = newNode
            self.tail = self.head
            self.size += 1
        # for other elements
        else:
            newNode = DoubleNode(x, None, self.head)
            self.head.prev_node = newNode
            self.head = self.head.prev_node
            self.size += 1

# TODO rewrite functions to use Node instead of DoubleNode
# and accordingly rewrite tests


class CyclicLinkedList(LinkedList):

    '''
        Works like LL, except it is cycled
        which means connection between tail
        and head with all consequences:
        list_all(), __iter__() work differently
        append does not work since it can not be
        defined correctly
    '''

    def __init__(self):
        super().__init__()
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
            cur = self.head  # i=0
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
            cur = self.head  # i=0
            j = 0
            while j < i:
                cur = cur.next_node
                j += 1
