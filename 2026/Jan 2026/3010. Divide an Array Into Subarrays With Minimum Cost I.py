class Solution:
    def minimumCost(self, A: List[int]) -> int:
        x, y = sorted(A[1:])[:2]
        return A[0] + x + y
