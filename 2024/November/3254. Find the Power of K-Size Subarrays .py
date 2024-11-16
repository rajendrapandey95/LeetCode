class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        n, res, dq = len(nums), [-1] * (len(nums) - k + 1), collections.deque()
        for i in range(n):
            if dq and dq[0] < i - k + 1: dq.popleft()
            if dq and nums[i] != nums[i - 1] + 1: dq.clear()
            dq.append(i)
            if i >= k - 1:
                res[i - k + 1] = nums[dq[-1]] if len(dq) == k else -1
        return res
