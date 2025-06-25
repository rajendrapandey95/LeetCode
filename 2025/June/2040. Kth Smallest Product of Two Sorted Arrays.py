from bisect import bisect_left, bisect_right

class Solution:
    def f(self, nums2, x, v):
        if x > 0: return bisect_right(nums2, v // x)
        if x < 0: return len(nums2) - bisect_left(nums2, -(-v // x))
        return len(nums2) if v >= 0 else 0

    def kthSmallestProduct(self, nums1, nums2, k: int) -> int:
        l, r = -10**10, 10**10
        while l <= r:
            m = (l + r) // 2
            cnt = sum(self.f(nums2, x, m) for x in nums1)
            if cnt < k: l = m + 1
            else: r = m - 1
        return l
