class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []

        def backTracking(total, index, path):
            if total == n and len(path) == k:
                res.append(path[:])
                return
            if total > n : return
            for i in range(index, 10):
                backTracking(total + i, i +1, path+[i])

        backTracking(0, 1, [])
        return res         