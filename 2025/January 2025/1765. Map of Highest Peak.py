class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        from collections import deque
        dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
        rows, cols = len(isWater), len(isWater[0])
        heights = [[-1] * cols for _ in range(rows)]
        q = deque([(x, y) for x in range(rows) for y in range(cols) if isWater[x][y]])
        for x, y in q: heights[x][y] = 0
        while q:
            x, y = q.popleft()
            for i in range(4):
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < rows and 0 <= ny < cols and heights[nx][ny] == -1:
                    heights[nx][ny] = heights[x][y] + 1
                    q.append((nx, ny))
        return heights
