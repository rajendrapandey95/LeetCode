from typing import List

class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        n = len(s)

        left = [[0, 0, 0] for _ in range(n)]
        num, mask, count = 0, 0, 0
        for i in range(n - 1):
            bit = 1 << (ord(s[i]) - ord("a"))
            if not (mask & bit):
                count += 1
                if count <= k:
                    mask |= bit
                else:
                    num += 1
                    mask = bit
                    count = 1
            left[i + 1] = [num, mask, count]

    
        right = [[0, 0, 0] for _ in range(n)]
        num, mask, count = 0, 0, 0
        for i in range(n - 1, 0, -1):
            bit = 1 << (ord(s[i]) - ord("a"))
            if not (mask & bit):
                count += 1
                if count <= k:
                    mask |= bit
                else:
                    num += 1
                    mask = bit
                    count = 1
            right[i - 1] = [num, mask, count]

        max_val = 1
        for i in range(n):
            seg = left[i][0] + right[i][0] + 2
            tot_mask = left[i][1] | right[i][1]
            tot_count = bin(tot_mask).count("1")

            if tot_count < k:
                seg += 1

            if tot_count <= k:
                seg = max(seg, left[i][0] + right[i][0] + 1)

            max_val = max(max_val, seg)

        return max_val
