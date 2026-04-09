class Solution:
    def xorAfterQueries(self,a,q):
        M=10**9+7; n=len(a); T=int(n**0.5)
        g=[[] for _ in range(T)]

        for l,r,k,v in q:
            if k<T: g[k].append((l,r,v))
            else:
                for i in range(l,r+1,k): a[i]=a[i]*v%M

        for k in range(1,T):
            if not g[k]: continue
            d=[1]*(n+T)
            for l,r,v in g[k]:
                d[l]=d[l]*v%M
                d[((r-l)//k+1)*k+l]=d[((r-l)//k+1)*k+l]*pow(v,M-2,M)%M
            for i in range(k,n): d[i]=d[i]*d[i-k]%M
            for i in range(n): a[i]=a[i]*d[i]%M

        return eval("^".join(map(str,a)))
