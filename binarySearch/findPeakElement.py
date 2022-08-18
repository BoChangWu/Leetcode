class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        s= list(nums)
        s.sort()
        
        return nums.index(s[-1])