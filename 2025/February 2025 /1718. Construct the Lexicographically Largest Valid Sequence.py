from typing import List

class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        res, used = [0] * (2 * n - 1), [False] * (n + 1)

        def backtrack(i: int) -> bool:
            if i == len(res):
                return True
            if res[i]:
                return backtrack(i + 1)

            for num in range(n, 0, -1):
                if used[num]:
                    continue
                used[num], res[i] = True, num
                if num == 1 or (i + num < len(res) and res[i + num] == 0):
                    if num > 1:
                        res[i + num] = num
                    if backtrack(i + 1):
                        return True
                    if num > 1:
                        res[i + num] = 0
                used[num], res[i] = False, 0
            return False

        backtrack(0)
        return res
