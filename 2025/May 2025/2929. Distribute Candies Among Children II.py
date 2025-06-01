class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        def C2(x):
            return x * (x - 1) // 2 if x >= 0 else 0

        L = limit + 1
        return C2(n + 2) - 3 * C2(n - L + 1) + 3 * C2(n - 2 * L + 2) - C2(n - 3 * L + 2)
