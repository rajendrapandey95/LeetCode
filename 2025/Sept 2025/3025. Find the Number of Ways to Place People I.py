class Solution:
    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x:(x[0],-x[1]))
        ans=n=len(points)
        for i in range(n):
            maxy=points[i][1]
            for j in range(i+1,n):
                if points[j][1]<=maxy: ans+=1
                maxy=max(maxy,points[j][1])
        return ans-n
