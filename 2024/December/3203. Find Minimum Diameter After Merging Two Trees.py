from math import ceil
from collections import deque
from typing import List

class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        def build_adj(n, edges):
            adj = [[] for _ in range(n)]
            for u, v in edges:
                adj[u].append(v)
                adj[v].append(u)
            return adj

        def find_diameter(n, adj):
            degrees = [len(adj[i]) for i in range(n)]
            leaves = deque(i for i in range(n) if degrees[i] == 1)
            remaining = n
            layers = 0

            while remaining > 2:
                layers += 1
                for _ in range(len(leaves)):
                    node = leaves.popleft()
                    remaining -= 1
                    for nei in adj[node]:
                        degrees[nei] -= 1
                        if degrees[nei] == 1:
                            leaves.append(nei)

            return 2 * layers + (1 if remaining == 2 else 0)

        n1, n2 = len(edges1) + 1, len(edges2) + 1
        adj1, adj2 = build_adj(n1, edges1), build_adj(n2, edges2)
        d1, d2 = find_diameter(n1, adj1), find_diameter(n2, adj2)

        return max(d1, d2, ceil(d1 / 2) + ceil(d2 / 2) + 1)

