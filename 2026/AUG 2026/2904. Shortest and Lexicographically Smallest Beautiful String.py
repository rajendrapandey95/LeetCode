class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        ans = ""
        n = len(s)

        for i in range(n):

            oneCnt = 0
            cur = ""

            for j in range(i, n):

                cur += s[j]

                if s[j] == '1':
                    oneCnt += 1

                if oneCnt > k:
                    break

                if oneCnt == k:
                    if ans == "" or len(cur) < len(ans) or (len(cur) == len(ans) and cur < ans):
                        ans = cur

        return ans
