class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def isMagic(grid, r, c):
            s = set()
            for i in range(3):
                for j in range(3):
                    num = grid[r+i][c+j]
                    if num < 1 or num > 9 or num in s:
                        return False
                    s.add(num)
            return (grid[r][c] + grid[r][c+1] + grid[r][c+2] == 
                    grid[r+1][c] + grid[r+1][c+1] + grid[r+1][c+2] == 
                    grid[r+2][c] + grid[r+2][c+1] + grid[r+2][c+2] == 
                    grid[r][c] + grid[r+1][c] + grid[r+2][c] == 
                    grid[r][c+1] + grid[r+1][c+1] + grid[r+2][c+1] == 
                    grid[r][c+2] + grid[r+1][c+2] + grid[r+2][c+2] == 
                    grid[r][c] + grid[r+1][c+1] + grid[r+2][c+2] == 
                    grid[r+2][c] + grid[r+1][c+1] + grid[r][c+2])
        
        return sum(isMagic(grid, r, c) for r in range(len(grid) - 2) for c in range(len(grid[0]) - 2))
