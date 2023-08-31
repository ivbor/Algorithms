from Algorithms.python_solutions.DoubleNode import DoubleNode
from Algorithms.python_solutions.Stack import Stack


class Queue(Stack):  # (FIFO) -(in)> Queue -(out)>

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
            _return = self.head.data
            buff = self.head.next_node
            del self.head
            self.head = buff
        self.size -= 1
        return _return
