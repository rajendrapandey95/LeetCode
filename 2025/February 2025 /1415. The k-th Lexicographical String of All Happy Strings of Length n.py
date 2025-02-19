class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        from itertools import product

        happy_strings = sorted(
            "".join(seq) for seq in product("abc", repeat=n) if all(seq[i] != seq[i+1] for i in range(n-1))
        )

        return happy_strings[k-1] if k <= len(happy_strings) else ""
