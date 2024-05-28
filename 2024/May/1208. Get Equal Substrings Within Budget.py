class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        start = 0
        max_len = 0
        current_cost = 0
        
        for end in range(len(s)):
            # Add the cost of the current character transformation
            current_cost += abs(ord(s[end]) - ord(t[end]))
            
            # While the cost exceeds maxCost, shrink the window from the start
            while current_cost > maxCost:
                current_cost -= abs(ord(s[start]) - ord(t[start]))
                start += 1
            
            # Update the maximum length of the valid window
            max_len = max(max_len, end - start + 1)
        
        return max_len
