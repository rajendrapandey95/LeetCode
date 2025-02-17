from typing import List
from itertools import permutations

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        return len(set("".join(p) for i in range(1, len(tiles) + 1) for p in permutations(tiles, i)))
