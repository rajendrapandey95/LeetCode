class Solution:
    def reverseDegree(self, s: str) -> int:
        return sum((i+1)*(ord('z')-ord(c)+1) for i, c in enumerate(s))
