class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:

        frequencies = {}
        for num in nums:
            if num in frequencies:
                frequencies[num] += 1
            else:
                frequencies[num] = 1

        max_frequency = 0
        for frequency in frequencies.values():
            max_frequency = max(max_frequency, frequency)

        frequency_of_max_frequency = 0
        for frequency in frequencies.values():
            if frequency == max_frequency:
                frequency_of_max_frequency += 1

        return frequency_of_max_frequency * max_frequency
