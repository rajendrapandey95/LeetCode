class Solution:
    def getWordsInLongestSubsequence(self, words, groups):
        n = len(words)
        dp = [1] * n
        pre = [-1] * n
        best = 0

        def check(a, b):
            return len(a) == len(b) and sum(x != y for x, y in zip(a, b)) == 1

        for i in range(n):
            for j in range(i):
                if check(words[i], words[j]) and groups[i] != groups[j] and dp[j] + 1 > dp[i]:
                    dp[i], pre[i] = dp[j] + 1, j
            if dp[i] > dp[best]: best = i

        res = []
        while best != -1:
            res.append(words[best])
            best = pre[best]
        return res[::-1]
