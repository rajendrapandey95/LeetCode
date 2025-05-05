class Solution:
    def numTilings(self, n: int) -> int:
        MOD = 10**9 + 7

        @lru_cache(None)
        def dp(i: int, gap: bool) -> int:
            if i == n:
                return 0 if gap else 1
            if i > n:
                return 0
            if gap:
                return (dp(i + 1, False) + dp(i + 1, True)) % MOD
            return (dp(i + 1, False) + dp(i + 2, False) + 2 * dp(i + 2, True)) % MOD

        return dp(0, False)
