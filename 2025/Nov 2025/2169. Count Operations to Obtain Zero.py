class Solution:
    def countOperations(self, a, b):
        r=0
        while b:a,b,r=b,a%b,r+a//b
        return r
