class Solution:
    def __init__(self):
        self.HASH_MULTIPLIER = 60001

    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obs = {x + self.HASH_MULTIPLIER * y for x, y in obstacles}
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        x, y, max_dist, d = 0, 0, 0, 0

        for cmd in commands:
            if cmd == -1:
                d = (d + 1) % 4
            elif cmd == -2:
                d = (d + 3) % 4
            else:
                dx, dy = dirs[d]
                for _ in range(cmd):
                    nx, ny = x + dx, y + dy
                    if nx + self.HASH_MULTIPLIER * ny in obs:
                        break
                    x, y = nx, ny
                max_dist = max(max_dist, x * x + y * y)
        
        return max_dist
