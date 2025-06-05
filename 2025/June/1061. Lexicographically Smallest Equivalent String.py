from typing import List

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = list(range(26))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                if px < py: parent[py] = px
                else: parent[px] = py

        for a, b in zip(s1, s2):
            union(ord(a)-97, ord(b)-97)

        return ''.join(chr(find(ord(c)-97)+97) for c in baseStr)
