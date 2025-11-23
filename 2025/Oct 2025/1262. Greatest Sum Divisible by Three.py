class Solution:
    def maxSumDivThree(self, a):
        dp=[0,-10**15,-10**15]
        for x in a:
            t=dp[:]
            for r in range(3): t[(r+x)%3]=max(t[(r+x)%3],dp[r]+x)
            dp=t
        return dp[0]
