class Solution:
    def canJump(self, nums: List[int]) -> bool:
        length = len(nums) - 1
        jump_count = 0
        for i in range(length - 1, -1, -1):
            if jump_count + 1 <= nums[i]:
                jump_count = 0
            else:
                jump_count += 1
        return jump_count <= 0