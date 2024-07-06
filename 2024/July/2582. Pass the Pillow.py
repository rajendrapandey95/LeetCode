class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        pos = 1
        t = 0
        dir = 1
        while t < time:
            if 0 < pos + dir <= n:
                pos += dir
                t += 1
            else:
                dir *= -1  # Reverse direction
        return pos
