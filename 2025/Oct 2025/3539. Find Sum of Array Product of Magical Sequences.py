from typing import List
class Solution:
    def magicalSum(self, m: int, k: int, nums: List[int]) -> int:
        n=len(nums);MOD=10**9+7
        fac=[1]*(m+1)
        for i in range(1,m+1): fac[i]=fac[i-1]*i%MOD
        ifac=[1]*(m+1); ifac[m]=pow(fac[m],MOD-2,MOD)
        for i in range(m-1,-1,-1): ifac[i]=ifac[i+1]*(i+1)%MOD

        npow=[[1]*(m+1) for _ in range(n)]
        for i in range(n):
            for j in range(1,m+1): npow[i][j]=npow[i][j-1]*nums[i]%MOD

        W=2*m+1
        f = [[[[0]*(k+1) for _ in range(W)] for _ in range(m+1)] for _ in range(n)]
        for j in range(m+1): f[0][j][j][0]=npow[0][j]*ifac[j]%MOD

        for i in range(n-1):
            for j in range(m+1):
                for p in range(W):
                    for q in range(k+1):
                        val=f[i][j][p][q]
                        if not val: continue
                        q2=(p%2)+q
                        if q2>k: continue
                        for r in range(m-j+1):
                            p2=(p//2)+r
                            if p2>=W: break
                            f[i+1][j+r][p2][q2]=(f[i+1][j+r][p2][q2] + val * npow[i+1][r] % MOD * ifac[r])%MOD

        res=0
        for p in range(W):
            for q in range(k+1):
                if bin(p).count("1")+q==k:
                    res=(res + f[n-1][m][p][q]*fac[m])%MOD
        return res
