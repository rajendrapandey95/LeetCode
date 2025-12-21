class Solution:
    def minDeletionSize(self, strs):
        ok = [True] * (len(strs) - 1)
        ans = 0

        for c in range(len(strs[0])):
            if any(ok[i] and strs[i][c] > strs[i+1][c] for i in range(len(ok))):
                ans += 1
            else:
                for i in range(len(ok)):
                    ok[i] &= strs[i][c] == strs[i+1][c]

        return ans
