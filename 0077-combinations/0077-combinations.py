class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def dfs(i, path):
            if len(path) == k:
                res.append(path[:])
                return
            for j in range(i, n+1):
                dfs(j+1, path+[j])

        dfs(1, [])
        return res
