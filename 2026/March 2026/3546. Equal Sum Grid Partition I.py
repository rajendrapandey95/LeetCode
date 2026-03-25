class Solution:
    def canPartitionGrid(self, g):
        m,n=len(g),len(g[0])
        tot=sum(map(sum,g))
        if tot&1: return False

        t=tot//2
        s=0

        for i in range(m-1):
            s+=sum(g[i])
            if s==t: return True

        col=[sum(g[i][j] for i in range(m)) for j in range(n)]
        s=0
        for j in range(n-1):
            s+=col[j]
            if s==t: return True

        return False
