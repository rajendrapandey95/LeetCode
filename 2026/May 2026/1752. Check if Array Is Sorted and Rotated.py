class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)

        for rotation_offset in range(n):
            check_sorted = []

            for index in range(rotation_offset, n):
                check_sorted.append(nums[index])
            for index in range(rotation_offset):
                check_sorted.append(nums[index])

            is_sorted = True
            for index in range(n - 1):
                if check_sorted[index] > check_sorted[index + 1]:
                    is_sorted = False
                    break

            if is_sorted:
                return True

        return False
