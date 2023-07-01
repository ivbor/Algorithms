from Algorythms.python_solutions.vector import Vector
import subprocess

# neither os.get_terminal_size() nor shutil give right terminal size
# hence, have to write this function


def get_terminal_width():
    out = subprocess.Popen('''tput cols'''.split(), stdout=subprocess.PIPE)
    out = out.communicate()[0]
    cols = out.split(b'\n')[0]
    return int(cols)


def swap(a, x, y):
    b = a[x]
    a[x] = a[y]
    a[y] = b

# test heap_sort


class Heap(Vector):
    # binary tree with min in parents and elts > min in children in each node

    # all we need is to rewrite insert and link append to insert (their
    # functionality will be the same)
    def __init__(self, elements=None, size=0, capacity=1):
        super().__init__(size=size, capacity=capacity)
        if elements is not None:
            for i in elements:
                self.insert(i)

    def append(self, x):
        self.insert(x)

    def get_children(self, i):
        if self.size > 2 * i + 2:
            return (self.elements[2*i+1], self.elements[2*i+2])
        elif self.size > 2 * i + 1:
            return self.elements[2 * i + 1]
        else:
            return None

    def height(self):
        size = self.size
        high = 0
        while (int(size) != 0):
            size //= 2
            high += 1
        return high

    def insert(self, x):

        if self.size + 1 >= self.capacity:
            self.increaseCapacity()

        i = self.size
        self.elements[i] = x
        self.size += 1

        # sift up
        sift_up(self.elements, i)

    # all we need is to rewrite erase to remove min
    def remove_min(self):

        if self.size <= self.capacity / 4:
            self.decreaseCapacity()

        if self.size == 0:
            raise IndexError('list assignment index out of range')

        swap(self.elements, 0, self.size - 1)
        _return = self.elements[self.size - 1]
        del self.elements[self.size - 1]
        self.size -= 1
        i = 0

        # sift down
        sift_down(self.elements, i, self.size)

        return _return

    def __repr__(self) -> str:
        res_str = ''
        elt_number = 0
        cur_str = 0
        while (cur_str < self.height() + 1):
            # 2**cur_str - amount of numbers in current str
            str_w_nums = ''
            for i in range(2**cur_str):
                if elt_number < self.size:
                    str_w_nums += (f'({elt_number + 1})' +
                                   f'{self.elements[elt_number]:8.2e}') if \
                                    self.elements[elt_number] is not None \
                                    else ' '
                    str_w_nums += ' '
                    elt_number += 1
            str_w_nums += '\n\n'
            res_str += str_w_nums
            cur_str += 1
        return res_str

    def erase(self):
        return self.remove_min()


def sift_up(a, i):
    while i > 0:
        if a[i] < a[int((i-1)/2)]:
            swap(a, i, int((i-1)/2))
            i = int((i-1)/2)
        else:
            break


def sift_down(a, i, size):
    while True:
        if size > 2*i+2:
            if (a[i] > a[2*i+2] and a[2*i+1] >= a[2*i+2]):
                swap(a, i, 2*i+2)
                i = 2*i+2
            elif (a[i] > a[2*i+1] and a[2*i+2] >= a[2*i+1]):
                swap(a, i, 2*i+1)
                i = 2*i+1
            else:
                break
        elif size > 2*i+1:
            if a[i] > a[2*i+1]:
                swap(a, i, 2*i+1)
                break
            break
        else:
            break


def heap_sort(a):

    h = Heap()
    for i in range(len(a)):
        h.insert(a[i])
    b = a.copy()
    for i in range(len(b)):
        h.capacity = h.size
        h.copy_to_new_vector()
        b[i] = h.erase()
    return b
