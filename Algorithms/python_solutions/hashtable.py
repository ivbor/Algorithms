# hash for nums and for strings (with open addresses and with chains)
# Bloom filter
# Cuckoo hashing

# Dynamic programming (backpack problem) from Lesson 6: O(n*W) instead of
# 2^n on low W
import hashlib
from collections import deque
from typing import Any, NamedTuple
from Algorithms.python_solutions.vector import Vector


class Pair(NamedTuple):
    key: Any
    value: Any


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


def poly_hash(x):
    return sum([ord(character) ** power
                for power, character in
                enumerate(str.__repr__(str(x)).lstrip("'"), 1)])


class HashTable_closed():

    def __init__(self, capacity=30, hashfunc='poly'):
        '''
            Usual hashtable using closed chains as method of
            resolving collisions

            Args:
                capacity - initial length
                load_factor_thr - load factor threshold
                when the size of the hashtable divided by capacity
                reaches this threshold hashtable will resize and rehash
                hashfunc - function used for hashing, may be callable
                or one of the following: poly for polynomial hash,
                md5, sha1
        '''
        self._capacity = gen_prime(capacity)
        self._pairs = Vector(elements=[deque()
                                       for _ in range(self._capacity)])
        # since vector by itself has Nones inside by default
        # have to cut the slice of it so that no Nones would be
        # left inside vector
        self._pairs = self._pairs.elements[:self._capacity]
        self._size = 0
        self._max_deque_len = self._capacity // 2
        self._hashfunc = hashfunc

    def get_hash(self, x):
        if self._hashfunc == 'poly':
            # polynomial hash
            return poly_hash(x) % self._capacity
        elif self._hashfunc == 'md5':
            return int(hashlib.md5(x.encode()).hexdigest(), 16) \
                % self._capacity
        elif self._hashfunc == 'sha1':
            return int(hashlib.sha1(x.encode()).hexdigest(), 16) \
                % self._capacity
        elif callable(self._hashfunc):
            return self._hashfunc(x)

    @property
    def pairs(self):
        ret = self._pairs.elements.copy()
        return ret

    @pairs.setter
    def pairs(self, pair):
        raise NotImplementedError('cannot set value to protected property' +
                                  'to append or set value use ' +
                                  'traditional setitem method: ' +
                                  f'{self.__name__}[{pair[0]}] = {pair[1]}')

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        raise NotImplementedError('cannot set value to protected property')

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        raise NotImplementedError('cannot set value to protected property')

    def __len__(self):
        return self._size

    def __setitem__(self, key, x):
        # update by delete and reset
        del self[key]
        hashed_key = self.get_hash(key)
        while self._pairs[hashed_key] is None:
            self.increase_capacity()
        self._pairs[hashed_key].append(Pair(key, x))
        self._size += 1
        if len(self._pairs[hashed_key]) > self._max_deque_len:
            self.increase_capacity()

    def __getitem__(self, i):
        for pair in [pair for pair in self._pairs[self.get_hash(i)]]:
            key = pair[0]
            value = pair[1]
            if key == i:
                return value
        raise KeyError('no value for corresponding key present')

    def increase_capacity(self):
        # in order to make amortized time to work capacity will be
        # increased to double immediately, instead of + 1 for example
        old_capacity = self._capacity
        self._capacity = gen_prime(self._capacity * 2)
        for len_deque in range(5):
            print('len_deque ', len_deque)
            print(sum([len(self._pairs[i]) == len_deque
                       for i in range(old_capacity)]))
        self.recapacitate_and_rehash(old_capacity)

    def recapacitate_and_rehash(self, old_capacity):
        newVector = Vector(capacity=self._capacity,
                           elements=[deque() for _ in range(self._capacity)])
        for i in range(old_capacity):
            for pair in self._pairs[i]:
                key = pair[0]
                value = pair[1]
                newVector[self.get_hash(key)].append(
                    Pair(key=key, value=value))
        del self._pairs
        self._pairs = newVector
        del newVector

    def decrease_capacity(self):
        old_capacity = self._capacity
        self._capacity //= 2
        self.recapacitate_and_rehash(old_capacity)

    def search(self, key):
        hashed_key = self.get_hash(key)
        for index, pair in enumerate(
                [pair for pair in self._pairs[hashed_key]]):
            key_of_pair = pair[0]
            if key == key_of_pair:
                return index
        return False

    def __delitem__(self, key):
        hashed_key = self.get_hash(key)
        index = self.search(key)
        if str(index) != 'False':
            del self._pairs[hashed_key][index]
            self._size -= 1
            if self._size <= self._capacity * 3:
                self.decrease_capacity()

    def to_dict(self):
        result = dict()
        for i in self._pairs:
            for j in i:
                result[j.key] = j.value
        return result

    def __contains__(self, key):
        if str(self.search(key)) == 'False':
            return False
        else:
            return True
