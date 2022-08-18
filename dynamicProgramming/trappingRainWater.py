class Solution:
    def trap(self, height: List[int]) -> int:
        ind_maxh = height.index(max(height))
		
		
        h, l = 0, 0
        for i in range(ind_maxh):
            if height[i] > h:
                h = height[i]
            else:
                l += h - height[i]
		
	
        h, r = 0, 0
        for i in range(len(height)-1 , ind_maxh, -1):
            if height[i] > h:
                h = height[i]
            else:
                r += h - height[i]
				
        return l + r