from typing import List

class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort(reverse=True)  # Sort nums in non-decreasing order
        
        for x in range(len(nums) + 1):  # Iterate over possible values of x
            count = sum(1 for num in nums if num >= x)  # Count numbers greater than or equal to x
            
            if count == x:  # If exactly x numbers are greater than or equal to x
                return x
                
        return -1  # If no such x is found

# Example usage:
solution = Solution()
print(solution.specialArray([3, 5, 2, 0, 4]))  # Output should be 2
