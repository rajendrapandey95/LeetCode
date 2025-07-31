from typing import List

class Solution:
    def subarrayBitwiseORs(self, A: List[int]) -> int:
        ans, cur = set(), {0}
        for x in A:
            cur = {x | y for y in cur} | {x}
            ans |= cur
        return len(ans)
