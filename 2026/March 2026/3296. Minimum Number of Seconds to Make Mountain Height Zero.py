class Solution:
    def minNumberOfSeconds(self, h: int, w: List[int]) -> int:
        l,r=1,max(w)*h*(h+1)//2
        eps=1e-7
        
        while l<=r:
            m=(l+r)//2
            cnt=0
            for t in w:
                work=m//t
                cnt+=int((-1+(1+8*work)**0.5)/2+eps)
            
            if cnt>=h:
                r=m-1
            else:
                l=m+1
                
        return l
