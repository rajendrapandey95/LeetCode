from typing import List

class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7

        powers = []
        p = 1
        while n > 0:
            if n & 1:
                powers.append(p)
            p <<= 1
            n >>= 1

        prefix = [1]
        for val in powers:
            prefix.append((prefix[-1] * val) % MOD)

        ans = []
        for l, r in queries:
            ans.append((prefix[r + 1] * pow(prefix[l], MOD - 2, MOD)) % MOD)
        return ans
