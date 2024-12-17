from collections import Counter
from heapq import heappush, heappop, heapify

class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        max_heap = [(-ord(char), count) for char, count in Counter(s).items()]
        heapify(max_heap)
        result = []

        while max_heap:
            char_neg, count = heappop(max_heap)
            char = chr(-char_neg)
            use = min(count, repeatLimit)
            result.append(char * use)
            if count > use:
                if max_heap:
                    next_char_neg, next_count = heappop(max_heap)
                    result.append(chr(-next_char_neg))
                    if next_count > 1:
                        heappush(max_heap, (next_char_neg, next_count - 1))
                heappush(max_heap, (char_neg, count - use))

        return "".join(result)
