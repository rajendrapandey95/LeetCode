class Solution:
    def countPalindromicSubsequence(self, s):
        f, l = {}, {}
        for i, c in enumerate(s):
            f.setdefault(c, i); l[c] = i
        return sum(len(set(s[f[c]+1:l[c]])) for c in f if l[c] > f[c])
