class Solution:
    def maximizeSquareArea(
        self, m: int, n: int, hFences: List[int], vFences: List[int]
    ) -> int:
        MOD = 10**9 + 7

        def max_consecutive(arr):
            arr.sort()
            cur = best = 1
            for i in range(1, len(arr)):
                if arr[i] == arr[i - 1] + 1:
                    cur += 1
                else:
                    cur = 1
                best = max(best, cur)
            return best + 1

        max_h = max_consecutive(hFences)
        max_v = max_consecutive(vFences)

        side = min(max_h, max_v)
        return (side * side) % MOD
