class DSU:
    def __init__(self,n):
        self.p=list(range(n))
        self.r=[0]*n
        self.c=n

    def find(self,x):
        if self.p[x]!=x:
            self.p[x]=self.find(self.p[x])
        return self.p[x]

    def unite(self,a,b):
        a,b=self.find(a),self.find(b)
        if a==b:return 0
        if self.r[a]<self.r[b]:a,b=b,a
        self.p[b]=a
        if self.r[a]==self.r[b]:self.r[a]+=1
        self.c-=1
        return 1


class Solution:
    def canAchieve(self,n,edges,k,x):
        d=DSU(n)

        for u,v,s,m in edges:
            if m:
                if s<x or not d.unite(u,v): return 0

        for u,v,s,m in edges:
            if not m and s>=x:
                d.unite(u,v)

        up=0
        for u,v,s,m in edges:
            if not m and s<x and s*2>=x:
                if d.unite(u,v):
                    up+=1
                    if up>k:return 0

        return d.c==1


    def maxStability(self,n,edges,k):
        d=DSU(n)
        for u,v,s,m in edges:
            if m and not d.unite(u,v):
                return -1

        l,h,ans=1,200000,-1

        while l<=h:
            mid=(l+h)//2
            if self.canAchieve(n,edges,k,mid):
                ans=mid
                l=mid+1
            else:
                h=mid-1

        return ans
