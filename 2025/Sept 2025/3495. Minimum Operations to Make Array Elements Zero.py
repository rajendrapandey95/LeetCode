class Solution:
    def get(self, num: int) -> int:
        i,base,cnt=1,1,0
        while base<=num:
            cnt+=((i+1)//2)*(min(base*2-1,num)-base+1)
            i,base=i+1,base*2
        return cnt
    def minOperations(self, queries: List[List[int]]) -> int:
        return sum((self.get(r)-self.get(l-1)+1)//2 for l,r in queries)
