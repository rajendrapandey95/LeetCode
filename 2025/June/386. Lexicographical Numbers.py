from typing import List

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []
        def dfs(x):
            if x > n: return
            res.append(x)
            for i in range(10):
                if x*10+i > n: break
                dfs(x*10+i)
        for i in range(1, 10): dfs(i)
        return res
