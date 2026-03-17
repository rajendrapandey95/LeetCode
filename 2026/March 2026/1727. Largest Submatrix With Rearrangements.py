class Solution:
    def largestSubmatrix(self, mat):
        m,n=len(mat),len(mat[0])
        ans=0
        
        for i in range(m):
            for j in range(n):
                if mat[i][j] and i:
                    mat[i][j]+=mat[i-1][j]
            
            row=sorted(mat[i],reverse=True)
            for k,h in enumerate(row):
                ans=max(ans,h*(k+1))
        
        return ans
      
