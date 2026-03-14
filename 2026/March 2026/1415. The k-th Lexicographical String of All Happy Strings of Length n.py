class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        if k > 3 * (1 << (n-1)):
            return ""

        k -= 1
        res, prev = [], ""

        for i in range(n):
            block = 1 << (n-i-1)
            choices = [c for c in "abc" if c != prev]

            c = choices[k // block]
            res.append(c)
            prev = c
            k %= block

        return "".join(res)
