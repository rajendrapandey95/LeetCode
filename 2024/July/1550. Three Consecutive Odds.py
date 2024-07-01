from typing import List

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        odd_count = 0
        
        for number in arr:
            if number % 2 == 1:
                odd_count += 1
            else:
                odd_count = 0
            
            if odd_count == 3:
                return True
                
        return False
