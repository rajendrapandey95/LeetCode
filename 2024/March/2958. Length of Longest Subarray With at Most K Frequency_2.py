class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        frequency = {}
        left = 0
        max_length = 0
        total_elements = 0

        for right in range(len(nums)):
            # Update frequency of nums[right]
            frequency[nums[right]] = frequency.get(nums[right], 0) + 1
            
            # Update total number of elements within the window
            total_elements += 1
            
            # Slide the left pointer if frequency exceeds k
            while frequency[nums[right]] > k:
                frequency[nums[left]] -= 1
                left += 1
                total_elements -= 1
            
            # Update max_length if the current window is valid
            max_length = max(max_length, total_elements)

        return max_length
