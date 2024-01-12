class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        def count_vowels(string: str) -> int:
            vowels = set("aeiouAEIOU")
            count = 0
            for char in string:
                if char in vowels:
                    count += 1
            return count
        
        n = len(s)
        mid = n // 2
        
        # Count vowels in the first half (a) and the second half (b)
        count_a = count_vowels(s[:mid])
        count_b = count_vowels(s[mid:])
        
        # Check if the counts are equal
        return count_a == count_b
