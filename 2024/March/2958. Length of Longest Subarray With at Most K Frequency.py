class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        frequency = {}
        left = 0
        max_length = 0

        for right in range(len(nums)):
            frequency[nums[right]] = frequency.get(nums[right], 0) + 1

            while max(frequency.values()) > k:
                frequency[nums[left]] -= 1
                if frequency[nums[left]] == 0:
                    del frequency[nums[left]]
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length
