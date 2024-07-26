from heapq import heappop, heappush
from typing import List

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], dt: int) -> int:
        adj = [[] for _ in range(n)]
        dist = [[float("inf")] * n for _ in range(n)]
        for i in range(n): dist[i][i] = 0
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))
        for i in range(n): self.dijkstra(n, adj, dist[i], i)
        return self.get_city(n, dist, dt)
    
    def dijkstra(self, n: int, adj: List[List[tuple]], dist: List[int], src: int):
        pq = [(0, src)]
        dist[:] = [float("inf")] * n
        dist[src] = 0
        while pq:
            d, u = heappop(pq)
            if d > dist[u]: continue
            for v, w in adj[u]:
                if dist[v] > d + w:
                    dist[v] = d + w
                    heappush(pq, (dist[v], v))
    
    def get_city(self, n: int, dist: List[List[int]], dt: int) -> int:
        res, min_reach = -1, n
        for i in range(n):
            reach = sum(1 for j in range(n) if i != j and dist[i][j] <= dt)
            if reach <= min_reach:
                min_reach, res = reach, i
        return res
