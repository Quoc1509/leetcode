class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        N = len(candidates)
        res = []

        def backTracking(index, path, total):
            if total == target: 
                res.append(path[:])
                return
            if total > target: return

            for i in range(index, len(candidates)):
                backTracking(i, path+[candidates[i]], total + candidates[i])
        backTracking(0, [], 0)
        return res
        