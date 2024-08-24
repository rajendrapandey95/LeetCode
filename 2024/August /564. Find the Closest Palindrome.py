class Solution:
    def nearestPalindromic(self, n: str) -> str:
        ln = len(n)
        mid = ln // 2 - 1 if ln % 2 == 0 else ln // 2
        fh = int(n[:mid + 1])

        cands = [
            self.to_palindrome(fh, ln % 2 == 0),
            self.to_palindrome(fh + 1, ln % 2 == 0),
            self.to_palindrome(fh - 1, ln % 2 == 0),
            10 ** (ln - 1) - 1,
            10 ** ln + 1
        ]

        diff = float("inf")
        res = 0
        num = int(n)
        
        for c in cands:
            if c == num:
                continue
            if abs(c - num) < diff:
                diff = abs(c - num)
                res = c
            elif abs(c - num) == diff:
                res = min(res, c)
                
        return str(res)

    def to_palindrome(self, left: int, even: bool) -> int:
        p = left
        if not even:
            left //= 10
        while left > 0:
            p = p * 10 + left % 10
            left //= 10
        return p
