class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()
        def count(th):
            i = cnt = 0
            while i < len(nums)-1:
                if nums[i+1] - nums[i] <= th:
                    cnt += 1
                    i += 1
                i += 1
            return cnt

        l, r = 0, nums[-1] - nums[0]
        while l < r:
            m = (l + r) // 2
            if count(m) >= p: r = m
            else: l = m + 1
        return l
