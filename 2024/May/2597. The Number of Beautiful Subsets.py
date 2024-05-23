from typing import List
from collections import defaultdict

class Solution:
    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        total_count = 1
        freq_map = defaultdict(lambda: defaultdict(int))

        for x in nums:
            freq_map[x % k][x] += 1

        for fr in freq_map.values():
            subsets = sorted(fr.items())
            total_count *= self._count_beautiful_subsets(subsets, len(subsets), k, 0)

        return total_count - 1

    def _count_beautiful_subsets(self, subsets, num_subsets, difference, i):
        if i == num_subsets:
            return 1

        skip = self._count_beautiful_subsets(subsets, num_subsets, difference, i + 1)
        take = (1 << subsets[i][1]) - 1

        if i + 1 < num_subsets and subsets[i + 1][0] - subsets[i][0] == difference:
            take *= self._count_beautiful_subsets(subsets, num_subsets, difference, i + 2)
        else:
            take *= self._count_beautiful_subsets(subsets, num_subsets, difference, i + 1)

        return skip + take
