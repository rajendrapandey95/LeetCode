class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        open_br, min_adds = 0, 0
        for c in s:
            if c == "(": open_br += 1
            elif open_br: open_br -= 1
            else: min_adds += 1
        return min_adds + open_br
