class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        last = {}
        n = len(nums)

        for i, v in enumerate(nums):
            last[v] = i

        segments = 0
        curr_end = 0

        for i, v in enumerate(nums):
            curr_end = max(curr_end, last[v])
            if i == curr_end:
                segments += 1

        MOD = 10**9 + 7
        return pow(2, segments - 1, MOD)
