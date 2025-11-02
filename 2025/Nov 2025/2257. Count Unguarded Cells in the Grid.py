class Solution:
    def countUnguarded(self, m, n, guards, walls):
        G, W, X = 2, 3, 1
        grid = [[0]*n for _ in range(m)]

        for r, c in guards: grid[r][c] = G
        for r, c in walls:  grid[r][c] = W

        for r, c in guards:
            i = r-1
            while i>=0 and grid[i][c]!=W and grid[i][c]!=G:
                grid[i][c] = X; i-=1
            i = r+1
            while i<m and grid[i][c]!=W and grid[i][c]!=G:
                grid[i][c] = X; i+=1
            j = c-1
            while j>=0 and grid[r][j]!=W and grid[r][j]!=G:
                grid[r][j] = X; j-=1
            j = c+1
            while j<n and grid[r][j]!=W and grid[r][j]!=G:
                grid[r][j] = X; j+=1

        return sum(grid[i][j]==0 for i in range(m) for j in range(n))
