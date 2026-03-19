class Solution:
    def numberOfSubmatrices(self, grid):
        n,m=len(grid),len(grid[0])
        s=[[0]*(m+1) for _ in range(n+1)]
        hasX=[[0]*(m+1) for _ in range(n+1)]
        ans=0

        for i in range(n):
            for j in range(m):
                val = 1 if grid[i][j]=='X' else -1 if grid[i][j]=='Y' else 0
                x   = 1 if grid[i][j]=='X' else 0

                s[i+1][j+1] = s[i+1][j]+s[i][j+1]-s[i][j]+val
                hasX[i+1][j+1] = hasX[i+1][j] or hasX[i][j+1] or x

                if s[i+1][j+1]==0 and hasX[i+1][j+1]:
                    ans+=1

        return ans
