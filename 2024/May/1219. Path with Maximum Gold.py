class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        def dfs(x, y, visited):
            if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] == 0 or (x, y) in visited:
                return 0
            
            visited.add((x, y))
            
            max_gold = 0
            for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                max_gold = max(max_gold, dfs(x + dx, y + dy, visited))
            
            visited.remove((x, y))
            
            return grid[x][y] + max_gold
        
        max_gold = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0:
                    max_gold = max(max_gold, dfs(i, j, set()))
        
        return max_gold
