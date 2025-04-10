from functools import cache

class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        low, high = str(start), str(finish)
        n = len(high)
        low = low.zfill(n)  
        pre_len = n - len(s)  

        @cache
        def dfs(i: int, is_low_bound: bool, is_high_bound: bool) -> int:
            if i == n:
                return 1  # Found a valid number

            lo = int(low[i]) if is_low_bound else 0
            hi = int(high[i]) if is_high_bound else 9
            res = 0

            if i < pre_len:
                for digit in range(lo, min(hi, limit) + 1):
                    res += dfs(
                        i + 1,
                        is_low_bound and digit == lo,
                        is_high_bound and digit == hi
                    )
            else:
                x = int(s[i - pre_len])
                if lo <= x <= min(hi, limit):
                    res += dfs(
                        i + 1,
                        is_low_bound and x == lo,
                        is_high_bound and x == hi
                    )

            return res

        return dfs(0, True, True)
