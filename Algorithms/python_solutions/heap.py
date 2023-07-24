from Algorithms.python_solutions.vector import Vector
import subprocess

# neither os.get_terminal_size() nor shutil give right terminal size
# hence, have to write this function


def get_terminal_width():
    out = subprocess.Popen('''tput cols'''.split(), stdout=subprocess.PIPE)
    out = out.communicate()[0]
    cols = out.split(b'\n')[0]
    return int(cols)


def swap(array, x, y):
    b = array[x]
    array[x] = array[y]
    array[y] = b


class Heap(Vector):
    '''
        binary tree with min in parents and elts > min in children in each node
    '''

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

        sift_up(self.elements, i)

    def __iter__(self):
        for i in self.elements[:self.size]:
            yield i

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

        sift_down(self.elements, i, self.size)

        return _return

    def __repr__(self) -> str:
        string_to_print = ''
        index_of_element_to_print = 0
        current_height = 0
        while (current_height < self.height() + 1):

            # 2**cur_str - amount of numbers in current str
            string_on_current_height = ''
            for _ in range(2**current_height):
                if index_of_element_to_print < self.size:
                    string_on_current_height += \
                        (f'({index_of_element_to_print + 1})' +
                         f'{self.elements[index_of_element_to_print]:8.2e}') \
                        if \
                        self.elements[index_of_element_to_print] is not None \
                        else ' '
                    string_on_current_height += ' '
                    index_of_element_to_print += 1
            string_on_current_height += '\n\n'
            string_to_print += string_on_current_height
            current_height += 1
        return string_to_print

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


def heap_sort(array):

    heap = Heap()
    for i in range(len(array)):
        heap.insert(array[i])
    new_array = array.copy()
    for i in range(len(new_array)):
        heap.capacity = heap.size
        heap.copy_to_new_vector()
        new_array[i] = heap.erase()
    return new_array
