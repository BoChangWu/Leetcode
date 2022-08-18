class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if len(nums) == 0 :
            return 0 
        if len(nums) ==1 : 
            if nums[0] == target:
                return 1
            else:
                return 0 
        sum = 0 
        left = 0 
        ans = len(nums)
        flag = False
        for right,val in enumerate(nums):
            sum = sum + val
            while sum >= target:
                sum = sum - nums[left]
                if ans >= (right-left+1):
                    flag = True
                    ans = right - left +1 
                left = left + 1   
        if flag: 
            return ans
        else : 
            return 0