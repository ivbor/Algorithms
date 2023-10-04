"""
Hash Table Implementations with Open and Closed Addressing
=========================================================

This module provides two hash table implementations: HashTable_closed and
HashTable_open, using closed and open addressing, respectively, for collision
resolution. Both implementations offer methods for adding, retrieving,
and removing key-value pairs.

Classes
-------
HashTable_closed
    A hash table implementation using closed addressing (separate chaining) to
    handle collisions.

HashTable_open
    A hash table implementation using open addressing (multiple and cuckoo
    hashing) to handle collisions with multiple hash functions.

PairsVector
    A specialized vector for storing key-value pairs in hash tables using
    closed addressing.

ElementsList
    A specialized list for storing elements in hash tables using open
    addressing.

Pair
    A named tuple representing a key-value pair.

Functions
---------
gen_primes()
    Generate an infinite sequence of prime numbers for use as hash table
    capacity.

gen_prime(stop=30)
    Generate prime numbers up to a specified stop value.

poly_hash(x)
    Calculate a polynomial hash value for a given input.

"""

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
    """
    A hash table implementation using closed addressing
    for collision resolution.

    This class represents a hash table that uses closed addressing
    (separate chaining) to handle collisions.
    It provides methods for adding, retrieving, and removing key-value pairs.

    Attributes
    ----------
    capacity : int
        The initial capacity of the hash table.

    size : int
        The number of key-value pairs currently stored in the hash table.

    hashfunc : str or callable
        The hashing function family used to determine the index
        for storing keys. Supported values: 'poly' (polynomial hash),
        'md5', 'sha1', or a custom callable function.

    Methods
    -------
    __setitem__(self, key, value) -> None
        Adds a key-value pair to the hash table.

    __getitem__(self, key) -> Any
        Retrieves the value associated with a given key.

    __delitem__(self, key) -> None
        Removes a key-value pair from the hash table.

    to_dict(self) -> dict
        Returns a dictionary representation of the hash table.

    __contains__(self, key) -> bool
        Checks if a key exists in the hash table.

    from_dict(cls, dictionary) -> HashTable_closed
        Creates a new hash table from a dictionary.

    __str__(self) -> str
        Returns a string representation of the hash table.

    __repr__(self) -> str
        Used for printing the contents of the hash table.

    __eq__(self, other) -> bool
        Checks if two hash tables are equal.

    Notes
    -----
    This hash table uses closed addressing to resolve collisions,
    which means that multiple key-value pairs with the same hash value
    are stored in linked lists within the hash table.

    """

    def __init__(self, capacity=30, hashfunc='md5'):
        """
        Initializes a HashTable_closed object with specified capacity
        and hash function.

        Parameters
        ----------
        capacity : int
            The initial capacity of the hash table.

        hashfunc : str or callable
            The hashing function family used to determine the index
            for storing keys. Supported values: 'poly' (polynomial hash),
            'md5', 'sha1', or a custom callable function.

        Returns
        -------
        None
        """
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
        """
        Calculates the hash value for a given key
        using the selected hash function.

        Parameters
        ----------
        x: any
            The key to be hashed.

        Returns
        -------
        int
            The calculated hash value.
        """
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
        """
        Property getter method for retrieving the pairs attribute
        of the hash table.

        Returns
        -------
        list
            A copy of the internal list of pairs in the hash table.
        """
        ret = self._pairs.elements.copy()
        return ret

    @pairs.setter
    def pairs(self, value):
        """
        Setter method for the pairs attribute.
        Raises an error as the pairs attribute is read-only.

        Parameters
        ----------
        value: any
            The value to be set (not used).

        Returns
        -------
        None

        Raises
        ------
            NotImplementedError: Always raised since the pairs attribute is
            read-only.
        """
        if value is not None:
            raise NotImplementedError(
                'cannot set value to protected property' +
                'to append or set value use setitem')

    @property
    def size(self):
        """
        Property getter method for retrieving the size attribute of the
        hash table.

        Returns
        -------
        int
            The number of key-value pairs currently stored in the hash table.
        """
        return self._size

    @size.setter
    def size(self, size):
        """
        Setter method for the size attribute.
        Raises an error as the size attribute is read-only.

        Parameters
        ----------
        size: int
            The value to be set (not used).

        Returns
        -------
        None

        Raises
        ------
            NotImplementedError: Always raised since the size attribute is
            read-only.
        """
        if size is not None:
            raise NotImplementedError(
                'cannot set value to protected property')

    @property
    def capacity(self):
        """
        Property getter method for retrieving the capacity attribute
        of the hash table.

        Returns
        -------
        int
            The current capacity of the hash table.
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        """
        Setter method for the capacity attribute.
        Raises an error as the capacity attribute is read-only.

        Parameters
        ----------
        capacity: int
            The value to be set (not used).

        Returns
        -------
        None

        Raises
        ------
            NotImplementedError: Always raised since the capacity attribute is
            read-only.
        """
        if capacity is not None:
            raise NotImplementedError(
                'cannot set value to protected property')

    def __len__(self):
        """
        Returns the number of key-value pairs currently
        stored in the hash table.

        Returns
        -------
        int
            The size of the hash table.
        """
        return self._size

    def __setitem__(self, key, x):
        """
        Adds or updates (if already taken) a key-value pair to the hash table.

        Parameters
        ----------
        key: any
            The key to be added.
        x: any
            The value associated with the key.
        """
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
        """
        Retrieves the value associated with a given key from the hash table.

        Parameters
        ----------
        i: int
            The key for which to retrieve the value.

        Returns
        -------
        Any
            The value associated with the key.

        Raises
        ------
            KeyError: If the key is not found in the hash table.
        """
        hashed_key = self.get_hash(i)
        for pair in [pair for pair in self._pairs[hashed_key]]:
            key = pair[0]
            value = pair[1]
            if key == i:
                return value
        raise KeyError('no value for corresponding key present')

    def increase_capacity(self):
        """
        Increases the capacity of the hash table.

        Returns
        -------
        None
        """
        # in order to make amortized time to work capacity will be
        # increased to double immediately, instead of + 1 for example
        old_capacity = self._capacity
        self._capacity = gen_prime(self._capacity * 2)
        # this method is used by both open and closed HashTables
        # hence, to use inheritance and do not copy the same function
        # without one parameter in the call in the end to the different
        # class it's better to write just if closure
        if 'closed' in self.__class__.__name__:
            self.recapacitate_and_rehash(old_capacity)
        else:
            self.recapacitate_and_rehash()

    def recapacitate_and_rehash(self, old_capacity):
        """
        Recalculates the hash values and rehashes the key-value pairs.

        Parameters
        ----------
        old_capacity: int
            The previous capacity of the hash table.

        Returns
        -------
        None
        """
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
        """
        Decreases the capacity of the hash table.
        """
        old_capacity = self._capacity
        self._capacity = self._capacity // 2 if self._capacity != 1 else 1
        # this method is used by both open and closed HashTables
        # hence, to use inheritance and do not copy the same function
        # without one parameter in the call in the end to the different
        # class it's better to write just if closure
        if 'closed' in self.__class__.__name__:
            self.recapacitate_and_rehash(old_capacity)
        else:
            self.recapacitate_and_rehash()

    def search(self, key):
        """
        Searches for a key in the hash table and returns the index if found,
        or False if not found.

        Parameters
        ----------
        key: any
            The key to search for.

        Returns
        -------
        int or False
            The index of the key in the hash table if found,
            or False if not found.
        """
        hashed_key = self.get_hash(key)
        for index, pair in enumerate(
                [pair for pair in self._pairs[hashed_key]]):
            key_of_pair = pair[0]
            if key == key_of_pair:
                return index
        return False

    def __delitem__(self, key):
        """
        Removes a key-value pair from the hash table.

        Parameters
        ----------
        key: any
            The key to be removed.

        Returns
        -------
        None
        """
        hashed_key = self.get_hash(key)
        index = self.search(key)
        if str(index) != 'False':
            del self._pairs[hashed_key][index]
            self._size -= 1
            if len(self._pairs[hashed_key]) < 1:
                self.decrease_capacity()

    def to_dict(self):
        """
        Returns a dictionary representation of the hash table.

        Returns
        -------
        dict
            A dictionary containing the key-value pairs from the hash table.
        """
        result = dict()
        for i in self._pairs:
            for j in i:
                result[j.key] = j.value
        return result

    def __contains__(self, key):
        """
        Checks if a key exists in the hash table.

        Parameters
        ----------
        key: any
            The key to check for existence.

        Returns
        -------
        bool
            True if the key exists in the hash table, False otherwise.
        """
        if str(self.search(key)) == 'False':
            return False
        else:
            return True

    @classmethod
    def from_dict(cls, dictionary):
        """
        Creates a new HashTable_closed object from a dictionary.

        Parameters
        ----------
        dictionary: dict
            The dictionary to create the hash table from.

        Returns
        -------
        HashTable_closed
            A new HashTable_closed object initialized with
            the contents of the dictionary.
        """
        result = HashTable_closed(capacity=len(dictionary))
        for key, value in dictionary.items():
            result[key] = value
        return result

    def __str__(self):
        """
        Returns a string representation of the hash table.

        Returns
        -------
        str
            A string representation of the hash table as a dictionary.
        """
        return dict.__str__(self.to_dict())

    def __repr__(self):
        """
        Returns a string representation of the hash table used for printing.

        Returns
        -------
        str
            A string representation of the hash table as a dictionary.
        """
        return dict.__repr__(self.to_dict())

    def __eq__(self, other):
        """
        Checks if two hash tables are equal by comparing their
        dictionary representations.

        Parameters
        ----------
        other: object with defined to_dict method
            Another hash table to compare.

        Returns
        -------
        bool
            True if the hash tables are equal, False otherwise.
        """
        return dict.__eq__(self.to_dict(), other.to_dict())


class ElementsList(list):

    def __setitem__(self, key, value):
        raise NotImplementedError(
            'can only store elements inside ' +
            'hashtable with open addressing ' +
            f'using HashTable_open_name[{key}] = {value}')


class HashTable_open(HashTable_closed):
    """
    A hash table implementation using open addressing
    for collision resolution.

    This class represents a hash table that uses open addressing
    (multiple and cuckoo hashing) to handle collisions.
    It provides methods for adding, retrieving, and removing key-value pairs.

    Attributes
    ----------
    capacity : int
        The initial capacity of the hash table.

    hashfuncs : list of str or callable
        A list of hash functions used to determine the index for storing keys.
        Supported values: 'md5', 'sha1', 'poly' (polynomial hash),
        or custom callable functions.

    Methods
    -------
    __setitem__(self, key, value) -> None
        Adds a key-value pair to the hash table.

    __getitem__(self, key) -> Any
        Retrieves the value associated with a given key.

    __delitem__(self, key) -> None
        Removes a key-value pair from the hash table.

    to_dict(self) -> dict
        Returns a dictionary representation of the hash table.

    update(self, key, value) -> None
        Updates the value associated with a given key in the hash table.

    search(self, key) -> tuple(int, int) or False
        Searches for a key in the hash table and returns
        the table index and hashed key index if found, or False if not found.

    increase_capacity(self) -> None
        Increases the capacity of the hash table.

    decrease_capacity(self) -> None
        Decreases the capacity of the hash table.

    one_table_capacity(self) -> int
        Calculates the capacity of each individual
        hash table within the open addressing scheme.

    get_hashes(self, key) -> generator
        Generates hash values for a key using the specified hash functions.

    current_hashed_key(self, key, table_index) -> int
        Computes the hashed key index for a key based on
        the current table index.

    recapacitate_and_rehash(self) -> None
        Recapacitates and rehashes hashtable.

    Notes
    -----
    This hash table uses open addressing (multiple and cuckoo hashing)
    to resolve collisions, which means that when a collision occurs,
    it looks for alternative positions within the table using multiple
    hash functions.

    Supported hash functions include 'md5', 'sha1', 'poly' (polynomial hash),
    and custom callable functions.

    """

    def __init__(self, capacity=30, hashfuncs=['md5', 'sha1']):
        """
        Initializes a HashTable_open instance with the given capacity
        and hash functions.

        Parameters
        ----------
        capacity : int, optional
            The initial capacity of the hash table, by default 30.

        hashfuncs : list of str or callables, optional
            A list of hash functions used to determine the index
            for storing keys, by default ['md5', 'sha1'].

        Returns
        -------
        None
        """
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
        """
        Calculates the capacity of each individual hash table
        within the open addressing scheme.

        Returns
        -------
        int
            The capacity of one hash table.

        """
        return self._capacity // len(self._hashfuncs)

    def get_hashes(self, key):
        """
        Generates hash values for a key using the specified hash functions.

        Parameters
        ----------
        key : Any
            The key for which hash values are generated.

        Yields
        ------
        int
            A hash value for the key.

        """
        for i in self._hashfuncs:
            self._hashfunc = i
            yield super().get_hash(key) % self.one_table_capacity()

    def current_hashed_key(self, key, table_index):
        """
        Computes the hashed key index for a key based on the
        current table index.

        Parameters
        ----------
        key : Any
            The key for which the hashed key index is computed.

        table_index : int
            The index of the hash table within the open addressing scheme.

        Returns
        -------
        int
            The hashed key index for the key in the specified table.

        """
        gen = self.get_hashes(key)
        for index, hashed_key in enumerate(gen):
            if index == table_index:
                return hashed_key

    @property
    def elements(self):
        """
        Defensive copying of the elements array.

        Returns
        -------
        list
            A copy of the elements array.

        """
        ret = self._elements.copy()
        return ret

    @elements.setter
    def elements(self, pair):
        """
        Setter for the elements property, raises NotImplementedError.

        Parameters
        ----------
        pair : tuple
            The key-value pair to be set.

        Returns
        -------
        None

        Raises
        ------
        NotImplementedError
            Raised when attempting to set the value of the protected property.

        """
        raise NotImplementedError('cannot set value to protected property' +
                                  'to append or set value use ' +
                                  'traditional setitem method: ' +
                                  f'{self.__name__}[{pair[0]}] = {pair[1]}')

    def __setitem__(self, key, value):
        """
        Adds a key-value pair to the hash table.

        Parameters
        ----------
        key : Any
            The key to be added.

        value : Any
            The value associated with the key.

        Returns
        -------
        None

        """
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
                        f'with key:' +
                        f' {self._elements[table_index][hashed_key].key}')
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
        """
        Updates the value associated with a given key in the hash table.

        Parameters
        ----------
        key : Any
            The key for which the value should be updated.

        value : Any
            The new value to associate with the key.

        Returns
        -------
        None

        Raises
        ------
        KeyError
            Raised if no value is present for the corresponding key.

        """
        for table_index, hashed_key in enumerate(self.get_hashes(key)):
            if self._elements[table_index][hashed_key] is None:
                raise KeyError('no value for the corresponding key present')
            if self._elements[table_index][hashed_key].key == key:
                self._elements[table_index][hashed_key] = Pair(key, value)
                return

    def __delitem__(self, key):
        """
        Removes a key-value pair from the hash table.

        Parameters
        ----------
        key : Any
            The key to be removed.

        Returns
        -------
        None

        """
        table_index, hashed_key = self.search(key)
        logging.debug(
            f'deleting key: {hashed_key} in table: {table_index}' +
            f' with value: {self._elements[table_index][hashed_key]}')
        self._elements[table_index][hashed_key] = None
        self._size -= 1

    def __getitem__(self, key):
        """
        Retrieves the value associated with a given key in the hash table.

        Parameters
        ----------
        key : Any
            The key for which the value is retrieved.

        Returns
        -------
        Any
            The value associated with the key.

        Raises
        ------
        KeyError
            Raised if no value is found for the corresponding key.

        """
        result = self.search(key)
        if result is False:
            raise KeyError('no value for corresponding key found')
        table_index, hashed_key = result
        return self._elements[table_index][hashed_key].value

    def search(self, key):
        """
        Searches for a key in the hash table and returns
        the table index and hashed key index if found,
        or False if not found.

        Parameters
        ----------
        key : Any
            The key to be searched for.

        Returns
        -------
        tuple(int, int) or False
            A tuple containing the table index and hashed key index if found,
            or False if the key is not present in the hash table.

        """
        for table_index, hashed_key in enumerate(self.get_hashes(key)):
            if self._elements[table_index][hashed_key] is None:
                continue
            if self._elements[table_index][hashed_key].key == key:
                return table_index, hashed_key
        return False

    def recapacitate_and_rehash(self):
        """
        Recapacitates the hash table and rehashes its contents.

        Parameters
        ----------
        old_capacity : int
            The old capacity of the hash table.

        Returns
        -------
        None

        """
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
        """
        Returns a dictionary representation of the hash table.

        Returns
        -------
        dict
            A dictionary containing key-value pairs from the hash table.

        """
        dict_res = dict()
        for pair in [pair for pair in self._elements[0] if pair is not None]:
            dict_res[pair[0]] = pair[1]
        for pair in [pair for pair in self._elements[1] if pair is not None]:
            dict_res[pair[0]] = pair[1]
        return dict_res
