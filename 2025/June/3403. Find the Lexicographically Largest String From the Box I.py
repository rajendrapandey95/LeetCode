class Solution:
    def answerString(self, word: str, k: int) -> str:
        if k == 1: return word
        n, ans = len(word), ""
        for i in range(n):
            ans = max(ans, word[i:i + n - k + 1])
        return ans
