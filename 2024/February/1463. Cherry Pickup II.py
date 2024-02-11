class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        
        memo = [[[None] * cols for _ in range(cols)] for _ in range(rows)]
        
        def dp(row, col1, col2):
            if row == rows or col1 < 0 or col1 >= cols or col2 < 0 or col2 >= cols:
                return float('-inf')
            if grid[row][col1] == -1 or grid[row][col2] == -1:
                return float('-inf')
            
            if memo[row][col1][col2] is not None:
                return memo[row][col1][col2]
            
            if row == rows - 1:
                return grid[row][col1] + (grid[row][col2] if col1 != col2 else 0)
            
            max_cherries = max(
                dp(row + 1, new_col1, new_col2)
                for new_col1 in range(col1 - 1, col1 + 2)
                for new_col2 in range(col2 - 1, col2 + 2)
            )
            
            if max_cherries != float('-inf'):
                max_cherries += grid[row][col1] + (grid[row][col2] if col1 != col2 else 0)
            
            memo[row][col1][col2] = max_cherries
            return max_cherries
        
        return max(0, dp(0, 0, cols - 1))
