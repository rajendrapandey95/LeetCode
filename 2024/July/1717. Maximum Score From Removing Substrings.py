class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        pts = 0
        s = list(s)

        if x > y:
            pts += self.rm_sub(s, "ab", x)
            pts += self.rm_sub(s, "ba", y)
        else:
            pts += self.rm_sub(s, "ba", y)
            pts += self.rm_sub(s, "ab", x)

        return pts

    def rm_sub(self, s, sub, pts_per_rm):
        pts = 0
        w_idx = 0

        for r_idx in range(len(s)):
            s[w_idx] = s[r_idx]
            w_idx += 1

            if w_idx > 1 and s[w_idx - 2] == sub[0] and s[w_idx - 1] == sub[1]:
                w_idx -= 2
                pts += pts_per_rm

        del s[w_idx:]
        return pts
