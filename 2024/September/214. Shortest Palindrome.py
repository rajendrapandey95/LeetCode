class Solution:
    def shortestPalindrome(self, s: str) -> str:
        reversed_string = s[::-1]  
        length = len(s)

        for i in range(length):
            if s[: length - i] == reversed_string[i:]:
                return reversed_string[:i] + s
        return ""
