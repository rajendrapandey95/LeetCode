from typing import List

class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        bit_count = [0] * 24
        for i in range(24):
            for num in candidates:
                if num & (1 << i):
                    bit_count[i] += 1
        return max(bit_count)
