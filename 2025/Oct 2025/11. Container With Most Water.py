class Solution:
    def maxArea(self, h: list[int]) -> int:
        i,j,res=0,len(h)-1,0
        while i<j:
            res=max(res,(j-i)*min(h[i],h[j]))
            if h[i]<h[j]:i+=1
            else:j-=1
        return res
