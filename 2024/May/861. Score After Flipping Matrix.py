class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        for row in grid:
            if row[0] == 0:
                for i in range(n):
                    row[i] ^= 1
        
        for j in range(1, n):
            count_1 = sum(grid[i][j] for i in range(m))
            if count_1 < m / 2:
                for i in range(m):
                    grid[i][j] ^= 1
        
        score = 0
        for row in grid:
            score += int(''.join(map(str, row)), 2)
        
        return score
