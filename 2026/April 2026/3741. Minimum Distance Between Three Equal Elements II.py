class Solution:
    def minimumDistance(self, a):
        n=len(a)
        nxt=[-1]*n
        pos={}
        ans=n+1

        for i in range(n-1,-1,-1):
            if a[i] in pos: nxt[i]=pos[a[i]]
            pos[a[i]]=i

        for i in range(n):
            j=nxt[i]
            if j!=-1 and nxt[j]!=-1:
                ans=min(ans,nxt[j]-i)

        return -1 if ans==n+1 else ans*2
