class Solution:
    def combinationSum(self,candidates:List[int], target:int)-> List[List[int]]:
        res = []
        candidates.sort()
        def getPossibleSums(candidates, target, res, op = []):
            if target == 0:
                res.append(op)
                return

            if target < 0:
                return

            for i in range(len(candidates)):
                if(candidates[i] > target):
                    break
                getPossibleSums(candidates[i:],target - candidates[i],
                                res,op + [candidates[i]])
            
        getPossibleSums(candidates,target, res)
        return res