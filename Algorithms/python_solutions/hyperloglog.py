import math
import hashlib
import array


class HyperLogLog:

    def __init__(self, precision=14):
        self.precision = precision
        self.num_buckets = 2 ** precision
        self.buckets = array.array('H', [0] * self.num_buckets)

    def _hash(self, element):
        # Use a hash function to convert the element to a binary string
        # hash_value = hash(element)
        hash_value = int(hashlib.sha256(element.encode()).hexdigest(), 16)
        return bin(hash_value & ((1 << 64) - 1))[2:]

    def _leading_zeros(self, binary_string):
        # Count the number of leading zeros in the binary string
        count = 0
        binary_value = int(binary_string, 2)
        while binary_value:
            binary_value >>= 1
            count += 1
        return count

    def add(self, element):
        hash_value = self._hash(element)
        index = int(hash_value[-self.precision:], 2)
        leading_zeros = self._leading_zeros(hash_value)
        self.buckets[index] = max(self.buckets[index], leading_zeros + 1)

    def count(self):
        alpha = 0.7213 / (1 + 1.079 / self.num_buckets)
        estimate = alpha * (self.num_buckets ** 2) / sum(
            2 ** -bucket for bucket in self.buckets)
        if estimate <= 2.5 * self.num_buckets:
            # Small range correction
            zeros = self.buckets.count(0)
            if zeros != 0:
                return round(self.num_buckets * math.log(
                    self.num_buckets / zeros))
            else:
                return round(estimate)
        elif estimate > 2 ** 32 / 30:
            # Large range correction
            return round(-(2 ** 32) * math.log(1 - estimate / (2 ** 32)))
        else:
            # No correction needed
            return round(estimate)
