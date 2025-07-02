class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        mod, n, cnt = 10**9 + 7, len(word), 1
        freq = []

        for i in range(1, n):
            cnt += word[i] == word[i - 1]
            if word[i] != word[i - 1]:
                freq.append(cnt)
                cnt = 1
        freq.append(cnt)

        ans = 1
        for f in freq:
            ans = ans * f % mod

        if len(freq) >= k:
            return ans

        f, g = [1] + [0] * (k - 1), [1] * k
        for c in freq:
            fn = [0] * k
            for j in range(1, k):
                fn[j] = g[j - 1]
                if j - c - 1 >= 0:
                    fn[j] = (fn[j] - g[j - c - 1]) % mod
            g = [fn[0]] + [0] * (k - 1)
            for j in range(1, k):
                g[j] = (g[j - 1] + fn[j]) % mod
            f = fn
        return (ans - g[k - 1]) % mod
