class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        d = [0] * 100001
        k = k1 + k2
        total = 0
        mx = 0

        for a, b in zip(nums1, nums2):
            x = abs(a - b)
            d[x] += 1
            total += x
            mx = max(mx, x)

        
        if total <= k:
            return 0

        for i in range(mx, 0, -1):
            if k <= 0:
                break
            move = min(k, d[i])
            d[i] -= move
            d[i - 1] += move
            k -= move

        ans = 0
        for i in range(mx + 1):
            ans += i * i * d[i]

        return ans
