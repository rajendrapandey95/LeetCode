class Solution:
    def maximumBeauty(self, items, queries):
        ans = [0] * len(queries)
        items.sort()
        queries_with_indices = sorted((q, i) for i, q in enumerate(queries))

        max_beauty = item_index = 0
        for query, original_index in queries_with_indices:
            while item_index < len(items) and items[item_index][0] <= query:
                max_beauty = max(max_beauty, items[item_index][1])
                item_index += 1
            ans[original_index] = max_beauty

        return ans
