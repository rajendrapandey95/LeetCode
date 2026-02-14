class Solution:
    def champagneTower(self, poured, r, c):
        A = [[0.0]*(i+1) for i in range(101)]
        A[0][0] = poured
        for i in range(r+1):
            for j in range(i+1):
                x = (A[i][j]-1)/2
                if x > 0:
                    A[i+1][j] += x
                    A[i+1][j+1] += x
        return min(1, A[r][c])
