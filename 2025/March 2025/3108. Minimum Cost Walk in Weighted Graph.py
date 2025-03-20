# Write your MySQL query statement below
from collections import deque
class Solution:
    def minimumCost(self, n, edges, queries):
        adj = [[] for _ in range(n)]
        for u, v, w in edges:
            adj[u].append((v, w))
            adj[v].append((u, w))
        vis = [0] * n
        comp, cost = [0] * n, []
        cid = 0
        for i in range(n):
            if not vis[i]:
                cost.append(self.bfs(i, adj, vis, comp, cid))
                cid += 1
        return [cost[comp[u]] if comp[u] == comp[v] else -1 for u, v in queries]

    def bfs(self, src, adj, vis, comp, cid):
        q, res = deque([src]), -1
        vis[src] = 1
        while q:
            u = q.popleft()
            comp[u] = cid
            for v, w in adj[u]:
                res &= w
                if vis[v]: continue
                vis[v] = 1
                q.append(v)
        return res
