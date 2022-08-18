class Solution(object):
    def checkStraightLine(self, Points):
      
        def slope(p1, p2):
            run = p2[0] - p1[0]
           
            if run == 0: return float('inf')

            rise = 1.0*(p2[1] - p1[1])
            return rise/run

        slope01 = slope(Points[0],Points[1])
        return all([slope01 == slope(Points[0], p) for p in Points[2:]])