import math

class Solution:
    def smallestNumber(self, n: int) -> int:
        k = math.ceil(math.log2(n + 1))
        return (1 << k) - 1
