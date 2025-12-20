class Solution:
    def minDeletionSize(self, strs):
        return sum(
            any(strs[r][c] < strs[r-1][c] for r in range(1, len(strs)))
            for c in range(len(strs[0]))
        )
