class Solution:
    def closestTarget(self, words, target, startIndex):
        n = len(words)
        ans = float('inf')

        for i in range(n):
            if words[i] == target:
                clockwise = (i - startIndex + n) % n
                anticlockwise = (startIndex - i + n) % n
                ans = min(ans, min(clockwise, anticlockwise))

        return -1 if ans == float('inf') else ans
