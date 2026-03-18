class Solution:
    def countSubmatrices(self, grid, k):
        n,m=len(grid),len(grid[0])
        cols=[0]*m
        res=0

        for i in range(n):
            s=0
            for j in range(m):
                cols[j]+=grid[i][j]
                s+=cols[j]
                if s<=k:
                    res+=1

        return res
