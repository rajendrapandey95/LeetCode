class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        max_heap = [-num for num in nums]
        heapq.heapify(max_heap)
        ans = 0
        while k > 0:
            k -= 1
            max_element = -heapq.heappop(max_heap)
            ans += max_element
            heapq.heappush(max_heap, -math.ceil(max_element / 3))
        return ans
