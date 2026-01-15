class Solution:
    def maximizeSquareHoleArea(
        self, n: int, m: int, hBars: List[int], vBars: List[int]
    ) -> int:

        def longest_consecutive(arr):
            arr.sort()
            best = cur = 1
            for i in range(1, len(arr)):
                cur = cur + 1 if arr[i] == arr[i - 1] + 1 else 1
                best = max(best, cur)
            return best

        side = min(longest_consecutive(hBars), longest_consecutive(vBars)) + 1
        return side * side
