class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        if n == 0:
            return 0

        leftmost_set_bit = 0
        while (1 << leftmost_set_bit) <= n:
            leftmost_set_bit += 1
        leftmost_set_bit -= 1

        if n == (1 << leftmost_set_bit):
            return 2 ** (leftmost_set_bit + 1) - 1

        return 2 ** leftmost_set_bit + self.minimumOneBitOperations((1 << leftmost_set_bit) ^ n ^ (1 << (leftmost_set_bit - 1)))
