from collections import Counter
import heapq

class Solution:
    def minimumPushes(self, word: str) -> int:
        freq_map = Counter(word)
        freq_queue = [-freq for freq in freq_map.values()]
        heapq.heapify(freq_queue)

        total_pushes = 0
        idx = 0

        while freq_queue:
            total_pushes += (1 + (idx // 8)) * (-heapq.heappop(freq_queue))
            idx += 1

        return total_pushes
