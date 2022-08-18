class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        i = sys.maxsize
        j = sys.maxsize
        
        for ind in range(len(nums)):
            if nums[ind]<=i:
                i = nums[ind]
            elif nums[ind]<=j:
                j = nums[ind]
            else:
                return True
            
        
        return False