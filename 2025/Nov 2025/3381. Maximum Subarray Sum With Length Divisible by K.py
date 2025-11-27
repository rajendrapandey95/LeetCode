class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        import sys

        n = len(nums)
        prefix = 0
        maxSum = -sys.maxsize

        kMin = [sys.maxsize] * k
        kMin[(k - 1) % k] = 0   

        for i, num in enumerate(nums):
            prefix += num
            r = i % k

            maxSum = max(maxSum, prefix - kMin[r])

            kMin[r] = min(kMin[r], prefix)

        return maxSum
