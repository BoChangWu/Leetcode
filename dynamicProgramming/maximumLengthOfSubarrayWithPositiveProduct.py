class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        n = len(nums)
        last_neg_index= None
        last_zero_index = -1

        ans = 0
        cur_prod = 1

        for i in range(n):

            cur_prod *= nums[i]

            if cur_prod>0: ans = max(ans, i-last_zero_index)

            elif cur_prod<0:

                #check for previous neg_index
                if last_neg_index != None:
                    ans = max(ans, i-last_neg_index)
                else:
                    last_neg_index = i

            else:
                #zero
                last_zero_index= i

                cur_prod = 1
                last_neg_index = None

        return ans