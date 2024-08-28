from collections import deque
from typing import List

class Solution:
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def is_sub_island(self, x, y, grid1, grid2, visited):
        rows, cols = len(grid2), len(grid2[0])
        is_sub = True
        queue = deque([(x, y)])
        visited[x][y] = True

        while queue:
            cx, cy = queue.popleft()
            if grid1[cx][cy] == 0:
                is_sub = False

            for dx, dy in self.directions:
                nx, ny = cx + dx, cy + dy
                if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny] and grid2[nx][ny] == 1:
                    queue.append((nx, ny))
                    visited[nx][ny] = True

        return is_sub

    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        rows, cols = len(grid2), len(grid2[0])
        visited = [[False] * cols for _ in range(rows)]
        count = 0

        for x in range(rows):
            for y in range(cols):
                if grid2[x][y] == 1 and not visited[x][y] and self.is_sub_island(x, y, grid1, grid2, visited):
                    count += 1

        return count
