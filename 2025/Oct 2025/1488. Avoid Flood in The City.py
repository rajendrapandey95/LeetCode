from sortedcontainers import SortedList
class Solution:
    def avoidFlood(self, r: list[int]) -> list[int]:
        a=[1]*len(r);s=SortedList();m={}
        for i,x in enumerate(r):
            if x==0:s.add(i)
            else:
                a[i]=-1
                if x in m:
                    j=s.bisect(m[x])
                    if j==len(s):return []
                    a[s[j]]=x;s.remove(s[j])
                m[x]=i
        return a
