from collections import Counter

class Solution:
    def robotWithString(self, s: str) -> str:
        cnt, stk, res, ch = Counter(s), [], [], "a"
        for c in s:
            stk.append(c)
            cnt[c] -= 1
            while ch <= "z" and cnt[ch] == 0:
                ch = chr(ord(ch) + 1)
            while stk and stk[-1] <= ch:
                res.append(stk.pop())
        return ''.join(res)
