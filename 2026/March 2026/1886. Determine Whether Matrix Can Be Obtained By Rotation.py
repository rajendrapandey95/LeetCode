class Solution:
    def findRotation(self, mat, target):
        n=len(mat)
        for _ in range(4):
            if mat==target: return True
            for i in range(n//2):
                for j in range((n+1)//2):
                    mat[i][j],mat[n-1-j][i],mat[n-1-i][n-1-j],mat[j][n-1-i]=\
                    mat[n-1-j][i],mat[n-1-i][n-1-j],mat[j][n-1-i],mat[i][j]
        return False
