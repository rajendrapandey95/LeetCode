import math
from typing import List

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        freq = {rank: ranks.count(rank) for rank in set(ranks)}
        low, high = 1, min(ranks) * cars * cars

        while low < high:
            mid = (low + high) // 2
            if sum(freq[r] * int(math.sqrt(mid // r)) for r in freq) >= cars:
                high = mid
            else:
                low = mid + 1

        return low
