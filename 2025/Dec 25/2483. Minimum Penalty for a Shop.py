class Solution:
    def bestClosingTime(self, customers: str) -> int:
        best = cur = min_penalty = 0
        
        for i, c in enumerate(customers):
            cur += -1 if c == 'Y' else 1
            if cur < min_penalty:
                min_penalty = cur
                best = i + 1
                
        return best
