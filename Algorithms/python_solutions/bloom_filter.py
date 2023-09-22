import math
import mmh3
from bitarray import bitarray


# Need to constrain U32 to only 32 bits using the & 0xffffffff
# since Python has no native notion of integers limited to 32 bit
# http://docs.python.org/library/stdtypes.html#numeric-types-int-float-long-complex

'''
    Original copyright notice:
    By Bob Jenkins, 1996.  bob_jenkins@burtleburtle.net.  You may use this
    code any way you wish, private, educational, or commercial.  Its free.
    Python implementation source:
    https://stackoverflow.com/questions/
    3279615/python-implementation-of-jenkins-hash
'''


def rot(x, k):
    return (((x) << (k)) | ((x) >> (32-(k))))


def mix(a, b, c):
    a &= 0xffffffff
    b &= 0xffffffff
    c &= 0xffffffff
    a -= c
    a &= 0xffffffff
    a ^= rot(c, 4)
    a &= 0xffffffff
    c += b
    c &= 0xffffffff
    b -= a
    b &= 0xffffffff
    b ^= rot(a, 6)
    b &= 0xffffffff
    a += c
    a &= 0xffffffff
    c -= b
    c &= 0xffffffff
    c ^= rot(b, 8)
    c &= 0xffffffff
    b += a
    b &= 0xffffffff
    a -= c
    a &= 0xffffffff
    a ^= rot(c, 16)
    a &= 0xffffffff
    c += b
    c &= 0xffffffff
    b -= a
    b &= 0xffffffff
    b ^= rot(a, 19)
    b &= 0xffffffff
    a += c
    a &= 0xffffffff
    c -= b
    c &= 0xffffffff
    c ^= rot(b, 4)
    c &= 0xffffffff
    b += a
    b &= 0xffffffff
    return a, b, c


def final(a, b, c):
    a &= 0xffffffff
    b &= 0xffffffff
    c &= 0xffffffff
    c ^= b
    c &= 0xffffffff
    c -= rot(b, 14)
    c &= 0xffffffff
    a ^= c
    a &= 0xffffffff
    a -= rot(c, 11)
    a &= 0xffffffff
    b ^= a
    b &= 0xffffffff
    b -= rot(a, 25)
    b &= 0xffffffff
    c ^= b
    c &= 0xffffffff
    c -= rot(b, 16)
    c &= 0xffffffff
    a ^= c
    a &= 0xffffffff
    a -= rot(c, 4)
    a &= 0xffffffff
    b ^= a
    b &= 0xffffffff
    b -= rot(a, 14)
    b &= 0xffffffff
    c ^= b
    c &= 0xffffffff
    c -= rot(b, 24)
    c &= 0xffffffff
    return a, b, c


