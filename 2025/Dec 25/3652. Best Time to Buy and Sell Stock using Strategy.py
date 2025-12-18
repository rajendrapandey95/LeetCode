class Solution:
    def maxProfit(self,p,s,k):
        n=len(p);ps=[0]*(n+1);ss=[0]*(n+1)
        for i in range(n):
            ps[i+1]=ps[i]+p[i]*s[i]
            ss[i+1]=ss[i]+p[i]
        ans=ps[n];h=k//2
        for i in range(k-1,n):
            ans=max(ans,ps[i-k+1]+ss[i+1]-ss[i-h+1]+ps[n]-ps[i+1])
        return ans
