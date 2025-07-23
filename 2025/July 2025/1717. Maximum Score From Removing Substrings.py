class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        high, high_val = ("ab", x) if x >= y else ("ba", y)
        low, low_val = ("ba", y) if high == "ab" else ("ab", x)

        score_high, s = self._remove_pairs(s, high, high_val)
        score_low, _ = self._remove_pairs(s, low, low_val)
        
        return score_high + score_low

    def _remove_pairs(self, s: str, pair: str, points: int):
        stack, count = [], 0
        for ch in s:
            if stack and stack[-1] == pair[0] and ch == pair[1]:
                stack.pop()
                count += 1
            else:
                stack.append(ch)
        return count * points, "".join(stack)
