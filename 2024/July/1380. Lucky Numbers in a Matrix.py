class Solution:
    def luckyNumbers(self, mat):
        n = len(mat)
        m = len(mat[0])

        rMin = [min(row) for row in mat]
        cMax = [max(col) for col in zip(*mat)]

        return [mat[i][j] for i in range(n) for j in range(m) if mat[i][j] == rMin[i] and mat[i][j] == cMax[j]]
