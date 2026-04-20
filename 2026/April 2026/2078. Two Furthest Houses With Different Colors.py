class Solution:
    def maxDistance(self, c):
        n = len(c)
        ans = 0

        for i in range(n):
            if c[i] != c[0]:
                ans = max(ans, i)
            if c[i] != c[-1]:
                ans = max(ans, n - 1 - i)

        return ans
