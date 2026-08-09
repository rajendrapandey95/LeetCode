class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        memo = [[0] * n for _ in range(n)]
        suffix_sum = piles[:]

        for i in range(n - 2, -1, -1):
            suffix_sum[i] += suffix_sum[i + 1]

        def max_stones(m, idx):
            if idx + 2 * m >= n:
                return suffix_sum[idx]
            if memo[idx][m] > 0:
                return memo[idx][m]
            res = float('inf')
            for i in range(1, 2 * m + 1):
                res = min(res, max_stones(max(i, m), idx + i))
            memo[idx][m] = suffix_sum[idx] - res
            return memo[idx][m]

        return max_stones(1, 0)
