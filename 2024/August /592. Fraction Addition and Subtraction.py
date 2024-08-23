import re

class Solution:
    def fractionAddition(self, exp: str) -> str:
        n, d = 0, 1
        terms = re.split("/|(?=[-+])", exp)
        terms = filter(None, terms)

        for i in range(0, len(terms), 2):
            cn, cd = int(terms[i]), int(terms[i + 1])
            n = n * cd + cn * d
            d *= cd

        gcd = abs(self._gcd(n, d))
        return f"{n // gcd}/{d // gcd}"

    def _gcd(self, a: int, b: int) -> int:
        return b if a == 0 else self._gcd(b % a, a)
