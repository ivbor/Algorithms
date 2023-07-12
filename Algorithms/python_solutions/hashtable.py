# hash for nums and for strings (with open addresses and with chains)
# Bloom filter
# Cuckoo hashing
# hashlib, get familiar with hashes: YMMV, FNV, SuperFastHash

# Dynamic programming (backpack problem) from Lesson 6: O(n*W) instead of
# 2^n on low W

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


class HashTable():

    def __init__(self, capacity=30, resolving='closed', load_factor_thr=0.6):
        '''
            Supports closed chains and linear probing type of
            open addressing
        '''
        self.resolving_method = resolving
        self.capacity = gen_prime(capacity)
        self._pairs = Vector(capacity=self.capacity)
        self.size = 0
        self.load_factor_thr = load_factor_thr

    def get_hash(self, x):
        # polynomial hash
        h = sum([ord(character) ** power
                 for power, character in
                 enumerate(str.__repr__(str(x)).lstrip("'"), 1)]) \
                 % self.capacity
        return h

    @property
    def pairs(self):
        ret = self._pairs.elements.copy()
        return ret

    def probe(self, key):
        index = self.get_hash(key)
        for _ in range(self.capacity):
            yield index, self._pairs[index]
            index = (index + 1) % self.capacity

    def __setitem__(self, i, x):
        # case by resolving method
        if self.size / self.capacity > self.load_factor_thr:
            self.increase_size()
        if self.resolving_method == 'closed':
            i_hashed = self.get_hash(i)
            self.closed_setitem(i_hashed, i, x)
        elif self.resolving_method == 'linear':
            for index, pair in self.probe(i):
                if pair is None or pair.key == i:
                    self._pairs[index] = Pair(i, x)
                    self.size += 1
                    break

    # dict-like pattern: each element in elements is a pair of
    # key and value
    def closed_setitem(self, i, key, x):
        if self._pairs[i] is None:
            # no collision
            self._pairs[i] = Pair(key, x)
            self.size += 1
        elif self._pairs[i] is not None and type(self._pairs[i]) != deque:
            # resolve collision with creating deque
            first_in_deque = self._pairs[i].value
            del self._pairs[i]
            self._pairs[i] = deque()
            self._pairs[i].append(Pair(key, first_in_deque))
            self._pairs[i].append(Pair(key, x))
        else:
            # when deque already exists
            self._pairs[i].append(Pair(key, x))

    def __getitem__(self, i):
        # case by resolving method
        if self.resolving_method == 'closed':
            return self.closed_getitem(i)
        elif self.resolving_method == 'linear':
            for _, pair in self.probe(i):
                if pair is None:
                    raise KeyError(i)
                if pair.key == i:
                    return pair.value
            raise KeyError(i)

    def closed_getitem(self, i):
        deque_or_pair_or_none = self._pairs[self.get_hash(i)]
        if deque_or_pair_or_none is None:
            raise KeyError(i)
        elif type(deque_or_pair_or_none) == deque:
            for pair in [pair for pair in deque_or_pair_or_none]:
                if pair[0] == i:
                    return pair[1]
        else:
            return deque_or_pair_or_none.value

    def increase_size(self):
        # in order to make amortized time to work
        self.capacity = gen_prime(self.capacity * 2)
        self.resize_and_rehash()

    def resize_and_rehash(self):
        newVector = [None for i in range(self.capacity)]
        for i in range(self.size):
            newVector[self.get_hash(i)] = self._pairs[i]
        del self._pairs
        self._pairs = newVector
        del newVector

    def decrease_size(self):
        self.capacity //= 2
        self.resize_and_rehash()

    def __delitem__(self):
        pass
