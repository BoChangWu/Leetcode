class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0 
        right = len(nums) - 1
        while left<=right:
            pivot = int(left + (right-left)/2)
            if target == nums[pivot]:
                return pivot
            
            elif target > nums[pivot]:
                left = pivot + 1
                continue
            elif target < nums[pivot]:
                right = pivot - 1
                continue
        return -1