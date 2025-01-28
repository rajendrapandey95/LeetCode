class Solution:
    def calculate_fishes(self, grid, visited, row, col) -> int:
        if (
            row < 0 or row >= len(grid) or
            col < 0 or col >= len(grid[0]) or
            grid[row][col] == 0 or
            visited[row][col]
        ):
            return 0

        visited[row][col] = True
        return grid[row][col] + sum(
            self.calculate_fishes(grid, visited, row + dr, col + dc)
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]
        )

    def findMaxFish(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = [[False] * cols for _ in range(rows)]
        return max(
            self.calculate_fishes(grid, visited, row, col)
            for row in range(rows) for col in range(cols)
            if grid[row][col] > 0 and not visited[row][col]
        )
