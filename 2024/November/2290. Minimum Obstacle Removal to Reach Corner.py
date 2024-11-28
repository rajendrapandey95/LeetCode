import heapq
from typing import List

class Solution:
    def minimumObstacles(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        m, n = len(grid), len(grid[0])
        min_obstacles = [[float("inf")] * n for _ in range(m)]
        min_obstacles[0][0] = grid[0][0]
        pq = [(min_obstacles[0][0], 0, 0)]
        
        while pq:
            obstacles, row, col = heapq.heappop(pq)
            if row == m - 1 and col == n - 1:
                return obstacles
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                if 0 <= new_row < m and 0 <= new_col < n:
                    new_obstacles = obstacles + grid[new_row][new_col]
                    if new_obstacles < min_obstacles[new_row][new_col]:
                        min_obstacles[new_row][new_col] = new_obstacles
                        heapq.heappush(pq, (new_obstacles, new_row, new_col))
        return -1
