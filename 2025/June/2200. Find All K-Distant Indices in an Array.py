class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        res = []
        r = 0
        for j, v in enumerate(nums):
            if v == key:
                l = max(r, j - k)
                r = min(len(nums)-1, j + k) + 1
                res += range(l, r)
        return list(res)
