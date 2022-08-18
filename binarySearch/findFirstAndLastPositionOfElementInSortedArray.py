class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        
        if target not in nums:
            return [-1,-1]
        
        n= []
        
        n.append(nums.index(target))
        nums.reverse()
        a = nums.index(target)
        n.append(len(nums)-1-a)
        
        return n