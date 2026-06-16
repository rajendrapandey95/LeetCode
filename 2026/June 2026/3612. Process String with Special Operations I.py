class Solution:
    def processStr(self, s: str) -> str:
        res = []
        n = len(s)

        for i in range(n):
            ch = s[i]

            if ch == '*':
                if len(res) != 0:
                    res.pop()
            elif ch == '#':
                res.extend(res)
            elif ch == '%':
                res.reverse()
            elif 'a' <= ch <= 'z':
                res.append(ch)

        return ''.join(res)
