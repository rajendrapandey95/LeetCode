class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        n, sums = len(nums) - k + 1, [sum(nums[:k])]
        for i in range(k, len(nums)):
            sums.append(sums[-1] - nums[i - k] + nums[i])

        memo, indices = [[-1] * 4 for _ in range(n)], []
        self._dp(sums, k, 0, 3, memo)
        self._dfs(sums, k, 0, 3, memo, indices)
        return indices

    def _dp(self, sums, k, idx, rem, memo):
        if rem == 0: return 0
        if idx >= len(sums): return float("-inf")
        if memo[idx][rem] != -1: return memo[idx][rem]

        with_current = sums[idx] + self._dp(sums, k, idx + k, rem - 1, memo)
        skip_current = self._dp(sums, k, idx + 1, rem, memo)
        memo[idx][rem] = max(with_current, skip_current)
        return memo[idx][rem]

    def _dfs(self, sums, k, idx, rem, memo, indices):
        if rem == 0 or idx >= len(sums): return
        if sums[idx] + self._dp(sums, k, idx + k, rem - 1, memo) >= self._dp(sums, k, idx + 1, rem, memo):
            indices.append(idx)
            self._dfs(sums, k, idx + k, rem - 1, memo, indices)
        else:
            self._dfs(sums, k, idx + 1, rem, memo, indices)
