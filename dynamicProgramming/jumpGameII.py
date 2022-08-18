class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        index, num, count = 0, nums[0], 0
        while len(nums) != 1:
            count += 1
            lower, upper = index + 1, index + num
            if upper >= len(nums) - 1:
                return count
            num = 0
            for n in range(lower, upper + 1):
                if (nums[n] != 0 or index == len(nums) - 1) and nums[n] + n >= num + index:
                    index = n
                    num = nums[index]
        return count