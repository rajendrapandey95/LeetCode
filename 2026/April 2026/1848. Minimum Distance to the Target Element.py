class Solution:
    def getMinDistance(self, a, t, s):
        return min(abs(i-s) for i,x in enumerate(a) if x==t)
