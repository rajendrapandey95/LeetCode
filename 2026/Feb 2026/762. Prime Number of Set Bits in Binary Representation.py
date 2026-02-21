class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        primes = {2, 3, 5, 7, 11, 13, 17, 19}
        return sum(x.bit_count() in primes for x in range(L, R + 1))
