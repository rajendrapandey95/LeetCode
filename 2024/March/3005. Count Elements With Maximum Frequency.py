class Solution:
    def maxFrequencyElements(self, nums):
        frequencies = {}
        max_frequency = 0
        total_frequencies = 0

        for num in nums:
            frequencies[num] = frequencies.get(num, 0) + 1
            frequency = frequencies[num]

            if frequency > max_frequency:
                max_frequency = frequency
                total_frequencies = frequency
            elif frequency == max_frequency:
                total_frequencies += frequency

        return total_frequencies
