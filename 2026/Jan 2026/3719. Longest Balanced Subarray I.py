class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n, ans = len(nums), 0

        for i in range(n):
            odd, even = {}, {}
            for j in range(i, n):
                d = odd if nums[j] & 1 else even
                d[nums[j]] = d.get(nums[j], 0) + 1
                if len(odd) == len(even):
                    ans = max(ans, j - i + 1)

        return ans
