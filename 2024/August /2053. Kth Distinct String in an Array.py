from typing import List

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        freq = {}
        for s in arr:
            if s in freq:
                freq[s] += 1
            else:
                freq[s] = 1
        
        distinct_strings = [s for s in arr if freq[s] == 1]
        
        if len(distinct_strings) < k:
            return ""
        
        return distinct_strings[k - 1]
