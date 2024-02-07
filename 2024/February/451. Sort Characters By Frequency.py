from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        # Count the frequency of each character
        char_freq = Counter(s)
        
        # Sort the characters based on their frequencies in decreasing order
        sorted_chars = sorted(char_freq.keys(), key=lambda x: char_freq[x], reverse=True)
        
        # Construct the sorted string
        sorted_string = ''.join([char * char_freq[char] for char in sorted_chars])
        
        return sorted_string
