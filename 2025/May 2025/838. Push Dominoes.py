class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        N, force = len(dominoes), [0] * len(dominoes)
        f = 0
        for i in range(N):
            if dominoes[i] == 'R': f = N
            elif dominoes[i] == 'L': f = 0
            else: f = max(f - 1, 0)
            force[i] += f
        f = 0
        for i in reversed(range(N)):
            if dominoes[i] == 'L': f = N
            elif dominoes[i] == 'R': f = 0
            else: f = max(f - 1, 0)
            force[i] -= f
        return ''.join('.' if x == 0 else 'R' if x > 0 else 'L' for x in force)
