from typing import List
from collections import deque

class Solution:
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        adj, parent, depth = [[] for _ in range(n)], [-1] * n, [0] * n

        def find(x):
            while parent[x] != -1:
                x = parent[x]
            return x

        def union(x, y):
            x, y = find(x), find(y)
            if x != y:
                if depth[x] < depth[y]:
                    x, y = y, x
                parent[y] = x
                depth[x] += depth[x] == depth[y]

        for u, v in edges:
            u, v = u - 1, v - 1
            adj[u].append(v)
            adj[v].append(u)
            union(u, v)

        def bfs(src):
            q, layers, seen = deque([src]), 0, [-1] * n
            seen[src] = 0
            while q:
                for _ in range(len(q)):
                    node = q.popleft()
                    for nei in adj[node]:
                        if seen[nei] == -1:
                            seen[nei] = layers + 1
                            q.append(nei)
                        elif seen[nei] == layers:
                            return -1
                layers += 1
            return layers

        groups = {}
        for i in range(n):
            g = bfs(i)
            if g == -1:
                return -1
            root = find(i)
            groups[root] = max(groups.get(root, 0), g)

        return sum(groups.values())
