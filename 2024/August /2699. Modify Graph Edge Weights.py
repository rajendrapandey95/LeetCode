from typing import List

class Solution:
    INF = int(2e9)

    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:
        dist = self.run_dijkstra(edges, n, source, destination)
        if dist < target: return []
        exact = dist == target

        for e in edges:
            if e[2] > 0: continue
            e[2] = self.INF if exact else 1
            if not exact:
                new_dist = self.run_dijkstra(edges, n, source, destination)
                if new_dist <= target:
                    exact = True
                    e[2] += target - new_dist

        return edges if exact else []

    def run_dijkstra(self, edges: List[List[int]], n: int, source: int, destination: int) -> int:
        adj = [[self.INF] * n for _ in range(n)]
        dist, visited = [self.INF] * n, [False] * n
        dist[source] = 0

        for u, v, w in edges:
            if w != -1:
                adj[u][v] = adj[v][u] = w

        for _ in range(n):
            u = min((dist[i], i) for i in range(n) if not visited[i])[1]
            visited[u] = True
            for v in range(n):
                dist[v] = min(dist[v], dist[u] + adj[u][v])

        return dist[destination]
