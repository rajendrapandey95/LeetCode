from typing import List

class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort() 
        n = len(deck)
        result = []

        for i in range(n):
            if result:  
                
                result.insert(0, result.pop())
            
            result.insert(0, deck.pop())

        return result
