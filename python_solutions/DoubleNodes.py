from Algorythms.python_solutions import Nodes

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

    def __init__(self, data = None, prev_node = None, next_node = None):
        super().__init__(data, next_node)

        # DoubleNodes can only be connected with DoubleNodes or Nones
        if (prev_node.__class__.__name__ == self.__class__.__name__)\
           or (prev_node is None):
            self.prev_node = prev_node
        else:
           raise TypeError('Wrong type of prev node')

    def prev(self):
        return self.prev_node

class Stack: #(LIFO) based on not implemented DoubleLinkedList  <(out)-(in)> Stack |

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

class Queue(Stack): #(FIFO) -(in)> Queue -(out)>

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

class Deck(Queue, Stack): # <(out)-(in)> Deck <(out)-(in)>

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

