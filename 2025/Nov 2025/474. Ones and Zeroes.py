class Solution:
    def findMaxForm(self, strs, m, n):
        dp = {(0,0):0}
        for s in strs:
            z = s.count('0'); o = len(s)-z
            add = {}
            for (cz, co), v in dp.items():
                nz, no = cz+z, co+o
                if nz<=m and no<=n:
                    add[(nz,no)] = max(add.get((nz,no),0), v+1)
            dp.update(add)
        return max(dp.values())
