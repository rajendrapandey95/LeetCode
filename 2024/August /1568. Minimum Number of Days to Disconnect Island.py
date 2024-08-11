class Solution:
    def minDays(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        def count_islands():
            visited = set()
            islands = 0
            for i in range(rows):
                for j in range(cols):
                    if grid[i][j] == 1 and (i, j) not in visited:
                        explore_island(i, j, visited)
                        islands += 1
                        if islands > 1:  # Early exit if more than 1 island found
                            return islands
            return islands

        def explore_island(i, j, visited):
            stack = [(i, j)]
            visited.add((i, j))
            while stack:
                x, y = stack.pop()
                for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1 and (nx, ny) not in visited:
                        visited.add((nx, ny))
                        stack.append((nx, ny))

        if count_islands() != 1:
            return 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    if count_islands() != 1:
                        return 1
                    grid[i][j] = 1

        return 2
