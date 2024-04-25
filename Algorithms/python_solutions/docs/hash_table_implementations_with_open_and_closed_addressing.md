# hash_table_implementations_with_open_and_closed_addressing

- **This module provides two hash table implementations**: HashTable_closed and

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

<a id="python_solutions.hashtable.hashlib"></a>

## hashlib

<a id="python_solutions.hashtable.logging"></a>

## logging

<a id="python_solutions.hashtable.deque"></a>

## deque

<a id="python_solutions.hashtable.Any"></a>

## Any

<a id="python_solutions.hashtable.NamedTuple"></a>

## NamedTuple

<a id="python_solutions.hashtable.Vector"></a>

## Vector

<a id="python_solutions.hashtable.Pair"></a>

## Pair Objects

```python
class Pair(NamedTuple)
```

<a id="python_solutions.hashtable.Pair.key"></a>

#### key

<a id="python_solutions.hashtable.Pair.value"></a>

#### value

<a id="python_solutions.hashtable.gen_primes"></a>

#### gen\_primes

```python
def gen_primes()
```

Generate an infinite sequence of prime numbers.

<a id="python_solutions.hashtable.gen_prime"></a>

#### gen\_prime

```python
def gen_prime(stop=30)
```

<a id="python_solutions.hashtable.poly_hash"></a>

#### poly\_hash

```python
def poly_hash(x)
```

<a id="python_solutions.hashtable.simple_hash"></a>

#### simple\_hash

```python
def simple_hash(x)
```

<a id="python_solutions.hashtable.PairsVector"></a>

## PairsVector Objects

```python
class PairsVector(Vector)
```

<a id="python_solutions.hashtable.PairsVector.__setitem__"></a>

#### \_\_setitem\_\_

```python
def __setitem__(key, value)
```

<a id="python_solutions.hashtable.HashTable_closed"></a>

## HashTable\_closed Objects

```python
class HashTable_closed()
```

A hash table implementation using closed addressing
for collision resolution.

This class represents a hash table that uses closed addressing
(separate chaining) to handle collisions.
It provides methods for adding, retrieving, and removing key-value pairs.

## Attributes
- **capacity**: int

    The initial capacity of the hash table.

- **size**: int

    The number of key-value pairs currently stored in the hash table.

- **hashfunc**: str or callable

    The hashing function family used to determine the index
    for storing keys. Supported values: 'poly' (polynomial hash),
    'md5', 'sha1', or a custom callable function.

## Methods

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

## Notes

This hash table uses closed addressing to resolve collisions,
which means that multiple key-value pairs with the same hash value
are stored in linked lists within the hash table.

<a id="python_solutions.hashtable.HashTable_closed.__init__"></a>

#### \_\_init\_\_

```python
def __init__(capacity=30, hashfunc=simple_hash, load_factor_threshold=0.75)
```

Initializes a HashTable_closed object with specified capacity
and hash function.

## Parameters
- **capacity**: int

    The initial capacity of the hash table.

- **hashfunc**: str or callable

    The hashing function family used to determine the index
    for storing keys. Supported values: 'poly' (polynomial hash),
    'md5', 'sha1', or a custom callable function.

- **load_factor_threshold**: float

    The maximum size / capacity ratio. When the actual value
    excesses this factor - the hashtable increases its size.
    When the actual value < this / 4 - the hashtable decreases its
    size. Can be set to any between 0 and 1, but is recommended to be
    set around 0.7 - 0.9.

## Returns

None

<a id="python_solutions.hashtable.HashTable_closed.get_hash"></a>

#### get\_hash

```python
def get_hash(x)
```

Calculates the hash value for a given key
using the selected hash function.

## Parameters
- **x**: any

    The key to be hashed.

## Returns

int
    The calculated hash value.

<a id="python_solutions.hashtable.HashTable_closed.pairs"></a>

#### pairs

```python
@property
def pairs()
```

Property getter method for retrieving the pairs attribute
of the hash table.

## Returns

list
    A copy of the internal list of pairs in the hash table.

<a id="python_solutions.hashtable.HashTable_closed.pairs"></a>

#### pairs

```python
@pairs.setter
def pairs(value)
```

Setter method for the pairs attribute.
Raises an error as the pairs attribute is read-only.

## Parameters
- **value**: any

    The value to be set (not used).

## Returns

None

## Raises
- **NotImplementedError**: Always raised since the pairs attribute is

    read-only.

<a id="python_solutions.hashtable.HashTable_closed.size"></a>

#### size

```python
@property
def size()
```

Property getter method for retrieving the size attribute of the
hash table.

## Returns

int
    The number of key-value pairs currently stored in the hash table.

<a id="python_solutions.hashtable.HashTable_closed.size"></a>

#### size

```python
@size.setter
def size(size)
```

Setter method for the size attribute.
Raises an error as the size attribute is read-only.

## Parameters
- **size**: int

    The value to be set (not used).

## Returns

None

## Raises
- **NotImplementedError**: Always raised since the size attribute is

    read-only.

