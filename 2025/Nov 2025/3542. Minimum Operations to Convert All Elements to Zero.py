class Solution:
    def minOperations(self, A: List[int]) -> int:
        s=[];r=0
        for x in A:
            while s and s[-1]>x:s.pop()
            if x and (not s or s[-1]<x):r+=1;s.append(x)
        return r
