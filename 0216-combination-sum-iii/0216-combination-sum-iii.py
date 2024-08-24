class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        A = [1,2,3,4,5,6,7,8,9]
        res = []

        def backTracking(total, i, r, path):
            if total == n and r == 0:
                res.append(path[:])
                return
            if total > n or r < 0 or i == len(A): return
            backTracking(total, i+1, r, path)
            backTracking(total + A[i], i+1, r-1, path+[A[i]])

        backTracking(0, 0, k, [])
        return res         