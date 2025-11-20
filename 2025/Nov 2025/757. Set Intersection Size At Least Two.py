class Solution:
    def intersectionSizeTwo(self, intervals):
        intervals.sort(key=lambda x: (x[0], -x[1]))
        need = [2]*len(intervals)
        res = 0
        while intervals:
            (s,e), t = intervals.pop(), need.pop()
            for p in range(s, s+t):
                for i,(s0,e0) in enumerate(intervals):
                    if need[i] and p <= e0:
                        need[i] -= 1
                res += 1
        return res
