class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        vowelMask = {"a": 1, "e": 2, "i": 4, "o": 8, "u": 16}  
        prefixXOR, longestSubstring = 0, 0
        mp = [-1] * 32  
        mp[0] = 0  

        for i, ch in enumerate(s, 1): 
            prefixXOR ^= vowelMask.get(ch, 0)  
            if mp[prefixXOR] == -1:  
                mp[prefixXOR] = i
            longestSubstring = max(longestSubstring, i - mp[prefixXOR])  

        return longestSubstring
