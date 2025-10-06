import heapq
class Solution:
    def swimInWater(self, g: list[list[int]]) -> int:
        m,n=len(g),len(g[0]);pq=[(g[0][0],0,0)];v=set()
        while pq:
            t,x,y=heapq.heappop(pq)
            if (x,y)in v:continue
            if (x,y)==(m-1,n-1):return t
            v.add((x,y))
            for dx,dy in((1,0),(-1,0),(0,1),(0,-1)):
                nx,ny=x+dx,y+dy
                if 0<=nx<m and 0<=ny<n and (nx,ny)not in v:
                    heapq.heappush(pq,(max(t,g[nx][ny]),nx,ny))
