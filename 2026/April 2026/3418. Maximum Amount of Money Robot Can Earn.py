class Solution:
    def maximumAmount(self, g):
        m,n=len(g),len(g[0])
        dp=[[[-10**18]*3 for _ in range(n)] for _ in range(m)]

        dp[0][0][0]=g[0][0]
        for k in range(1,3):
            dp[0][0][k]=max(g[0][0],0)

        for j in range(1,n):
            for k in range(3):
                dp[0][j][k]=dp[0][j-1][k]+g[0][j]
                if k:
                    dp[0][j][k]=max(dp[0][j][k],
                                    dp[0][j-1][k-1]+max(g[0][j],0))

        for i in range(1,m):
            for k in range(3):
                dp[i][0][k]=dp[i-1][0][k]+g[i][0]
                if k:
                    dp[i][0][k]=max(dp[i][0][k],
                                    dp[i-1][0][k-1]+max(g[i][0],0))

        for i in range(1,m):
            for j in range(1,n):
                for k in range(3):
                    dp[i][j][k]=max(dp[i-1][j][k],dp[i][j-1][k])+g[i][j]
                    if k:
                        dp[i][j][k]=max(dp[i][j][k],
                                        max(dp[i-1][j][k-1],
                                            dp[i][j-1][k-1]))

        return dp[-1][-1][2]
