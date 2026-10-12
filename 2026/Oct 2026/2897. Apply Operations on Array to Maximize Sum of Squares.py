class Solution:
    def maxSum(self, nums: list[int], k: int) -> int:
        cnt = [sum(x >> b & 1 for x in nums) for b in range(30)]  
        total = 0
        for i in range(k):  
            row = sum(1 << b for b in range(30) if cnt[b] > i)  
            total += row * row
        return total % (10**9 + 7)
