class Solution:
    def areSimilar(self, mat, k):
        n=len(mat[0])
        k%=n
        for row in mat:
            for j,v in enumerate(row):
                if v!=row[(j+k)%n]:
                    return False
        return True
