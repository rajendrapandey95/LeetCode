class Solution:
    def longestCommonPrefix(self, arr1, arr2):
        prefixes = set()

        for val in arr1:
            while val > 0:
                prefixes.add(val)
                val //= 10

        longest = 0
        for val in arr2:
            while val > 0 and val not in prefixes:
                val //= 10
            if val > 0:
                longest = max(longest, len(str(val)))

        return longest
