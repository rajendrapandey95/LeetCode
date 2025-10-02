class Solution:
    def maxBottlesDrunk(self, n: int, x: int) -> int:
        a=e=n
        while e>=x:e-=x-1;a+=1;x+=1
        return a
