from typing import List

class Solution:
    def minimumMountainRemovals(self, nums: List[int]) -> int:
        N = len(nums)
        lis, lds = [1] * N, [1] * N

        for i in range(N):
            for j in range(i):
                if nums[i] > nums[j]:
                    lis[i] = max(lis[i], lis[j] + 1)

        for i in range(N - 1, -1, -1):
            for j in range(i + 1, N):
                if nums[i] > nums[j]:
                    lds[i] = max(lds[i], lds[j] + 1)

        return min(N - lis[i] - lds[i] + 1 for i in range(N) if lis[i] > 1 and lds[i] > 1)
