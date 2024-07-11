class Solution:
    def reverseParentheses(self, s: str) -> str:
        idx = deque()
        res = []

        for c in s:
            if (c == "("):
                idx.append(len(res))
            elif (c == ")"):
                start = idx.pop()
                res[start:] = res[start:][::-1]
            else:
                res.append(c)
                
        return "".join(res)
