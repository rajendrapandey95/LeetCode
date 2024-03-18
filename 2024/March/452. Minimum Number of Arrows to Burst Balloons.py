class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0
        
        points.sort(key=lambda x: x[1])  # Sort by end points
        
        arrows = 1
        end = points[0][1]
        
        for balloon in points[1:]:
            if balloon[0] > end:  # If the start of the next balloon is beyond current end
                arrows += 1
                end = balloon[1]  # Update end point
            else:
                end = min(end, balloon[1])  # Update end point
                
        return arrows
