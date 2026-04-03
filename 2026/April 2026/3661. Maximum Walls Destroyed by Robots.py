class Solution:
    def maxWalls(self, r, d, w):
        import bisect as B

        n=len(r)
        mp=dict(zip(r,d))
        r.sort(); w.sort()

        L=[0]*n; R=[0]*n; num=[0]*n

        for i in range(n):
            pos=B.bisect_right(w,r[i])

            lb = max(r[i]-mp[r[i]], r[i-1]+1) if i else r[i]-mp[r[i]]
            L[i]=pos - B.bisect_left(w,lb)

            rb = min(r[i]+mp[r[i]], r[i+1]-1) if i<n-1 else r[i]+mp[r[i]]
            R[i]=B.bisect_right(w,rb) - B.bisect_left(w,r[i])

            if i:
                num[i]=pos - B.bisect_left(w,r[i-1])

        sl,sr=L[0],R[0]

        for i in range(1,n):
            nl=max(sl+L[i],
                   sr-R[i-1]+min(L[i]+R[i-1],num[i]))
            nr=max(sl+R[i], sr+R[i])
            sl,sr=nl,nr

        return max(sl,sr)
