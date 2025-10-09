class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        skill.sort()
        mana.sort()

        total = 0
        for s, m in zip(skill, mana):
            total += s * m

        return total
