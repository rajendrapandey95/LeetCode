class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        def cnt(a, b, t): return abs(a-b) + 2*t
        ans = n = s_ = e = w = 0
        for c in s:
            if c == 'N': n += 1
            elif c == 'S': s_ += 1
            elif c == 'E': e += 1
            elif c == 'W': w += 1
            t1 = min(n, s_, k)
            t2 = min(e, w, k - t1)
            ans = max(ans, cnt(n, s_, t1) + cnt(e, w, t2))
        return ans
