class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        N = len(candidates)
        res = []

        def backTracking(i, path, total):
            if total == target: 
                res.append(path[:])
                return
            if total > target or i == N: return
            t = i+1
            while t < N and candidates[t] == candidates[i]:
                t += 1
            backTracking(t, path, total)
            backTracking(i, path+[candidates[i]], total + candidates[i])
        backTracking(0, [], 0)
        return res
        