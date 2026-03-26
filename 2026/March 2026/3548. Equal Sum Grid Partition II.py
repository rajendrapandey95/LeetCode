class Solution:
    def canPartitionGrid(self, g):
        tot=sum(map(sum,g))

        for _ in range(4):
            m,n=len(g),len(g[0])
            if m<2:
                g=self.rot(g); continue

            s=0
            seen={0}

            if n==1:
                for i in range(m-1):
                    s+=g[i][0]
                    t=2*s-tot
                    if t==0 or t==g[0][0] or t==g[i][0]:
                        return True
                g=self.rot(g); continue

            for i in range(m-1):
                for v in g[i]:
                    seen.add(v)
                    s+=v

                t=2*s-tot
                if i==0:
                    if t==0 or t==g[0][0] or t==g[0][-1]:
                        return True
                elif t in seen:
                    return True

            g=self.rot(g)

        return False

    def rot(self, g):
        return [list(row) for row in zip(*g[::-1])]