<a id="python_solutions.hashtable.HashTable_closed.capacity"></a>

#### capacity

```python
@property
def capacity()
```

Property getter method for retrieving the capacity attribute
of the hash table.

## Returns

int
    The current capacity of the hash table.

<a id="python_solutions.hashtable.HashTable_closed.capacity"></a>

#### capacity

```python
@capacity.setter
def capacity(capacity)
```

Setter method for the capacity attribute.
Raises an error as the capacity attribute is read-only.

## Parameters
- **capacity**: int

    The value to be set (not used).

## Returns

None

## Raises
- **NotImplementedError**: Always raised since the capacity attribute is

    read-only.

<a id="python_solutions.hashtable.HashTable_closed.__len__"></a>

#### \_\_len\_\_

```python
def __len__()
```

Returns the number of key-value pairs currently
stored in the hash table.

## Returns

int
    The size of the hash table.

<a id="python_solutions.hashtable.HashTable_closed.__setitem__"></a>

#### \_\_setitem\_\_

```python
def __setitem__(key, x)
```

Adds or updates (if already taken) a key-value pair to the hash table.

## Parameters
- **key**: any

    The key to be added.
- **x**: any

    The value associated with the key.

<a id="python_solutions.hashtable.HashTable_closed.__getitem__"></a>

#### \_\_getitem\_\_

```python
def __getitem__(i)
```

Retrieves the value associated with a given key from the hash table.

## Parameters
- **i**: int

    The key for which to retrieve the value.

## Returns

Any
    The value associated with the key.

## Raises
- **KeyError**: If the key is not found in the hash table.


<a id="python_solutions.hashtable.HashTable_closed.increase_capacity"></a>

#### increase\_capacity

```python
def increase_capacity()
```

Increases the capacity of the hash table.

## Returns

None

<a id="python_solutions.hashtable.HashTable_closed.recapacitate_and_rehash"></a>

#### recapacitate\_and\_rehash

```python
def recapacitate_and_rehash(old_capacity)
```

Recalculates the hash values and rehashes the key-value pairs.

## Parameters
- **old_capacity**: int

    The previous capacity of the hash table.

## Returns

None

<a id="python_solutions.hashtable.HashTable_closed.decrease_capacity"></a>

#### decrease\_capacity

```python
def decrease_capacity()
```

Decreases the capacity of the hash table.

<a id="python_solutions.hashtable.HashTable_closed.search"></a>

#### search

```python
def search(key)
```

Searches for a key in the hash table and returns the index if found,
or False if not found.

## Parameters
- **key**: any

    The key to search for.

## Returns

int or False
    The index of the key in the hash table if found,
    or False if not found.

<a id="python_solutions.hashtable.HashTable_closed.__delitem__"></a>

#### \_\_delitem\_\_

```python
def __delitem__(key)
```

Removes a key-value pair from the hash table.

## Parameters
- **key**: any

    The key to be removed.

## Returns

None

<a id="python_solutions.hashtable.HashTable_closed.to_dict"></a>

#### to\_dict

```python
def to_dict()
```

Returns a dictionary representation of the hash table.

## Returns

dict
    A dictionary containing the key-value pairs from the hash table.

<a id="python_solutions.hashtable.HashTable_closed.__contains__"></a>

#### \_\_contains\_\_

```python
def __contains__(key)
```

Checks if a key exists in the hash table.

## Parameters
- **key**: any

    The key to check for existence.

## Returns

bool
    True if the key exists in the hash table, False otherwise.

<a id="python_solutions.hashtable.HashTable_closed.from_dict"></a>

#### from\_dict

```python
@classmethod
def from_dict(cls, dictionary)
```

Creates a new HashTable_closed object from a dictionary.

## Parameters
- **dictionary**: dict

    The dictionary to create the hash table from.

## Returns

HashTable_closed
    A new HashTable_closed object initialized with
    the contents of the dictionary.

<a id="python_solutions.hashtable.HashTable_closed.__str__"></a>

#### \_\_str\_\_

```python
def __str__()
```

Returns a string representation of the hash table.

## Returns

str
    A string representation of the hash table as a dictionary.

<a id="python_solutions.hashtable.HashTable_closed.__repr__"></a>

#### \_\_repr\_\_

```python
def __repr__()
```

Returns a string representation of the hash table used for printing.

## Returns

str
    A string representation of the hash table as a dictionary.

<a id="python_solutions.hashtable.HashTable_closed.__eq__"></a>

#### \_\_eq\_\_

```python
def __eq__(other)
```

Checks if two hash tables are equal by comparing their
dictionary representations.

## Parameters
- **other**: object with defined to_dict method

    Another hash table to compare.

## Returns

bool
    True if the hash tables are equal, False otherwise.

<a id="python_solutions.hashtable.ElementsList"></a>

## ElementsList Objects

```python
class ElementsList(list)
```

<a id="python_solutions.hashtable.ElementsList.__setitem__"></a>

#### \_\_setitem\_\_

