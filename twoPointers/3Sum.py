class Solution:
    
    
    def two_sum(self, nums, target: int):
        candidates = []
        new_nums = {}
        for num in nums:
            if num not in new_nums:
                new_nums[num] = 1
            else:
                new_nums[num] +=1
        
        for num in new_nums:
            new_target = target - num
            
            if new_target in new_nums:
                if new_target == num and new_nums[num] < 2:
                    continue
                candidates.append([new_target, num])
        
        if candidates == []:
            return None
        return candidates
                
                
        
    
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        seen = set()
        for idx_num, num in enumerate(nums):
            if num in seen:
                continue
            seen.add(num)
            target = 0 - num
            sol = self.two_sum(nums[:idx_num]+nums[idx_num+1:], target)
            
            if sol is None:
                continue
        
            for s in sol:
                res.append([num]+s)
        
        
        res = ['|'.join([str(e) for e in sorted(elem)]) for elem in res]
        res = set(res)
        new_res = []
        for elem in res:
            seq = elem.split("|")
            temp = []
            for char in seq:
                temp.append(int(char))
            new_res.append(temp)
        
        
        return new_res