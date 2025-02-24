from collections import deque
from typing import List

class Solution:
    def __init__(self):
        self.bob_path, self.tree = {}, []

    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        n, q, mx = len(amount), deque([(0, 0, 0)]), float("-inf")
        self.tree, visited = [[] for _ in range(n)], [False] * n

        for u, v in edges:
            self.tree[u].append(v)
            self.tree[v].append(u)

        self.find_bob_path(bob, 0, visited[:]) 

        visited = [False] * n
        while q:
            node, t, inc = q.popleft()
            if node not in self.bob_path or t < self.bob_path[node]:
                inc += amount[node]
            elif t == self.bob_path[node]:
                inc += amount[node] // 2
            if len(self.tree[node]) == 1 and node: mx = max(mx, inc)
            for nei in self.tree[node]:
                if not visited[nei]: q.append((nei, t + 1, inc))
            visited[node] = True

        return mx

    def find_bob_path(self, node: int, t: int, visited: List[bool]) -> bool:
        self.bob_path[node], visited[node] = t, True
        if node == 0: return True
        for nei in self.tree[node]:
            if not visited[nei] and self.find_bob_path(nei, t + 1, visited): return True
        self.bob_path.pop(node)
        return False
