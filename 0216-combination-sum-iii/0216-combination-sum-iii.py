class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []

        def backTracking(total, path, index):
            if len(path) == k and total == n:
                res.append(path[:])
                return
            if len(path) > k or total > n:
                return
            
            for i in range(index, 10):
                backTracking(total + i, path+[i], i+1)
        backTracking(0, [], 1)
        return res