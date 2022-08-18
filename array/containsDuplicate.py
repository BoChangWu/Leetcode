class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        n = list(set(nums))
        n.sort()
        if nums!=n:
            return True
        return False