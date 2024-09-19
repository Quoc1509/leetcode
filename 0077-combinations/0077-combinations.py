class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def dfs(i, path):
            if len(path) == k:
                print(path)
                res.append(path[:])
                return
            if i > n: return
            dfs(i+1, path)
            dfs(i+1, path+[i])

        dfs(1, [])
        return res
