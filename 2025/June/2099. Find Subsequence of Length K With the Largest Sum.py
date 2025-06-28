class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        topk = sorted([(i, v) for i, v in enumerate(nums)], key=lambda x: -x[1])[:k]
        return [v for i, v in sorted(topk)]
