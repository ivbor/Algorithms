def swap(a, x, y):
    b = a[x]
    a[x] = a[y]
    a[y] = b

# test heap_sort
class Heap(Vector): # binary tree with min in parents and elts > min in children in each node

    # all we need is to rewrite insert and link append to insert (their functionality will be the same)
    def append(self, x):
        self.insert(x)

    def h_heap(self):
        size = self.size
        high = 0
        while (int(size) != 0):
            size //= 2
            high +=1
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

    def erase(self):
        return self.remove_min()

# erase slips (determine reason and think about format print for trees inside array)

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
    for i in range(len(a)):
        h.capacity = h.size
        h.copy_to_new_vector()
        a[i] = h.erase()
