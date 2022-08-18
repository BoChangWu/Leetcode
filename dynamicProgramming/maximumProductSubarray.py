class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mx=mn=res=nums[0]
        for i in range(1,len(nums)):
            x=max(nums[i],mx*nums[i],mn*nums[i])
            y=min(nums[i],mx*nums[i],mn*nums[i])
            mx,mn=x,y
            res=max(res,mx)
        return res