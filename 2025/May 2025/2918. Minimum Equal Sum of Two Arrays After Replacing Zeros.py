class Solution:
    def minSum(self, A: List[int], B: List[int]) -> int:
        s1, z1 = sum(x or 1 for x in A), A.count(0)
        s2, z2 = sum(x or 1 for x in B), B.count(0)
        return -1 if (z1 == 0 and s2 > s1) or (z2 == 0 and s1 > s2) else max(s1, s2)
