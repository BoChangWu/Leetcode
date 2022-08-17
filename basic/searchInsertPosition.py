def searchInsert(self, nums: List[int], target: int) -> int:
        for i in nums:
            if target <= i:
                return nums.index(i)
            elif target > i:
                continue
        return len(nums)