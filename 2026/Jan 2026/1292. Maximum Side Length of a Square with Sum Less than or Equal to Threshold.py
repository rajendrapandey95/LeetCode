class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])
        ps = [[0]*(n+1) for _ in range(m+1)]

        for i in range(m):
            for j in range(n):
                ps[i+1][j+1] = ps[i][j+1] + ps[i+1][j] - ps[i][j] + mat[i][j]

        def ok(k):
            for i in range(k, m+1):
                for j in range(k, n+1):
                    if ps[i][j] - ps[i-k][j] - ps[i][j-k] + ps[i-k][j-k] <= threshold:
                        return True
            return False

        lo, hi, ans = 1, min(m, n), 0
        while lo <= hi:
            mid = (lo + hi) // 2
            if ok(mid):
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        return ans
