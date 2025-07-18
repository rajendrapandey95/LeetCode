import heapq

class Solution:
    def minimumDifference(self, nums: list[int]) -> int:
        n = len(nums) // 3
        left_sum = sum(nums[:n])
        max_heap = [-x for x in nums[:n]]
        heapq.heapify(max_heap)
        
        left_prefix = [0] * (n + 1)
        left_prefix[0] = left_sum

        for i in range(n, 2 * n):
            heapq.heappush(max_heap, -nums[i])
            left_sum += nums[i] + heapq.heappop(max_heap)
            left_prefix[i - n + 1] = left_sum

        right_sum = sum(nums[2 * n:])
        min_heap = nums[2 * n:]
        heapq.heapify(min_heap)

        ans = left_prefix[n] - right_sum

        for i in range(2 * n - 1, n - 1, -1):
            heapq.heappush(min_heap, nums[i])
            right_sum += nums[i] - heapq.heappop(min_heap)
            ans = min(ans, left_prefix[i - n] - right_sum)

        return ans
