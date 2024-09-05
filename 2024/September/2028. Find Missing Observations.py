class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        total = mean * (n + len(rolls)) - sum(rolls)
        if total < n or total > 6 * n: return []
        avg, mod = divmod(total, n)
        return [avg + 1] * mod + [avg] * (n - mod)
