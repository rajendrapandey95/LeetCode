class Solution:
    def spiralMatrixIII(self, rows: int, cols: int, r: int, c: int) -> List[List[int]]:
        res, dirs, step = [], [(0, 1), (1, 0), (0, -1), (-1, 0)], 1
        while len(res) < rows * cols:
            for _ in range(2):
                for _ in range(step):
                    if 0 <= r < rows and 0 <= c < cols:
                        res.append([r, c])
                    r += dirs[0][0]
                    c += dirs[0][1]
                dirs.append(dirs.pop(0))  # Rotate direction
            step += 1
        return res
