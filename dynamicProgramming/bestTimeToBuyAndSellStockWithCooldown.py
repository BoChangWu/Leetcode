class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        maxProfitForState = [[0,0] for _ in range(len(prices)+2)]
        
        
        for i in range(len(prices)-1,-1,-1):
           
            maxProfitForState[i][0] = max(maxProfitForState[i+1][1]-prices[i], maxProfitForState[i+1][0])
            
           
            maxProfitForState[i][1] = max(maxProfitForState[i+2][0]+prices[i], maxProfitForState[i+1][1])
                
        return maxProfitForState[0][0]