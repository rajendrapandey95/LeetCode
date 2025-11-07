class Solution:
    def maxPower(self, st, r, k):
        n = len(st)
        base = [0]*(n+1)

        for i, v in enumerate(st):
            L, R = max(0, i-r), min(n, i+r+1)
            base[L] += v
            base[R] -= v

        def ok(x):
            diff = base[:]
            cur = 0
            rem = k
            for i in range(n):
                cur += diff[i]
                if cur < x:
                    need = x-cur
                    if need > rem: return False
                    rem -= need
                    cur += need
                    j = min(n, i+2*r+1)
                    diff[j] -= need
            return True

        lo, hi = min(st), sum(st)+k
        ans = lo
        while lo <= hi:
            m = (lo+hi)//2
            if ok(m):
                ans = m
                lo = m+1
            else:
                hi = m-1
        return ans
