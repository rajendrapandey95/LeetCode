from collections import defaultdict
from typing import List

class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        merged_dict = defaultdict(int)

        for key, value in nums1:
            merged_dict[key] += value
        for key, value in nums2:
            merged_dict[key] += value

        return sorted(merged_dict.items())
