class Solution:
    def minMaxDifference(self, num: int) -> int:
        s, t = str(num), str(num)
        for c in s:
            if c != '9':
                s = s.replace(c, '9')
                break
        t = t.replace(t[0], '0')
        return int(s) - int(t)
