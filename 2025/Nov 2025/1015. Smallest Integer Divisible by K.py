class Solution:
    def smallestRepunitDivByK(self, k):
        r=0
        for i in range(1,k+1):
            r=(r*10+1)%k
            if not r:return i
        return -1
