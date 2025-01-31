from typing import List

class DisjointSet:
    def __init__(self, n: int):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x: int) -> int:
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x: int, y: int):
        x, y = self.find(x), self.find(y)
        if x != y:
            if self.size[x] < self.size[y]:
                x, y = y, x
            self.parent[y] = x
            self.size[x] += self.size[y]

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n, ds, dirs = len(grid), DisjointSet(len(grid) * len(grid)), [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        def index(r, c): return r * n + c

        # Union adjacent '1's
        for r in range(n):
            for c in range(n):
                if grid[r][c]:
                    for dr, dc in dirs:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < n and 0 <= nc < n and grid[nr][nc]:
                            ds.union(index(r, c), index(nr, nc))

        # Find max island by flipping '0' to '1'
        max_size, has_zero = 0, False
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:
                    has_zero, seen, size = True, set(), 1
                    for dr, dc in dirs:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < n and 0 <= nc < n and grid[nr][nc]:
                            root = ds.find(index(nr, nc))
                            if root not in seen:
                                size += ds.size[root]
                                seen.add(root)
                    max_size = max(max_size, size)

        return max_size if has_zero else n * n
