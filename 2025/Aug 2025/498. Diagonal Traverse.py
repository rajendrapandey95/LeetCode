class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]: return []
        m, n, res = len(mat), len(mat[0]), []
        for d in range(m + n - 1):
            tmp, r, c = [], (0 if d < n else d - n + 1), (d if d < n else n - 1)
            while r < m and c > -1:
                tmp.append(mat[r][c])
                r, c = r + 1, c - 1
            res.extend(tmp if d % 2 else tmp[::-1])
        return res
