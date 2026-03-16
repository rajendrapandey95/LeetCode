class Solution:
    def getBiggestThree(self, grid):
        m, n = len(grid), len(grid[0])
        st = set()

        for i in range(m):
            for j in range(n):

                st.add(grid[i][j])

                k = 1
                while True:
                    r = i + 2 * k
                    left = j - k
                    right = j + k

                    if r >= m or left < 0 or right >= n:
                        break

                    s = 0
                    x, y = i, j

                    for t in range(k):
                        s += grid[x + t][y + t]

                    for t in range(k):
                        s += grid[x + k + t][y + k - t]

                    for t in range(k):
                        s += grid[x + 2 * k - t][y - t]

                    for t in range(k):
                        s += grid[x + k - t][y - k + t]

                    st.add(s)
                    k += 1

        ans = []
        for v in sorted(st, reverse=True):
            ans.append(v)
            if len(ans) == 3:
                break

        return ans
