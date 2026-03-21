class Solution:
    def reverseSubmatrix(self, g, x, y, k):
        i,j=x,x+k-1
        while i<j:
            for c in range(y,y+k):
                g[i][c],g[j][c]=g[j][c],g[i][c]
            i+=1; j-=1
        return g
