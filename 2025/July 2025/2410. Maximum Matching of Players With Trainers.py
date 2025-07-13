class Solution:
    def matchPlayersAndTrainers(self, p: list[int], t: list[int]) -> int:
        p.sort(), t.sort()
        i = j = cnt = 0
        while i < len(p) and j < len(t):
            if p[i] <= t[j]:
                cnt += 1
                i += 1
            j += 1
        return cnt
