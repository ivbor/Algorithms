# hash for nums and for strings (with open addresses and with chains)
# Bloom filter
# Cuckoo hashing
# get familiar with hashes: MD5, SHA, YMMV, FNV, SuperFastHash
# TODO convert or define everything to magical, get all methods to convert
# keys to hashed keys

# Dynamic programming (backpack problem) from Lesson 6: O(n*W) instead of
# 2^n on low W


from Algorythms.python_solutions.vector import Vector
import random

# generate list of prime numbers

# Sieve of Eratosthenes
# Code by David Eppstein, UC Irvine, 28 Feb 2002
# http://code.activestate.com/recipes/117119/


def gen_primes():
    """ Generate an infinite sequence of prime numbers."""
    # Maps composites to primes witnessing their compositeness.
    # This is memory efficient, as the sieve is not "run forward"
    # indefinitely, but only as long as required by the current
    # number being tested.
    #
    D = {}

    # The running integer that's checked for primeness
    q = 2

    while True:
        if q not in D:
            # q is a new prime.
            # Yield it and mark its first multiple that isn't
            # already marked in previous iterations
            #
            yield q
            D[q * q] = [q]
        else:
            # q is composite. D[q] is the list of primes that
            # divide it. Since we've reached q, we no longer
            # need it in the map, but we'll mark the next
            # multiples of its witnesses to prepare for larger
            # numbers
            #
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]
        q += 1


def gen_prime(stop=30):  # 31 is a nice start as a capacity
    gen = gen_primes()
    for i in gen:
        if i > stop:
            return i


class HashTable(Vector):

    def __init__(self, capacity=30):
        super().__init__(capacity=gen_prime(capacity))

    def get_hash(self, x):
        # polynomial hash
        h = sum([ord(character) ** power
                 for power, character in
                 enumerate(str.__repr__(str(x)).lstrip("'"), 1)]) \
                 % self.capacity
        return h

    # dict-like pattern: each element in elements is a pair of
    # key and value
    def __setitem__(self, i, x):
        if self.size != 0:
            super().__setitem__(self.get_hash(i), (i, x))
        else:
            # only main changes
            # do not have to do memory work, since capacity = 31
            self.size += 1
            self.elements[self.get_hash(i)] = (i, x)

    def __getitem__(self, i):
        if self.elements[self.get_hash(i)][0] == i:
            return self.elements[self.get_hash(i)][1]

    def insert(self, x, i):
        i_hashed = self.get_hash(i)
        if i_hashed < self.size:
            super().insert((i, x), i_hashed)
        elif i_hashed >= self.size and \
                i_hashed < self.capacity:
            self.elements[i_hashed] = (i, x)
            self.size += 1
        else:
            self.increaseCapacity()
            self.insert(x, i)

    def append(self, x):
        self.insert(x, self.size + 1)

    def increaseCapacity(self):
        # in order to make amortized time to work
        self.capacity = gen_prime(self.capacity * 2)
        self.copy_to_new_vector()

    def copy_to_new_vector(self):
        newVector = [None for i in range(self.capacity)]
        for i in range(self.size):
            newVector[self.get_hash(i)] = self.elements[i]
        del self.elements
        self.elements = newVector
        del newVector
