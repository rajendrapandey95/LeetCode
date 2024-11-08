from typing import List

class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        prefix_xor = 0
        ans = []
        mask = (1 << maximumBit) - 1

        for num in nums:
            prefix_xor ^= num
            ans.append(prefix_xor ^ mask)

        return ans[::-1]
