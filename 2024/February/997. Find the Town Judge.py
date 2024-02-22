from typing import List

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # Initialize arrays to keep track of trust counts and trusted counts
        trust_count = [0] * (n + 1)
        trusted_count = [0] * (n + 1)
        
        # Iterate through the trust array and update counts
        for a, b in trust:
            trust_count[a] += 1
            trusted_count[b] += 1
        
        # Check for the town judge
        for i in range(1, n + 1):
            if trust_count[i] == 0 and trusted_count[i] == n - 1:
                return i
        
        # If no town judge found
        return -1
