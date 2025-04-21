class Solution:
    def numberOfArrays(self, differences: List[int], lower: int, upper: int) -> int:
        min_prefix_sum = max_prefix_sum = current = 0

        for d in differences:
            current += d
            min_prefix_sum = min(min_prefix_sum, current)
            max_prefix_sum = max(max_prefix_sum, current)

            if max_prefix_sum - min_prefix_sum > upper - lower:
                return 0

        return (upper - lower) - (max_prefix_sum - min_prefix_sum) + 1
