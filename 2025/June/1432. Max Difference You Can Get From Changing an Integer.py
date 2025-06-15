class Solution:
    def maxDiff(self, num: int) -> int:
        s = str(num)
        lo, hi = num, num
        for x in '0123456789':
            for y in '0123456789':
                r = s.replace(x, y)
                if r[0] != '0':
                    v = int(r)
                    lo = min(lo, v)
                    hi = max(hi, v)
        return hi - lo
