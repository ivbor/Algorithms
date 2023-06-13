class Vector: # self-expanding array

    # define a vector by defining its starting capacity
    # (and elements in list-like form  if necessary)
    def __init__(self, elements = None, size = 0, capacity = 1):

        if capacity < size:
            raise NotImplementedError('Capacity of array cannot be less than its size')

        if capacity <= 0 or size < 0:
            raise NotImplementedError('Impossible memory allocation')

        if elements != None:
            if len(elements) != 0:
                self.size = len(elements)
                self.capacity = self.size * 2
        else:
            self.size = size
            self.capacity = capacity
            self.elements = [None for i in range(self.capacity)]
            # if in C - have to do malloc on self.capacity here

    # len in its essential will not lead to expected result
    # since by default vector is organized with non-null
    # length and one None element and list is not

    # using self.size instead of length will still cover
    # usual cases, but for explained above it is manually
    # corrected to recognize vector's size as expected 
    # inside __init__
    def __len__(self):
        return self.size

    def __setitem__(self, i, x):

        # handle wrong indexes and prevent from error
        # raised because of null size
        if abs(i) >= self.size and (i != 0 and self.size == 0):
            raise IndexError('list index out of range')

        # handle negative indexes            
        if i < 0:
            i = self.size + i

        # main changes to the vector while setting an item
        self.size += 1
        self.elements[i] = x

        # some memory work
        if self.size + 1 >= self.capacity:
            self.increaseCapacity()
        

    def __getitem__(self, i):

        # handle wrong indexes
        if abs(i) >= self.size:
            raise IndexError('list index out of range')

        # handle negative indexes
        if i < 0:
            return self.elements[self.size + i]
        return self.elements[i]

    def copy_to_new_vector(self):
        newVector = [None for i in range(self.capacity)]
        for i in range(self.size):
            newVector[i] = self.elements[i]
        del self.elements
        self.elements = newVector
        del newVector

    def increaseCapacity(self):
        self.capacity *= 2
        self.copy_to_new_vector()

    def decreaseCapacity(self):
        self.capacity //= 2
        self.copy_to_new_vector()

    def erase(self, i):
        if self.size <= self.capacity / 4:
            self.decreaseCapacity()
        if i < 0 or i >= self.size:
            raise IndexError('list index out of range')
        self.size -= 1
        if self.size != 0:
            del self.elements[i]
            

    def append(self, x):
        if self.size + 1 >= self.capacity:
            self.increaseCapacity()
        self.elements[self.size] = x
        self.size += 1
        

    def insert(self, x, i):

        # handle wrong indexes
        if i < 0 or i > self.size:
            raise IndexError('list index out of range')

        # handle addition of the first
        # element using insertion
        if self.size == 0:
            self.elements[0] = x
            self.size += 1
            return None

        # append using insertion
        if i == self.size:
            self.append(x)
            return None

        # insertion in its essential
        # some memory work
        if self.size + 1 >= self.capacity:
            self.increaseCapacity()

        # first create dump and drop item with index to be inserted by
        buff = self.elements[i]
        # insert by index
        self.elements[i] = x

        # if inserted index was the last -
        # append dumped item
        if i + 1 == self.size:
            self.elements[i + 1], buff = buff, self.elements[i + 1]
            self.size += 1
            return None
 
        # move all other items and append the last
        for j in range(i+1, self.size):
            self.elements[j], buff = buff, self.elements[j]
        self.elements[self.size] = buff
        self.size += 1

class CyclicVector(Vector):
    pass
