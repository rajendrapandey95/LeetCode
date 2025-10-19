from collections import deque

class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:
        seen = set()
        q = deque([s])
        res = s
        n = len(s)

        while q:
            cur = q.popleft()
            if cur in seen:
                continue
            seen.add(cur)
            res = min(res, cur)

            chars = list(cur)
            for i in range(1, n, 2):
                chars[i] = str((int(chars[i]) + a) % 10)
            q.append("".join(chars))

            q.append(cur[-b:] + cur[:-b])

        return res
