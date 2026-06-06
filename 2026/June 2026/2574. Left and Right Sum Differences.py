class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        return (L:=list(accumulate(nums, initial=0))) and [abs(L[-1]-x-2*l) for l, x in zip(L, nums)]
