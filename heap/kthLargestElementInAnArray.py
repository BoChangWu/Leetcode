class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        nums.sort()
        # print(n)
        return nums[-k]