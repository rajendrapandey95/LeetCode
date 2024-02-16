from typing import List
from collections import Counter

class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        frequency = Counter(arr)
        
        sorted_freq = sorted(frequency.values())
        
        num_unique = len(sorted_freq)
        for freq in sorted_freq:
            if k >= freq:
                k -= freq
                num_unique -= 1
            else:
                break
        
        # Step 4: Return the number of remaining unique integers
        return num_unique
