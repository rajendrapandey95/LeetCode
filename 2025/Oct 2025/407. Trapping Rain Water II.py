import heapq

class Solution:
    def trapRainWater(self, h):
        m,n=len(h),len(h[0])
        v=[[0]*n for _ in range(m)]
        pq=[]
        for i in range(m):
            for j in (0,n-1):
                heapq.heappush(pq,(h[i][j],i,j));v[i][j]=1
        for j in range(n):
            for i in (0,m-1):
                if not v[i][j]:
                    heapq.heappush(pq,(h[i][j],i,j));v[i][j]=1
        w=0
        while pq:
            ht,x,y=heapq.heappop(pq)
            for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
                nx,ny=x+dx,y+dy
                if 0<=nx<m and 0<=ny<n and not v[nx][ny]:
                    v[nx][ny]=1
                    nh=h[nx][ny]
                    w+=max(0,ht-nh)
                    heapq.heappush(pq,(max(ht,nh),nx,ny))
        return w
