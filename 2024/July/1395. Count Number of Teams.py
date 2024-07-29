class Solution:
    def numTeams(self, r: List[int]) -> int:
        n = len(r)
        t = 0
        inc = [[0] * 4 for _ in range(n)]
        dec = [[0] * 4 for _ in range(n)]
        for i in range(n):
            inc[i][1] = 1
            dec[i][1] = 1
        for cnt in range(2, 4):
            for i in range(n):
                for j in range(i + 1, n):
                    if r[j] > r[i]:
                        inc[j][cnt] += inc[i][cnt - 1]
                    if r[j] < r[i]:
                        dec[j][cnt] += dec[i][cnt - 1]
        for i in range(n):
            t += inc[i][3] + dec[i][3]
        return t
