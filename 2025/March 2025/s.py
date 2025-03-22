class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        left = total = 0
        freq = [0] * 3 

        for right, c in enumerate(s):
            freq[ord(c) - ord("a")] += 1

            while all(freq):
                total += len(s) - right
                freq[ord(s[left]) - ord("a")] -= 1
                left += 1

        return total
