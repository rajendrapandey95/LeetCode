class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        def is_unique_from(i):
            return len(set(nums[i:])) == len(nums[i:])

        ans = 0
        for i in range(0, len(nums), 3):
            if is_unique_from(i):
                return ans
            ans += 1
        return ans
