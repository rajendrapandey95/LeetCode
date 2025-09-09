from collections import deque

class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        MOD=10**9+7
        know,share=deque([(1,1)]),deque()
        kc,sc=1,0
        for i in range(2,n+1):
            if know and know[0][0]==i-delay:
                kc-=know[0][1]; sc+=know[0][1]; share.append(know.popleft())
            if share and share[0][0]==i-forget:
                sc-=share[0][1]; share.popleft()
            if sc: kc+=sc; know.append((i,sc))
        return (kc+sc)%MOD
