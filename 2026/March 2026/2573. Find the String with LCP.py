class Solution:
    def findTheString(self, a):
        n=len(a); w=['']*n; c=97

        for i in range(n):
            if not w[i]:
                if c>122: return ""
                for j in range(i,n):
                    if j==i or a[i][j]: w[j]=chr(c)
                c+=1

        for i in range(n-1,-1,-1):
            for j in range(n-1,-1,-1):
                if (w[i]!=w[j] and a[i][j]) or \
                   (w[i]==w[j] and ((i==n-1 or j==n-1 and a[i][j]!=1) or
                   (i<n-1 and j<n-1 and a[i][j]!=a[i+1][j+1]+1))):
                    return ""

        return "".join(w)
