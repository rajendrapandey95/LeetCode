class Solution:
    def maxWidthRamp(self, nums):
        n = len(nums)
        stack = []
        
        # Fill the stack with indices in increasing order of their values
        for i in range(n):
            if not stack or nums[stack[-1]] > nums[i]:
                stack.append(i)

        max_width = 0
        
        # Traverse the array from the end to the start
        for j in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[j]:
                max_width = max(max_width, j - stack.pop())
        
        return max_width
