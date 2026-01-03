class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10**9 + 7
        x = y = 6

        for _ in range(2, n + 1):
            x, y = (3*x + 2*y) % MOD, (2*x + 2*y) % MOD

        return (x + y) % MOD
