from typing import List

class Solution:
    def can_distribute(self, x: int, quantities: List[int], n: int) -> bool:
        j, remaining = 0, quantities[0]
        for _ in range(n):
            if remaining <= x:
                j += 1
                if j == len(quantities):
                    return True
                remaining = quantities[j]
            else:
                remaining -= x
        return False

    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        left, right = 0, max(quantities)
        while left < right:
            middle = (left + right) // 2
            if self.can_distribute(middle, quantities, n):
                right = middle
            else:
                left = middle + 1
        return left
