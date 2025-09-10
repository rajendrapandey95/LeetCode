class Solution:
    def minimumTeachings(self, n: int, languages: List[List[int]], friendships: List[List[int]]) -> int:
        cn=set()
        for u,v in friendships:
            if not (set(languages[u-1])&set(languages[v-1])):
                cn|={u-1,v-1}
        cnt=[0]*(n+1)
        for i in cn:
            for l in languages[i]: cnt[l]+=1
        return len(cn)-max(cnt)
