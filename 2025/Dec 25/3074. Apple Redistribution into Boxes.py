class Solution:
    def minimumBoxes(self, a, c):
        s=0; c.sort(reverse=True)
        for i,x in enumerate(c):
            s+=x
            if s>=sum(a): return i+1
