class Solution:
    def clearStars(self, s: str) -> str:
        pos = [[] for _ in range(26)]
        a = list(s)
        for i, c in enumerate(a):
            if c != "*":
                pos[ord(c)-97].append(i)
            else:
                for j in range(26):
                    if pos[j]:
                        a[pos[j].pop()] = "*"
                        break
        return ''.join(c for c in a if c != "*")
