class Solution:
    def maxProductPath(self, g):
        m,n=len(g),len(g[0])
        mx=[[0]*n for _ in range(m)]
        mn=[[0]*n for _ in range(m)]

        mx[0][0]=mn[0][0]=g[0][0]

        for j in range(1,n):
            mx[0][j]=mn[0][j]=mx[0][j-1]*g[0][j]
        for i in range(1,m):
            mx[i][0]=mn[i][0]=mx[i-1][0]*g[i][0]

        for i in range(1,m):
            for j in range(1,n):
                a,b=mx[i-1][j],mx[i][j-1]
                c,d=mn[i-1][j],mn[i][j-1]
                if g[i][j]>=0:
                    mx[i][j]=max(a,b)*g[i][j]
                    mn[i][j]=min(c,d)*g[i][j]
                else:
                    mx[i][j]=min(c,d)*g[i][j]
                    mn[i][j]=max(a,b)*g[i][j]

        return -1 if mx[-1][-1]<0 else mx[-1][-1]%(10**9+7)
