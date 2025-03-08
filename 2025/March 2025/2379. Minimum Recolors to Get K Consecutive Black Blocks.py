from collections import deque

class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        q, w = deque(blocks[:k]), blocks[:k].count("W")
        res = w
        for i in range(k, len(blocks)):
            if q.popleft() == "W": w -= 1
            if blocks[i] == "W": w += 1
            q.append(blocks[i])
            res = min(res, w)
        return res
