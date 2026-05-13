class Solution:
    def minMoves(self, nums: List[int], limit: int) -> int:
        n = len(nums)
        d = [0] * (2 * limit + 2)

        for i in range(n // 2):
            a, b = sorted((nums[i], nums[~i]))

            d[2] += 2
            d[a + 1] -= 1
            d[a + b] -= 1
            d[a + b + 1] += 1
            d[b + limit + 1] += 1

        s = ans = n
        for i in range(2, 2 * limit + 1):
            s += d[i]
            ans = min(ans, s)

        return ans
