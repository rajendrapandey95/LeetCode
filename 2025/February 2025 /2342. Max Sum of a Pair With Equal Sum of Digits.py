import heapq

class Solution:
    def calculate_digit_sum(self, num):
        return sum(int(digit) for digit in str(num))

    def maximumSum(self, nums):
        digit_sum_groups = {} 
        max_pair_sum = -1

        for number in nums:
            digit_sum = self.calculate_digit_sum(number)

            if digit_sum not in digit_sum_groups:
                digit_sum_groups[digit_sum] = []

            heapq.heappush(digit_sum_groups[digit_sum], number)

            if len(digit_sum_groups[digit_sum]) > 2:
                heapq.heappop(digit_sum_groups[digit_sum])

        for numbers in digit_sum_groups.values():
            if len(numbers) == 2:
                max_pair_sum = max(max_pair_sum, sum(numbers))

        return max_pair_sum
