class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        ans = 0
        for letter in set(s):
            i, j = s.find(letter), s.rfind(letter)
            if j > i + 1:
                ans += len(set(s[i + 1:j]))
        return ans
