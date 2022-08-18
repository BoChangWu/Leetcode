class Solution(object):
	def lengthOfLIS(self, nums):
		"""
		:type nums: List[int]
		:rtype: int
		"""
		hashmap = {}
		
		def dfs(index, count):
			if index in hashmap:
				return count + hashmap[index]
			
			if index == len(nums) -1:
				return count
		
			max_count = 0
			for i in range(index + 1, len(nums)):
				if nums[index] < nums[i]:
					max_count = max(max_count, dfs(i, count + 1))

			return max_count

		for i in range(len(nums)-1, -1, -1):
			hashmap[i] = dfs(i, 0)
		
		return max(hashmap.values()) + 1