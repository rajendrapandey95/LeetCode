class Solution:
    def prefixesDivBy5(self, nums):
        ans = []
        pref = 0
        for b in nums:
            pref = (pref*2 + b) % 5
            ans.append(pref == 0)
        return ans
