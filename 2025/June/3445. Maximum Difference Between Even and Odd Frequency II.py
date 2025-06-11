class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        def status(a, b): return ((a & 1) << 1) | (b & 1)

        n, ans = len(s), float('-inf')
        for a in "01234":
            for b in "01234":
                if a == b: continue
                best = [float('inf')] * 4
                ca = cb = pa = pb = 0
                l = -1
                for r in range(n):
                    ca += s[r] == a
                    cb += s[r] == b
                    while r - l >= k and cb - pb >= 2:
                        best[status(pa, pb)] = min(best[status(pa, pb)], pa - pb)
                        l += 1
                        pa += s[l] == a
                        pb += s[l] == b
                    st = status(ca, cb)
                    if best[st ^ 2] < float('inf'):
                        ans = max(ans, ca - cb - best[st ^ 2])
        return ans
