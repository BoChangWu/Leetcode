class Solution:
    def nearestValidPoint(self, x, y, points):
        result, minDist = -1, float('inf')
        for i in range(len(points)):
            if points[i][0]==x or points[i][1]==y:
                currDist = abs(points[i][0]-x)+abs(points[i][1]-y)
                if currDist<minDist:
                    result, minDist = i, currDist
        return result