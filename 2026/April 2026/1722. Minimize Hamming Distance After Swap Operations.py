class Solution:
    def minimumHammingDistance(self,s,t,sw):
        p=list(range(len(s)))
        def f(x):
            if p[x]!=x: p[x]=f(p[x])
            return p[x]
        for a,b in sw:
            p[f(a)]=f(b)

        from collections import defaultdict
        d=defaultdict(lambda:defaultdict(int))
        for i,x in enumerate(s): d[f(i)][x]+=1

        ans=0
        for i,x in enumerate(t):
            if d[f(i)][x]: d[f(i)][x]-=1
            else: ans+=1
        return ans
