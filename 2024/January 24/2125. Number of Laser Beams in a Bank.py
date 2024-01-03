from typing import List

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        prev = 0
        ans = 0
        
        for row in bank:
            count = row.count('1')
            if count:
                ans += prev * count
                prev = count
                
        return ans
