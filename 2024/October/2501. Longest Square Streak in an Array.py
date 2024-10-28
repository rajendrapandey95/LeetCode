from typing import List

class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        nums.sort()
        processed = set()
        longest_streak = 0

        for num in nums:
            if num in processed:
                continue

            streak, streak_len = num, 1

            while streak * streak <= 10**5:
                if self._binary_search(nums, streak * streak):
                    streak *= streak
                    processed.add(streak)
                    streak_len += 1
                else:
                    break

            longest_streak = max(longest_streak, streak_len)

        return longest_streak if longest_streak >= 2 else -1

    def _binary_search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
