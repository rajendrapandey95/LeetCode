from collections import deque

class Solution:
    def minSwaps(self, s: str) -> int:
        unbalanced = 0
        for ch in s:
            if ch == "[":
                unbalanced += 1
            elif unbalanced:
                unbalanced -= 1
        return (unbalanced + 1) // 2
