class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(complexity)

        if any(complexity[i] <= complexity[0] for i in range(1, n)):
            return 0

        ans = 1
        for i in range(2, n):
            ans = ans * i % MOD
        return ans
