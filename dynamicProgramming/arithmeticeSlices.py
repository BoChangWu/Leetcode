class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        if len(nums) < 3:
            return 0
        
        diff =  float('inf') 
        ap_arrays = cur_length = 0
        
        for index in range(1, len(nums)):
            if nums[index] - nums[index-1] == diff:
                cur_length += 1
            else:
                diff = nums[index] - nums[index-1]
                cur_length = 2
            
            if cur_length >= 2:
                ap_arrays += (cur_length - 2)
        
        return ap_arrays