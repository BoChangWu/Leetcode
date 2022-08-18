def roo(i,nums,dp):
    if(i>=len(nums)):
        return 0
    if(dp[i]!=-1):
        return dp[i]
    dp[i]=max(nums[i]+roo(i+2,nums,dp) , roo(i+1,nums,dp))
    return dp[i]

class Solution:   
    def rob(self, nums: List[int]) -> int:
        dp=[-1]*len(nums)
        fs= nums[0]+roo(0,nums[2:-1],dp)
        dp=[-1]*len(nums)
        ss=roo(0,nums[1:],dp)
        return max(fs,ss)