class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        def backTracking(total, index):
            
            if total == target: return [[]]
            if total > target: return None
            
            res = []
            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i - 1]:
                    continue
                temp =  backTracking(total+candidates[i], i+1)

                if temp is not None:
                    for j in temp:
                        cur = j
                        cur.append(candidates[i])
                        res.append(cur)
                    
            return res
        return backTracking(0, 0)

