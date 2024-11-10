class Solution:
    def minimumSubarrayLength(self, nums: List[int], k: int) -> int:
        min_len, start, bits = float("inf"), 0, [0] * 32
        for end in range(len(nums)):
            self._update(bits, nums[end], 1)
            while start <= end and self._to_num(bits) >= k:
                min_len = min(min_len, end - start + 1)
                self._update(bits, nums[start], -1)
                start += 1
        return -1 if min_len == float("inf") else min_len

    def _update(self, bits, num, delta):
        for pos in range(32):
            if num & (1 << pos):
                bits[pos] += delta

    def _to_num(self, bits):
        return sum((1 << pos) for pos in range(32) if bits[pos])
