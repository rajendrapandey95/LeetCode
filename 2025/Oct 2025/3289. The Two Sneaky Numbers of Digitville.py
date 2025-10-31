class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        res = []
        freq = {}

        for x in nums:
            freq[x] = freq.get(x, 0) + 1
            if freq[x] == 2:
                res.append(x)

        return res