```python
def __setitem__(key, value)
```

<a id="python_solutions.hashtable.HashTable_open"></a>

## HashTable\_open Objects

```python
class HashTable_open(HashTable_closed)
```

A hash table implementation using open addressing
for collision resolution.

This class represents a hash table that uses open addressing
(multiple and cuckoo hashing) to handle collisions.
It provides methods for adding, retrieving, and removing key-value pairs.

## Attributes
- **capacity**: int

    The initial capacity of the hash table.

- **hashfuncs**: list of str or callable

    A list of hash functions used to determine the index for storing keys.
- **Supported values**: 'md5', 'sha1', 'poly' (polynomial hash),

    or custom callable functions.

## Methods

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

## Notes

This hash table uses open addressing (multiple and cuckoo hashing)
to resolve collisions, which means that when a collision occurs,
it looks for alternative positions within the table using multiple
hash functions.

Supported hash functions include 'md5', 'sha1', 'poly' (polynomial hash),
and custom callable functions.

<a id="python_solutions.hashtable.HashTable_open.__init__"></a>

#### \_\_init\_\_

```python
def __init__(capacity=30, hashfuncs=[hash, simple_hash], max_displasements=16)
```

Initializes a HashTable_open instance with the given capacity
and hash functions.

## Parameters
- **capacity**: int, optional

    The initial capacity of the hash table, by default 30.

- **hashfuncs**: list of str or callables, optional

    A list of hash functions used to determine the index
    for storing keys, by default ['md5', 'sha1'].

## Returns

None

<a id="python_solutions.hashtable.HashTable_open.one_table_capacity"></a>

#### one\_table\_capacity

```python
def one_table_capacity()
```

Calculates the capacity of each individual hash table
within the open addressing scheme.

## Returns

int
    The capacity of one hash table.

<a id="python_solutions.hashtable.HashTable_open.get_hashes"></a>

#### get\_hashes

```python
def get_hashes(key)
```

Generates hash values for a key using the specified hash functions.

## Parameters
- **key**: Any

    The key for which hash values are generated.

Yields
------
int
    A hash value for the key.

<a id="python_solutions.hashtable.HashTable_open.current_hashed_key"></a>

#### current\_hashed\_key

```python
def current_hashed_key(key, table_index)
```

Computes the hashed key index for a key based on the
current table index.

## Parameters
- **key**: Any

    The key for which the hashed key index is computed.

- **table_index**: int

    The index of the hash table within the open addressing scheme.

## Returns

int
    The hashed key index for the key in the specified table.

<a id="python_solutions.hashtable.HashTable_open.elements"></a>

#### elements

```python
@property
def elements()
```

Defensive copying of the elements array.

## Returns

list
    A copy of the elements array.

<a id="python_solutions.hashtable.HashTable_open.__setitem__"></a>

#### \_\_setitem\_\_

```python
def __setitem__(key, value)
```

Adds a key-value pair to the hash table.

## Parameters
- **key**: Any

    The key to be added.

- **value**: Any

    The value associated with the key.

## Returns

None

<a id="python_solutions.hashtable.HashTable_open.update"></a>

#### update

```python
def update(key, value)
```

Updates the value associated with a given key in the hash table.

## Parameters
- **key**: Any

    The key for which the value should be updated.

- **value**: Any

    The new value to associate with the key.

## Returns

None

## Raises

KeyError
    Raised if no value is present for the corresponding key.

<a id="python_solutions.hashtable.HashTable_open.__delitem__"></a>

#### \_\_delitem\_\_

```python
def __delitem__(key)
```

Removes a key-value pair from the hash table.

## Parameters
- **key**: Any

    The key to be removed.

## Returns

None

<a id="python_solutions.hashtable.HashTable_open.__getitem__"></a>

#### \_\_getitem\_\_

```python
def __getitem__(key)
```

Retrieves the value associated with a given key in the hash table.

## Parameters
- **key**: Any

    The key for which the value is retrieved.

## Returns

Any
    The value associated with the key.

## Raises

KeyError
    Raised if no value is found for the corresponding key.

<a id="python_solutions.hashtable.HashTable_open.search"></a>

#### search

```python
def search(key)
```

Searches for a key in the hash table and returns
the table index and hashed key index if found,
or False if not found.

## Parameters
- **key**: Any

    The key to be searched for.

## Returns

tuple(int, int) or False
    A tuple containing the table index and hashed key index if found,
    or False if the key is not present in the hash table.

<a id="python_solutions.hashtable.HashTable_open.recapacitate_and_rehash"></a>

#### recapacitate\_and\_rehash

```python
def recapacitate_and_rehash()
```

Recapacitates the hash table and rehashes its contents.

## Parameters
- **old_capacity**: int

    The old capacity of the hash table.

## Returns

None

<a id="python_solutions.hashtable.HashTable_open.to_dict"></a>

#### to\_dict

```python
def to_dict()
```

Returns a dictionary representation of the hash table.

## Returns

dict
    A dictionary containing key-value pairs from the hash table.