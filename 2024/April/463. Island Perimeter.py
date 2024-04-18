from typing import List

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        rows, cols = len(grid), len(grid[0])

        # Define directions to check neighbors: up, down, left, right
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    neighbors = 0
                    for dx, dy in directions:
                        ni, nj = i + dx, j + dy
                        if ni < 0 or ni >= rows or nj < 0 or nj >= cols or grid[ni][nj] == 0:
                            neighbors += 1
                    perimeter += neighbors

        return perimeter
