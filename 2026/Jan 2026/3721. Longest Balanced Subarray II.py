class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        from collections import defaultdict, deque

        n = len(nums)
        occ = defaultdict(deque)
        pre = [0] * n

        pre[0] = 1 if nums[0] % 2 == 0 else -1
        occ[nums[0]].append(1)

        for i in range(1, n):
            pre[i] = pre[i - 1]
            q = occ[nums[i]]
            if not q:
                pre[i] += 1 if nums[i] % 2 == 0 else -1
            q.append(i + 1)

        seg = SegmentTree(pre)
        ans = 0

        for i in range(n):
            res = seg.find_last(i + ans, 0)
            if res != -1:
                ans = max(ans, res - i)

            occ[nums[i]].popleft()
            nxt = occ[nums[i]][0] if occ[nums[i]] else n + 1
            seg.add(i + 1, nxt - 1, -1 if nums[i] % 2 else 1)

        return ans
