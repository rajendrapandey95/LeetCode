class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # Create a dictionary to store the frequency of characters in string s
        freq = {}
        for char in s:
            freq[char] = freq.get(char, 0) + 1
        
        # Construct the permutation according to the order
        permutation = ''
        for char in order:
            if char in freq:
                permutation += char * freq[char]
                freq.pop(char)
        
        # Append remaining characters (if any) to the permutation
        for char, count in freq.items():
            permutation += char * count
        
        return permutation
