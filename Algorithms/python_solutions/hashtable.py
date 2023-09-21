import hashlib
import logging
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


class PairsVector(Vector):

    def __setitem__(self, key, value):
        raise NotImplementedError(
            'can only store elements inside ' +
            'hashtable with closed chaining ' +
            f'using HashTable_closed_name[{key}] = {value}')


class HashTable_closed():

    def __init__(self, capacity=30, hashfunc='md5'):
        '''
            Usual hashtable using closed chains as method of
            resolving collisions

            Args:
                capacity - initial length
        '''
        self._capacity = gen_prime(capacity)
        self._pairs = PairsVector(elements=[deque()
                                            for _ in range(self._capacity)])
        # since vector by itself has Nones inside by default
        # have to cut the slice of it so that no Nones would be
        # left inside vector
        self._pairs.elements = self._pairs.elements[:self._capacity]
        self._size = 0
        self._max_deque_len = self._capacity // 2
        self._hashfunc = hashfunc

    def get_hash(self, x):
        if self._hashfunc == 'poly':
            # polynomial hash
            return poly_hash(x) % self._capacity
        elif self._hashfunc == 'md5':
            return int(hashlib.md5(x.__repr__().encode(),
                                   usedforsecurity=False).hexdigest(), 16) \
                % self._capacity
        elif self._hashfunc == 'sha1':
            return int(hashlib.sha1(x.__repr__().encode(),
                                    usedforsecurity=False).hexdigest(), 16) \
                % self._capacity
        elif callable(self._hashfunc):
            return self._hashfunc(x) % self._capacity

    @property
    def pairs(self):
        ret = self._pairs.elements.copy()
        return ret

    @pairs.setter
    def pairs(self, value):
        raise NotImplementedError('cannot set value to protected property' +
                                  'to append or set value use setitem')

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
        hashed_key = self.get_hash(key)
        index = self.search(key)
        if not (str(index) == 'False'):
            del self._pairs[hashed_key][index]
            self._size -= 1
        self._pairs[hashed_key].append(Pair(key, x))
        self._size += 1
        if len(self._pairs[hashed_key]) > self._max_deque_len:
            self.increase_capacity()

    def __getitem__(self, i):
        hashed_key = self.get_hash(i)
        for pair in [pair for pair in self._pairs[hashed_key]]:
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
        self.recapacitate_and_rehash(old_capacity)

    def recapacitate_and_rehash(self, old_capacity):
        newVector = PairsVector(
            capacity=self._capacity, elements=[
                deque() for _ in range(
                    self._capacity)])
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
        self._capacity = self._capacity // 2 if self._capacity != 1 else 1
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
            if len(self._pairs[hashed_key]) < 1:
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

    @classmethod
    def from_dict(cls, dictionary):
        result = HashTable_closed(capacity=len(dictionary))
        for key, value in dictionary.items():
            result[key] = value
        return result

    def __str__(self):
        return dict.__str__(self.to_dict())

    def __repr__(self):
        return dict.__repr__(self.to_dict())

    def __eq__(self, other):
        return dict.__eq__(self.to_dict(), other.to_dict())


class ElementsList(list):

    def __setitem__(self, key, value):
        raise NotImplementedError(
            'can only store elements inside ' +
            'hashtable with open addressing ' +
            f'using HashTable_open_name[{key}] = {value}')


