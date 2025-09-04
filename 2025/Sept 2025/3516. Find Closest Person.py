class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        dx,dy=abs(x-z),abs(y-z)
        return 1 if dx<dy else 2 if dx>dy else 0
