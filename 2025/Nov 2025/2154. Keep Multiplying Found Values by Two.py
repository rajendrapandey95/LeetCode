class Solution:
    def findFinalValue(self, a,o):
        a=set(a)
        while o in a:o*=2
        return o
