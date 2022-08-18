class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # This solution uses a pivot pointer
        n = len(prices)
        # keep track of min left and max right
        min_left, max_right = [], []
        min_left_temp, max_right_temp = math.inf, -math.inf
        ans = 0
        for i in range(n):
            min_left_temp = min(min_left_temp, prices[i])
            min_left.append(min_left_temp)
            max_right_temp = max(max_right_temp, prices[n-i-1])
            max_right.append(max_right_temp)
        
        max_right = max_right[::-1]
        
        for i in range(n):
            ans = max(ans, max_right[i]-min_left[i])
            
        return(ans)