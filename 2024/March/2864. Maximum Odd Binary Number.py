class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        # Get n and ones_cnt
        n = len(s)
        ones_cnt = s.count('1')

        # Construct the resulting string
        return '1' * (ones_cnt - 1) + '0' * (n - ones_cnt) + '1'
