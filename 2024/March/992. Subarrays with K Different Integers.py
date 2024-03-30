from collections import defaultdict

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        def atMostKDistinct(k):
            count = defaultdict(int)
            distinct = 0
            left = 0
            total = 0
            for right, value in enumerate(nums):
                if count[value] == 0:
                    distinct += 1
                count[value] += 1
                
                while distinct > k:
                    count[nums[left]] -= 1
                    if count[nums[left]] == 0:
                        distinct -= 1
                    left += 1
                
                total += right - left + 1
            return total
        
        return atMostKDistinct(k) - atMostKDistinct(k - 1)
