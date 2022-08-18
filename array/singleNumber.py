class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        
        n = list(set(nums))
        
        for i in range(len(nums)):
            if nums.index(nums[i]) != i:
                n.remove(nums[i])
                
        return n[0]