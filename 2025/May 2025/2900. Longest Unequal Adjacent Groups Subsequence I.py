class Solution:
    def getLongestSubsequence(self, w, g):
        return [w[0]] + [w[i] for i in range(1, len(g)) if g[i] != g[i-1]]
