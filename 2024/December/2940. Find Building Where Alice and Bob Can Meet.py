class Solution:
    def leftmostBuildingQueries(self, heights, queries):
        def search(height, mono_stack):
            left, right, ans = 0, len(mono_stack) - 1, -1
            while left <= right:
                mid = (left + right) // 2
                if mono_stack[mid][0] > height:
                    ans = max(ans, mid)
                    left = mid + 1
                else:
                    right = mid - 1
            return ans

        result = [-1] * len(queries)
        new_queries = [[] for _ in range(len(heights))]
        for i, (a, b) in enumerate(queries):
            if a > b:
                a, b = b, a
            if heights[b] > heights[a] or a == b:
                result[i] = b
            else:
                new_queries[b].append((heights[a], i))

        mono_stack = []
        for i in range(len(heights) - 1, -1, -1):
            for height, idx in new_queries[i]:
                pos = search(height, mono_stack)
                if 0 <= pos < len(mono_stack):
                    result[idx] = mono_stack[pos][1]
            while mono_stack and mono_stack[-1][0] <= heights[i]:
                mono_stack.pop()
            mono_stack.append((heights[i], i))

        return result
