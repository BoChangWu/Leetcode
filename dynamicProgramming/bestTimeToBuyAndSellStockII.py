class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0 #Buy
        right = 1 #Sell

        ans=[]
        while right < len(prices):
            currentProfit = prices[right] - prices[left] #our current Profit
            if currentProfit>0:
                ans.append(currentProfit)
            left+=1
            right+=1
        
        return sum(ans)