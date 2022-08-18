class Solution:
    def majorityElement(self, nums):
        import collections
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)