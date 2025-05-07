import heapq

class Solution:
    def minTimeToReach(self, moveTime):
        n, m = len(moveTime), len(moveTime[0])
        inf = float("inf")
        d = [[inf] * m for _ in range(n)]
        visited = [[False] * m for _ in range(n)]
        d[0][0] = 0

        heap = [(0, 0, 0)]  # (distance, x, y)
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while heap:
            dis, x, y = heapq.heappop(heap)
            if visited[x][y]:
                continue
            visited[x][y] = True

            for dx, dy in dirs:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < m:
                    wait_time = max(d[x][y], moveTime[nx][ny]) + 1
                    if wait_time < d[nx][ny]:
                        d[nx][ny] = wait_time
                        heapq.heappush(heap, (wait_time, nx, ny))

        return d[n - 1][m - 1]
