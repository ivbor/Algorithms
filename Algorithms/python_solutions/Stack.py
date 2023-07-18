from Algorithms.python_solutions.DoubleNode import DoubleNode


class Stack:  # (LIFO)   <(out)-(in)> Stack |

    def __init__(self):

        self.head = None
        self.tail = None
        self.size = 0

    def push(self, value):
        # for the first element
        if self.size == 0:
            newNode = DoubleNode(value, None, None)
            self.head = newNode
            self.tail = self.head
            self.size += 1
        # for other elements
        else:
            newNode = DoubleNode(value, self.tail, None)
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
        return self.tail.data if self.tail is not None else None

    def front(self):
        '''
            Front of Stack is from where
            elements are inaccessible
        '''
        return self.head.data if self.head is not None else None

    def __len__(self):
        return self.size
