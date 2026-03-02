class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        n = len(grid)
        a = []
        for r in grid:
            c = 0
            for x in r[::-1]:
                if x: break
                c += 1
            a.append(c)

        ans = 0
        for i in range(n):
            j = i
            while j < n and a[j] < n-1-i: j += 1
            if j == n: return -1
            ans += j - i
            while j > i:
                a[j], a[j-1] = a[j-1], a[j]
                j -= 1
        return ans
