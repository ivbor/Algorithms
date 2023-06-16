# hash for nums and for strings (with open addresses and with chains)
# Bloom filter
# Cuckoo hashing
# get familiar with hashes: MD5, SHA, YMMV, FNV, SuperFastHash
# TODO convert or define everything to magical, get all methods to convert keys to hashed keys

# Dynamic programming (backpack problem) from Lesson 6: O(n*W) instead of 2^n on low W

import Lesson4, random

class HashTable(Lesson4.Vector):

    # generate list of prime numbers

    # Sieve of Eratosthenes
    # Code by David Eppstein, UC Irvine, 28 Feb 2002
    # http://code.activestate.com/recipes/117119/

    def gen_primes():
        """ Generate an infinite sequence of prime numbers.
        """
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

    def get_hash(x, a = self.capacity):

        # polynomial hash
        h = sum(ord(character) for power, character in enumerate(repr(x))) % a
        return h

    def gen_prime(stop = 30): # 31 is a nice start as a capacity
        gen = self.gen_primes()
        for i in gen:
            if i > stop:
                return i

    def insert(self, x, i):
        i = self.get_hash(i, self.a, self.capacity)
        super.insert(x, i)


    def increaseCapacity(self):
        self.capacity = self.gen_prime(capacity*2) # in order to make amortized time to work
        self.a = self.gen_prime(2 + capacity//2) # two times lower than capacity to decrease calculation complexity and more than two to make hash to work
        self.copy_to_new_vector()

    def __init__(self, capacity = 30):
        super.__init__(capacity = self.gen_prime(capacity))
        a = self.gen_prime(2 + capacity//2)
        p = self.gen_prime(capacity)


