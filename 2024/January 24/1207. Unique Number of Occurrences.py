from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        freq_dict = {}
        
        for num in arr:
            freq_dict[num] = freq_dict.get(num, 0) + 1
        
        occurrences_set = set(freq_dict.values())
        return len(occurrences_set) == len(freq_dict)
