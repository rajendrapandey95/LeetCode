class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left, right = [], []
        count = 0  

        for num in nums:
            if num < pivot:
                left.append(num)
            elif num > pivot:
                right.append(num)
            else:
                count += 1 

        return left + [pivot] * count + right
