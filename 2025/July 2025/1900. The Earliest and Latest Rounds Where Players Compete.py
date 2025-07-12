from functools import cache

class Solution:
    def earliestAndLatest(self, n: int, f: int, s: int) -> list[int]:
        @cache
        def dp(n: int, f: int, s: int) -> tuple[int, int]:
            if f + s == n + 1: return (1, 1)
            if f + s > n + 1: return dp(n, n + 1 - s, n + 1 - f)

            e, l, nh = float('inf'), float('-inf'), (n + 1) // 2
            if s <= nh:
                for i in range(f):
                    for j in range(s - f):
                        x, y = dp(nh, i + 1, i + j + 2)
                        e, l = min(e, x), max(l, y)
            else:
                sp, mid = n + 1 - s, (n - 2 * (n + 1 - s) + 1) // 2
                for i in range(f):
                    for j in range(sp - f):
                        x, y = dp(nh, i + 1, i + j + mid + 2)
                        e, l = min(e, x), max(l, y)
            return (e + 1, l + 1)

        if f > s: f, s = s, f
        res = dp(n, f, s)
        dp.cache_clear()
        return list(res)
