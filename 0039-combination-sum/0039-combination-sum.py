class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        N = len(candidates)
        res = []

        def backTracking(index, path, total):
            if total > target: return
            if total == target: res.append(path[:])

            for i in range(index, N):
                backTracking(i, path+[candidates[i]], total + candidates[i])
        backTracking(0, [], 0)
        return res
        