class DSU:
    def __init__(self, n):
        self.p = list(range(n))

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, a, b):
        pa, pb = self.find(a), self.find(b)
        if pa != pb:
            self.p[pa] = pb


class Solution:
    def latestDayToCross(self, row: int, col: int, cells: list[list[int]]) -> int:
        N = row * col
        dsu = DSU(N + 2)
        grid = [[0]*col for _ in range(row)]
        top, bottom = 0, N + 1
        dirs = [(1,0),(-1,0),(0,1),(0,-1)]

        for i in range(len(cells)-1, -1, -1):
            r, c = cells[i][0]-1, cells[i][1]-1
            grid[r][c] = 1
            idx = r * col + c + 1

            for dr, dc in dirs:
                nr, nc = r+dr, c+dc
                if 0 <= nr < row and 0 <= nc < col and grid[nr][nc]:
                    dsu.union(idx, nr*col + nc + 1)

            if r == 0:
                dsu.union(top, idx)
            if r == row-1:
                dsu.union(bottom, idx)

            if dsu.find(top) == dsu.find(bottom):
                return i

        return -1
