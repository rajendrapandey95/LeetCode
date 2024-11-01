class Solution:
    def makeFancyString(self, s: str) -> str:
        ans, freq = s[0], 1
        for i in range(1, len(s)):
            freq = freq + 1 if s[i] == s[i - 1] else 1
            if freq < 3:
                ans += s[i]
        return ans
