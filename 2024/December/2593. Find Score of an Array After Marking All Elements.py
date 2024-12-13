class Solution:
    def findScore(self, nums: list[int]) -> int:
        n = len(nums)
        marked = [False] * n
        score = 0

        sorted_nums = sorted((value, idx) for idx, value in enumerate(nums))

        for value, idx in sorted_nums:
            if not marked[idx]:
                score += value
                marked[idx] = True
                if idx > 0:
                    marked[idx - 1] = True
                if idx < n - 1:
                    marked[idx + 1] = True

        return score
