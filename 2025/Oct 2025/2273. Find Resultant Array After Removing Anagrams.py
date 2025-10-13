from typing import List
from collections import Counter

class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        res=[words[0]]
        for w in words[1:]:
            if Counter(w)!=Counter(res[-1]):
                res.append(w)
        return res
