class Solution:
    def smallestDistancePair(self, nums, k):
        nums.sort()
        array_size = len(nums)

        left, right = 0, nums[-1] - nums[0]

        while left < right:
            mid = (left + right) // 2
            count = self.count_pairs_within_distance(nums, mid)

            if count < k:
                left = mid + 1
            else:
                right = mid

        return left

    def count_pairs_within_distance(self, nums, distance):
        count = 0
        j = 0

        for i in range(len(nums)):
            while j < len(nums) and nums[j] - nums[i] <= distance:
                j += 1
            count += j - i - 1

        return count
