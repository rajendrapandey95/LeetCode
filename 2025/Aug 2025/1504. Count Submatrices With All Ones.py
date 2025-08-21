class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        heights = [0] * n
        ans = 0

        for i in range(m):
            for j in range(n):
                heights[j] = heights[j] + 1 if mat[i][j] else 0

            stack = []
            sum_sub = [0] * n
            for j in range(n):
                while stack and heights[stack[-1]] >= heights[j]:
                    stack.pop()
                if stack:
                    prev = stack[-1]
                    sum_sub[j] = sum_sub[prev] + heights[j] * (j - prev)
                else:
                    sum_sub[j] = heights[j] * (j + 1)
                ans += sum_sub[j]
                stack.append(j)

        return ans
