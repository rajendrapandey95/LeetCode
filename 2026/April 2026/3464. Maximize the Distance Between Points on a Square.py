class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        R = L = U = 0
        for ch in moves:
            if ch == 'R':
                R += 1
            elif ch == 'L':
                L += 1
            else:
                U += 1
        return abs(R - L) + U
