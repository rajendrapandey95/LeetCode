class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        odd, even, count, mod = 0, 1, 0, int(1e9 + 7)
        prefix_sum = 0

        for num in arr:
            prefix_sum += num
            if prefix_sum % 2:
                count += even
                odd += 1
            else:
                count += odd
                even += 1

        return count % mod
