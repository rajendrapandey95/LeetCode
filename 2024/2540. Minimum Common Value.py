from typing import List

class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        # Initialize pointers for both arrays
        pointer1 = 0
        pointer2 = 0
        
        # Iterate until we exhaust any of the arrays
        while pointer1 < len(nums1) and pointer2 < len(nums2):
            # If we find a common integer, return it
            if nums1[pointer1] == nums2[pointer2]:
                return nums1[pointer1]
            
            # Move the pointer for the array with the smaller element
            if nums1[pointer1] < nums2[pointer2]:
                pointer1 += 1
            else:
                pointer2 += 1
        
        # If no common integer is found
        return -1
