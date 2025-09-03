import bisect

class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        pts = sorted(points, key=lambda x: (x[0], -x[1]))
        n, ans = len(pts), 0
        for i in range(n):
            yi, between = pts[i][1], []
            for j in range(i+1, n):
                yj = pts[j][1]
                if yj <= yi:
                    lo = bisect.bisect_left(between, yj)
                    hi = bisect.bisect_right(between, yi)
                    if lo == hi: 
                        ans += 1
                bisect.insort(between, yj)
        return ans
