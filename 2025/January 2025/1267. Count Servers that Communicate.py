class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        row_counts = [sum(row) for row in grid]
        col_counts = [sum(grid[r][c] for r in range(len(grid))) for c in range(len(grid[0]))]

        return sum(1 for r in range(len(grid)) for c in range(len(grid[0])) if grid[r][c] and (row_counts[r] > 1 or col_counts[c] > 1))
