class Solution:
    def findXSum(self, nums, k, x):
        from collections import Counter
        import heapq
        return [
            sum(v*c for v, c in heapq.nlargest(x, Counter(nums[i:i+k]).items(), key=lambda t:(t[1],t[0])))
            for i in range(len(nums)-k+1)
        ]
