class Solution:
    def minimumDistance(self,w):
        d=lambda a,b:abs(a//6-b//6)+abs(a%6-b%6)
        dp=[[10**9]*26 for _ in range(26)]
        x=ord(w[0])-65
        for i in range(26): dp[i][x]=dp[x][i]=0

        for i in range(1,len(w)):
            c,p=ord(w[i])-65,ord(w[i-1])-65
            nd=[[10**9]*26 for _ in range(26)]
            for l in range(26):
                for r in range(26):
                    v=dp[l][r]
                    if v==10**9: continue
                    nd[c][r]=min(nd[c][r],v+d(p,c),v+d(l,c))
                    nd[l][c]=min(nd[l][c],v+d(p,c),v+d(r,c))
            dp=nd

        return min(map(min,dp))
