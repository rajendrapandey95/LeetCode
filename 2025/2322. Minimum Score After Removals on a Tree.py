from typing import List

class Solution:
    def calc(self, part1: int, part2: int, part3: int) -> int:
        return max(part1, part2, part3) - min(part1, part2, part3)

    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        n = len(nums)
        g = [[] for _ in range(n)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        total = 0
        for x in nums:
            total ^= x

        res = float("inf")

        # DFS for second cut
        def dfs2(x: int, parent: int, oth: int, anc: int) -> int:
            xor_val = nums[x]
            for nei in g[x]:
                if nei == parent:
                    continue
                xor_val ^= dfs2(nei, x, oth, anc)
            if parent != anc:
                nonlocal res
                res = min(res, self.calc(oth, xor_val, total ^ oth ^ xor_val))
            return xor_val

        # DFS for first cut
        def dfs(x: int, parent: int) -> int:
            xor_val = nums[x]
            for nei in g[x]:
                if nei == parent:
                    continue
                xor_val ^= dfs(nei, x)
            for nei in g[x]:
                if nei != parent:
                    dfs2(nei, x, xor_val, x)
            return xor_val

        dfs(0, -1)
        return res
