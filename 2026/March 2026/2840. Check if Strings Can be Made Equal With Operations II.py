class Solution:
    def checkStrings(self, a, b):
        return sorted(a[::2])==sorted(b[::2]) and sorted(a[1::2])==sorted(b[1::2])
      
