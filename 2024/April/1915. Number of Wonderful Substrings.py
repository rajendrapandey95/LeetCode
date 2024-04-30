class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        count = [0] * 1024  

        result = 0
        bitmask = 0 

        
        count[0] = 1

        for char in word:
            
            bitmask ^= 1 << (ord(char) - ord('a'))

           
            result += count[bitmask]

            
            for i in range(10):
                result += count[bitmask ^ (1 << i)]

            
            count[bitmask] += 1

        return result
