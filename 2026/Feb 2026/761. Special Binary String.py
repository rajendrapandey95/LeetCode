class Solution:
    def makeLargestSpecial(self, s: str) -> str:
        cnt = i = 0
        parts = []

        for j, ch in enumerate(s):
            cnt += 1 if ch == '1' else -1
            if cnt == 0:
                parts.append('1' + self.makeLargestSpecial(s[i+1:j]) + '0')
                i = j + 1

        parts.sort(reverse=True)
        return ''.join(parts)
