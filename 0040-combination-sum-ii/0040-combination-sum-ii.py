class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        res = []
        N = len(candidates)
        def backTracking(path, i, total):
            if total == target: 
                res.append(path[:])
                return
            if total > target or i == N: return
            t = i+1
            while t < N and candidates[t] == candidates[i]:
                t += 1
                
            backTracking(path, t, total)
            backTracking(path + [candidates[i]], i+1, total + candidates[i])
        backTracking([], 0, 0)
        return res 