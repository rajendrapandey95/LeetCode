import heapq

class State:
    def __init__(self, x, y, dis):
        self.x = x
        self.y = y
        self.dis = dis

    def __lt__(self, other):
        return self.dis < other.dis

class Solution:
    def minTimeToReach(self, moveTime):
        n, m = len(moveTime), len(moveTime[0])
        inf = float("inf")
        d = [[inf] * m for _ in range(n)]
        visited = [[False] * m for _ in range(n)]

        d[0][0] = 0
        pq = []
        heapq.heappush(pq, State(0, 0, 0))

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        while pq:
            s = heapq.heappop(pq)
            if visited[s.x][s.y]:
                continue
            if s.x == n - 1 and s.y == m - 1:
                break
            visited[s.x][s.y] = True

            for dx, dy in directions:
                nx, ny = s.x + dx, s.y + dy
                if 0 <= nx < n and 0 <= ny < m:
                    extra_cost = (s.x + s.y) % 2 + 1
                    next_time = max(d[s.x][s.y], moveTime[nx][ny]) + extra_cost
                    if d[nx][ny] > next_time:
                        d[nx][ny] = next_time
                        heapq.heappush(pq, State(nx, ny, next_time))

        return d[n - 1][m - 1]
