class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Step 1: Find the intersection point of the two pointers
        tortoise = nums[0]
        hare = nums[0]
        
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break
        
        # Step 2: Find the entrance to the cycle (the repeated number)
        tortoise = nums[0]
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]
        
        return hare
