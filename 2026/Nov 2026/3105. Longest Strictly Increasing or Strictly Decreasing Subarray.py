class Solution:
    def longestMonotonicSubarray(self, nums: list[int]) -> int:
        best = up = down = 1
        for a, b in pairwise(nums):
            up = up + 1 if a < b else 1  
            down = down + 1 if a > b else 1 
            best = max(best, up, down)
        return best