def hashlittle2(data, initval=0, initval2=0):
    length = lenpos = len(data)

    a = b = c = (0xdeadbeef + (length) + initval)

    c += initval2
    c &= 0xffffffff

    p = 0  # string offset
    while lenpos > 12:
        a += (ord(data[p+0]) + (ord(data[p+1]) <<
              8) + (ord(data[p+2]) << 16) + (ord(data[p+3]) << 24))
        a &= 0xffffffff
        b += (ord(data[p+4]) + (ord(data[p+5]) <<
              8) + (ord(data[p+6]) << 16) + (ord(data[p+7]) << 24))
        b &= 0xffffffff
        c += (ord(data[p + 8]) + (ord(data[p + 9]) << 8) +
              (ord(data[p + 10]) << 16) + (ord(data[p + 11]) << 24))
        c &= 0xffffffff
        a, b, c = mix(a, b, c)
        p += 12
        lenpos -= 12

    if lenpos == 12:
        c += (ord(data[p + 8]) + (ord(data[p + 9]) << 8) +
              (ord(data[p + 10]) << 16) + (ord(data[p + 11]) << 24))
        b += (ord(data[p+4]) + (ord(data[p+5]) <<
              8) + (ord(data[p+6]) << 16) + (ord(data[p+7]) << 24))
        a += (ord(data[p+0]) + (ord(data[p+1]) <<
              8) + (ord(data[p+2]) << 16) + (ord(data[p+3]) << 24))
    if lenpos == 11:
        c += (ord(data[p+8]) + (ord(data[p+9]) << 8) + (ord(data[p+10]) << 16))
        b += (ord(data[p+4]) + (ord(data[p+5]) <<
              8) + (ord(data[p+6]) << 16) + (ord(data[p+7]) << 24))
        a += (ord(data[p+0]) + (ord(data[p+1]) <<
              8) + (ord(data[p+2]) << 16) + (ord(data[p+3]) << 24))
    if lenpos == 10:
        c += (ord(data[p+8]) + (ord(data[p+9]) << 8))
        b += (ord(data[p+4]) + (ord(data[p+5]) <<
              8) + (ord(data[p+6]) << 16) + (ord(data[p+7]) << 24))
        a += (ord(data[p+0]) + (ord(data[p+1]) <<
              8) + (ord(data[p+2]) << 16) + (ord(data[p+3]) << 24))
    if lenpos == 9:
        c += (ord(data[p+8]))
        b += (ord(data[p+4]) + (ord(data[p+5]) <<
              8) + (ord(data[p+6]) << 16) + (ord(data[p+7]) << 24))
        a += (ord(data[p+0]) + (ord(data[p+1]) <<
              8) + (ord(data[p+2]) << 16) + (ord(data[p+3]) << 24))
    if lenpos == 8:
        b += (ord(data[p+4]) + (ord(data[p+5]) <<
              8) + (ord(data[p+6]) << 16) + (ord(data[p+7]) << 24))
        a += (ord(data[p+0]) + (ord(data[p+1]) <<
              8) + (ord(data[p+2]) << 16) + (ord(data[p+3]) << 24))
    if lenpos == 7:
        b += (ord(data[p+4]) + (ord(data[p+5]) << 8) + (ord(data[p+6]) << 16))
        a += (ord(data[p+0]) + (ord(data[p+1]) <<
              8) + (ord(data[p+2]) << 16) + (ord(data[p+3]) << 24))
    if lenpos == 6:
        b += ((ord(data[p+5]) << 8) + ord(data[p+4]))
        a += (ord(data[p+0]) + (ord(data[p+1]) <<
              8) + (ord(data[p+2]) << 16) + (ord(data[p+3]) << 24))
    if lenpos == 5:
        b += (ord(data[p+4]))
        a += (ord(data[p+0]) + (ord(data[p+1]) <<
              8) + (ord(data[p+2]) << 16) + (ord(data[p+3]) << 24))
    if lenpos == 4:
        a += (ord(data[p+0]) + (ord(data[p+1]) <<
              8) + (ord(data[p+2]) << 16) + (ord(data[p+3]) << 24))
    if lenpos == 3:
        a += (ord(data[p+0]) + (ord(data[p+1]) << 8) + (ord(data[p+2]) << 16))
    if lenpos == 2:
        a += (ord(data[p+0]) + (ord(data[p+1]) << 8))
    if lenpos == 1:
        a += ord(data[p+0])
    a &= 0xffffffff
    b &= 0xffffffff
    c &= 0xffffffff
    if lenpos == 0:
        return c

    a, b, c = final(a, b, c)

    return c


def hashlittle(data, initval=0):
    '''
        This function calculates Jenkins hash of data using initval as seed.

        It utilises rot(), mix(), final(), hashlittle() functions to
        calculate Jenkins hash as a python translation of the author's
        original C++ algorithm.

        Parameters
        ----------
        data: any
            Object of class with defined __getitem__ method consisting
            of characters (which could be passed to ord() function)
        initval: int
            Seed for calculating hash
            Default value = 0

        Returns
        -------
        int
            Jenkins hash of data
    '''

    c = hashlittle2(data, initval, 0)
    return c


