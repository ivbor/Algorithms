from Algorithms.python_solutions.DoubleNode import DoubleNode
from Algorithms.python_solutions.Stack import Stack
from Algorithms.python_solutions.Queue import Queue


class Deque(Queue, Stack):  # <(out)-(in)> Deck <(out)-(in)>

    # push from Queue
    def push_back(self, value):
        Queue.push(self, value)

    # pop from Queue
    def pop_front(self):
        Queue.pop(self)

    # pop from Stack
    def pop_back(self):
        Stack.pop(self)

    def push_front(self, value):
        # for the first element
        if self.size == 0:
            newNode = DoubleNode(value, None, None)
            self.head = newNode
            self.tail = self.head
            self.size += 1
        # for other elements
        else:
            newNode = DoubleNode(value, None, self.head)
            self.head.prev_node = newNode
            self.head = self.head.prev_node
            self.size += 1
