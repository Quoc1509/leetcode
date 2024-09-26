class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        res = []
        N = len(candidates)
        def backTracking(path, i, total):
            if total == target: 
                res.append(path[:])
                return
            if total > target: return
                
            for j in range(i,N):
                if j > i and candidates[j] == candidates[j-1]:
                    continue
                backTracking(path+[candidates[j]], j+1, total + candidates[j])
        backTracking([], 0, 0)
        return res 