class Bloom_filter():

    '''
        This is an implementation of the Bloom filter data structure.

        Bloom filter is used to determine whether passed object has
        already been passed to it. It has a false positive outcome
        probability which depends on the expected items count to be passed
        and amount of hash functions available.
        This particular implementation requires expected false positives
        probability and items to be passed count and determines its size
        and creates all hash functions on its own provided the algorithm
        for function family.

        Attributes
        ----------
        fp_prob: float
            False positives probability.
            Default value = 0.05
        size: int
            Real size of the structure, is calculated automatically
        hash_count: int
            Amount of hashes needed to redeem fp_prob given items_count,
            is calculated automatically provided with hashfunc family
        bit_array: bitarray
            Special structure imported from bitarray module, allows usage
            of only one byte per bucket, compared to unlimited memory for
            integer values inside lists, hence taking much less memory.
            Consists of either 0's or 1's and has a size of self.size.
            It is the main storage and the filter itself.
            Cannot be modified directly, modifies itself when new values
            passes through filter.
        hashfunc: string
            Family of algorithms for generating hash functions.
            Default value = 'mmh3' (murmur3 hash), possible value = 'jenkins'
            for Jenkins hash

        Methods
        -------
        __init__(self, items_count: int = 1000000,
            fp_prob: float = 0.05, hashfunc: string = 'mmh3') -> None
            Creates an instance of Bloom filter.

        add(self, item: any) -> None
            Passes through the Bloom filter given item.

        check(self, item: any) -> Bloom_filter
            Checks whether the item was passed through Bloom filter.

        get_size(self, items_count: int, fp_prob: float) -> int
            Calculates full size of the Bloom filter.

        get_hash_count(self, size: int, items_count: int) -> int:
            Calculates the necessary amount of hash functions to ensure
            false positives probability with expected
            items to be passed count.

    '''

    def __init__(
            self, items_count=1000000, fp_prob=0.05, hashfunc='mmh3'):
        '''
            Creates an instance of Bloom filter

            Parameters
            ----------
            items_count: int
                Expected amount of items to be passed through filter.
                Default value = 1000000
            fp_prob: float
                Expected false positive outcome probability.
                Default value = 0.05
            hashfunc: 'mmh3' or 'jenkins'
                Name of the family of functions to use for hash functions
                generation.
                Default value = 'mmh3'

            Returns
            -------
            None

        '''
        self.fp_prob = fp_prob
        self.size = self.get_size(items_count, fp_prob)
        self.hash_count = self.get_hash_count(self.size, items_count)
        self.bit_array = bitarray(self.size)
        self.bit_array.setall(0)
        if hashfunc == 'mmh3':
            self.hashfunc = mmh3.hash
        elif hashfunc == 'jenkins':
            self.hashfunc = hashlittle
        else:
            raise ValueError(
                'available are only murmur (mmh3) and jenkins hashes')

    def add(self, item):
        '''
            Passes given item through Bloom filter.

            Parameters
            ----------
            self: Bloom_filter
            item: str or byte-like

            Returns
            -------
            None
        '''
        for i in range(self.hash_count):
            hashed_index = self.hashfunc(str(item), i) % self.size
            self.bit_array[hashed_index] = 1

    def check(self, item):
        '''
            Checks whether the item was passed through the Bloom filter.

            Parameters
            ----------
            self: Bloom_filter
            item: str or byte-like

            Returns
            -------
            bool
                True if the item was passed through, False if it was not.
        '''
        for i in range(self.hash_count):
            hashed_index = self.hashfunc(str(item), i) % self.size
            if self.bit_array[hashed_index] == 0:
                return False
        return True

    def get_size(self, items_count, fp_prob):
        '''
            Calculates the size of bloom filter for its initialization.

            Parameters
            ----------
            self: Bloom_filter
            items_count: int
                Amount of items expected to be passed through.
            fp_prob: float
                False positive case probability

            Returns
            -------
            int
                Size of the bloom filter.
        '''
        m = - (items_count * math.log(fp_prob)) / (math.log(2) ** 2)
        return int(m)

    def get_hash_count(self, size, items_count):
        '''
            Calculates amount of hash functions necessary to assure
            required false probability.

            Parameters
            ----------
            self: Bloom_filter
            size: int
                Calculated size of the bloom filter.
            items_count: int
                Amount of items expected to be passed through the filter.

            Returns
            -------
            int
                Amount of hash functions to generate different hashes.
        '''
        k = (size / items_count) * math.log(2)
        return int(k)
