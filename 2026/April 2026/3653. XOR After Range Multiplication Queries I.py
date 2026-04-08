class Solution:
    def xorAfterQueries(self,a,q):
        M=10**9+7; n=len(a); m=[1]*n
        for l,r,k,v in q:
            for i in range(l,r+1,k): m[i]=m[i]*v%M
        return eval("^".join(str(a[i]*m[i]%M) for i in range(n)))
