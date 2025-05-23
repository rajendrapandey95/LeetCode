class Solution(object):
    def maxSumOfNodes(self, index, isEven, nums, k, memo):
        if index == len(nums):
            return 0 if isEven == 1 else -float("inf")

        if memo[index][isEven] != -1:
            return memo[index][isEven]

        noXor = nums[index] + self.maxSumOfNodes(index + 1, isEven, nums, k, memo)

        xorVal = (nums[index] ^ k) + self.maxSumOfNodes(index + 1, isEven ^ 1, nums, k, memo)

        memo[index][isEven] = max(noXor, xorVal)
        return memo[index][isEven]

    def maximumValueSum(self, nums, k, edges):
        memo = [[-1] * 2 for _ in range(len(nums))]
        return self.maxSumOfNodes(0, 1, nums, k, memo)
