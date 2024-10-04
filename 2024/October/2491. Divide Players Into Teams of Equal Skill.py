class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        n, total_chem = len(skill), 0
        target = skill[0] + skill[-1]
        
        for i in range(n // 2):
            if skill[i] + skill[n - i - 1] != target:
                return -1
            total_chem += skill[i] * skill[n - i - 1]
        
        return total_chem
