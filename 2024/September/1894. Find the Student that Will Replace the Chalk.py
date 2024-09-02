class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        n = len(chalk)

        prefix_sum = [0] * n
        prefix_sum[0] = chalk[0]
        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i - 1] + chalk[i]

        total_chalk = prefix_sum[-1]
        remaining_chalk = k % total_chalk

        return self._find_student(prefix_sum, remaining_chalk)

    def _find_student(self, arr: List[int], target: int) -> int:
        low, high = 0, len(arr) - 1

        while low < high:
            mid = (low + high) // 2

            if arr[mid] <= target:
                low = mid + 1
            else:
                high = mid

        return high
