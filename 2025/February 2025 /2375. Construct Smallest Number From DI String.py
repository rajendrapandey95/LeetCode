from itertools import permutations

class Solution:
    def smallestNumber(self, pattern: str) -> str:
        stack, result = [], ""
        
        for i, ch in enumerate(pattern + "I", 1):  
            stack.append(str(i))
            if ch == "I":
                result += "".join(stack[::-1])  
                stack = []
        
        return result
