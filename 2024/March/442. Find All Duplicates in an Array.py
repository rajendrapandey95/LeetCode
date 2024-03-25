class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        duplicates = []
        
        for num in nums:
            # Index to be checked
            index = abs(num) - 1
            
            # If the value at this index is negative, it means we've seen this number before
            if nums[index] < 0:
                duplicates.append(abs(num))
            else:
                # Mark the number as visited by negating its value
                nums[index] = -nums[index]
        
        return duplicates
