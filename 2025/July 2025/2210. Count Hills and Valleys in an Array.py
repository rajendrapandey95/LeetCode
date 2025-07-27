from typing import List

class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        arr = [nums[0]]
        for num in nums[1:]:
            if num != arr[-1]:
                arr.append(num)

        res = 0
        for i in range(1, len(arr) - 1):
            if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
                res += 1  
            elif arr[i] < arr[i - 1] and arr[i] < arr[i + 1]:
                res += 1  
        return res
