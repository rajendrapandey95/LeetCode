from typing import List
from collections import deque

class Solution:
    def maxCandies(self, status: List[int], candies: List[int], keys: List[List[int]], boxes: List[List[int]], init: List[int]) -> int:
        n = len(status)
        openable = [s == 1 for s in status]
        has, used = [0]*n, [0]*n
        q, ans = deque(), 0
        for b in init:
            has[b] = 1
            if openable[b]:
                q.append(b)
                used[b] = 1
                ans += candies[b]
        while q:
            b = q.popleft()
            for k in keys[b]:
                openable[k] = 1
                if has[k] and not used[k]:
                    q.append(k)
                    used[k] = 1
                    ans += candies[k]
            for x in boxes[b]:
                has[x] = 1
                if openable[x] and not used[x]:
                    q.append(x)
                    used[x] = 1
                    ans += candies[x]
        return ans
