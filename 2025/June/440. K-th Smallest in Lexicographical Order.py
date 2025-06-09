class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def steps(n, a, b):
            s = 0
            while a <= n:
                s += min(n+1, b) - a
                a, b = a*10, b*10
            return s

        cur = 1
        k -= 1
        while k:
            s = steps(n, cur, cur+1)
            if s <= k:
                cur += 1
                k -= s
            else:
                cur *= 10
                k -= 1
        return cur
