class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.ways = 0

        def dfs(idx, total):
            if idx == len(nums):
                self.ways += total == target
                return
            dfs(idx + 1, total + nums[idx])
            dfs(idx + 1, total - nums[idx])

        dfs(0, 0)
        return self.ways
