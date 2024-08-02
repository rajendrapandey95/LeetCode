class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        return min(self.min_swaps_helper(nums, 0), self.min_swaps_helper(nums, 1))

    def min_swaps_helper(self, data: List[int], val: int) -> int:
        total_val_count = data.count(val)
        if total_val_count == 0 or total_val_count == len(data):
            return 0

        current_val_in_window = sum(1 for i in range(total_val_count) if data[i] == val)
        max_val_in_window = current_val_in_window

        for i in range(total_val_count, len(data)):
            current_val_in_window += data[i] == val
            current_val_in_window -= data[i - total_val_count] == val
            max_val_in_window = max(max_val_in_window, current_val_in_window)

        return total_val_count - max_val_in_window
