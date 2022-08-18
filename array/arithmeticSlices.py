class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        def num_ways(len):
            return (len - 2) * (len - 1) // 2
            
        result = 0
        prev_delta = float("inf")
        cur_len = 0
        for i in range(1, len(nums)):
            delta = nums[i] - nums[i - 1]
            if delta == prev_delta:
                cur_len += 1
            else:
                if cur_len >= 3:
                    result += num_ways(cur_len)
                cur_len = 2
                prev_delta = delta
        if cur_len >= 3:
            result += num_ways(cur_len)

        return result