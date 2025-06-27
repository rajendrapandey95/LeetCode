from collections import Counter, deque

class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        ans = ""
        chars = sorted([c for c, v in Counter(s).items() if v >= k], reverse=True)
        q = deque(chars)
        while q:
            cur = q.popleft()
            if len(cur) > len(ans): ans = cur
            for c in chars:
                nxt = cur + c
                it = iter(s)
                if all(ch in it for ch in nxt * k):
                    q.append(nxt)
        return ans
