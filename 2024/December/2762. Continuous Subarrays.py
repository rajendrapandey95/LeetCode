class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        from collections import Counter

        freq, left, count = Counter(), 0, 0

        for right in range(len(nums)):
            freq[nums[right]] += 1

            while max(freq) - min(freq) > 2:
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    del freq[nums[left]]
                left += 1

            count += right - left + 1

        return count
