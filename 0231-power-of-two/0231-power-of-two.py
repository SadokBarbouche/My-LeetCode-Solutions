import math

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        return math.ceil(math.log2(n)) == math.floor(math.log2(n))