class HashTable_open(HashTable_closed):

    def __init__(self, capacity=30, hashfuncs=['md5', 'sha1']):
        '''
            Usual hashtable using double hashing as method of
            resolving collisions

            load_factor_thr - load factor threshold
            when the size of the hashtable divided by capacity
            reaches this threshold hashtable will resize and rehash
            hashfunc - function used for hashing, may be callable
            or one of the following: poly for polynomial hash,
            md5, sha1

            also uses cuckoo hashing with double hashing
        '''
        # full capacity - capacity of all tables
        self._capacity = gen_prime(capacity)
        # capacity - of one table to be filled with indexes
        # being hashes of one hashfunc
        # number of such tables equals to the number of hashfunctions
        # hence capacity of one table can be calculated by the following:
        self._hashfuncs = hashfuncs
        self._one_table_capacity = self.one_table_capacity()
        # create those tables
        self._elements = ElementsList()
        for _ in hashfuncs:
            self._elements.append([
                    None for _ in range(self.one_table_capacity())])
        self._size = 0

    def one_table_capacity(self):
        return self._capacity // len(self._hashfuncs)

    def get_hashes(self, key):
        for i in self._hashfuncs:
            self._hashfunc = i
            yield super().get_hash(key) % self.one_table_capacity()

    def current_hashed_key(self, key, table_index):
        gen = self.get_hashes(key)
        for index, hashed_key in enumerate(gen):
            if index == table_index:
                return hashed_key

    @property
    def elements(self):
        ret = self._elements.copy()
        return ret

    @elements.setter
    def elements(self, pair):
        raise NotImplementedError('cannot set value to protected property' +
                                  'to append or set value use ' +
                                  'traditional setitem method: ' +
                                  f'{self.__name__}[{pair[0]}] = {pair[1]}')

    def __setitem__(self, key, value):
        # memorize parameter key as starting one
        starting_key = key
        # fix the index of current table if
        # Cuckoo hashing will start to work
        index = 0
        while True:
            # multiple hashing
            for table_index, hashed_key in enumerate(self.get_hashes(key)):
                if self._elements[table_index][hashed_key] is None:
                    self._elements[table_index][hashed_key] = Pair(key, value)
                    self._size += 1
                    logging.debug(
                        f'index: {hashed_key} in table {table_index} busy ' +
                        f'with key: {self._elements[table_index][hashed_key].key}')
                    return
            # Cuckoo hashing
            # (displacing pairs from occupied places to possible free)
            hashed_key = self.current_hashed_key(key, index)
            logging.debug(f'placing key: {key}, value: {value} to ' +
                          f'index: {hashed_key} in table {index}')
            new_key = self._elements[index][hashed_key].key
            new_value = self._elements[index][hashed_key].value
            self._elements[index][hashed_key] = Pair(key, value)
            logging.debug(f'instead of key: {new_key}, value: {new_value}')
            # check if Cuckoo leads to looping
            if new_key == starting_key:
                # if it does - change the table
                # to check other loops for free places
                index += 1
                logging.debug('loop\n')
            # if all tables are busy - increase capacity
            if index == len(self._hashfuncs):
                logging.debug('increase capacity\n')
                super().increase_capacity()
            key = new_key
            value = new_value
            logging.debug(f'new key: {key}, value: {value}\n')

    def update(self, key, value):
        for table_index, hashed_key in enumerate(self.get_hashes(key)):
            if self._elements[table_index][hashed_key] is None:
                raise KeyError('no value for the corresponding key present')
            if self._elements[table_index][hashed_key].key == key:
                self._elements[table_index][hashed_key] = Pair(key, value)
                return

    def __delitem__(self, key):
        table_index, hashed_key = self.search(key)
        logging.debug(
            f'deleting key: {hashed_key} in table: {table_index}' +
            f' with value: {self._elements[table_index][hashed_key]}')
        self._elements[table_index][hashed_key] = None
        self._size -= 1

    def __getitem__(self, key):
        result = self.search(key)
        if result is False:
            raise KeyError('no value for corresponding key found')
        table_index, hashed_key = result
        return self._elements[table_index][hashed_key].value

    def search(self, key):
        for table_index, hashed_key in enumerate(self.get_hashes(key)):
            if self._elements[table_index][hashed_key] is None:
                continue
            if self._elements[table_index][hashed_key].key == key:
                return table_index, hashed_key
        return False

    def recapacitate_and_rehash(self, old_capacity):
        old_elements = self._elements
        self._elements = ElementsList()
        self._size = 0
        for _ in self._hashfuncs:
            self._elements.append([
                    None for _ in range(self.one_table_capacity())])
        old_elements[0].extend(old_elements[1])
        for pair in [pair for pair in old_elements[0] if pair is not None]:
            self[pair[0]] = pair[1]

    def to_dict(self):
        dict_res = dict()
        for pair in [pair for pair in self._elements[0] if pair is not None]:
            dict_res[pair[0]] = pair[1]
        for pair in [pair for pair in self._elements[1] if pair is not None]:
            dict_res[pair[0]] = pair[1]
        return dict_res
