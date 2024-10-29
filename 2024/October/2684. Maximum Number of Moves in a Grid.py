from collections import deque
from typing import List

class Solution:
    dirs = [-1, 0, 1]

    def maxMoves(self, grid: List[List[int]]) -> int:
        M, N = len(grid), len(grid[0])
        q = deque()
        vis = [[False] * N for _ in range(M)]

        for i in range(M):
            vis[i][0] = True
            q.append((i, 0, 0))

        max_moves = 0
        while q:
            row, col, count = q.popleft()
            max_moves = max(max_moves, count)

            for dir in self.dirs:
                new_row, new_col = row + dir, col + 1
                if (
                    0 <= new_row < M
                    and 0 <= new_col < N
                    and not vis[new_row][new_col]
                    and grid[row][col] < grid[new_row][new_col]
                ):
                    vis[new_row][new_col] = True
                    q.append((new_row, new_col, count + 1))

        return max_moves
