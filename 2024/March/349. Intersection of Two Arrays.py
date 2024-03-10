class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Convert arrays to sets
        set1 = set(nums1)
        set2 = set(nums2)
        
        # Find the intersection
        intersection_set = set1.intersection(set2)
        
        # Convert intersection set to a list and return
        return list(intersection_set)
