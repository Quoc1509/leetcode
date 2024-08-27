class Solution:
    def partition(self, s: str) -> List[List[str]]:
        N = len(s)
        res = []
        def dfs(st, start):
            if start >= N:
                res.append(st)
                return
            for i in range(start, N):
                temp = s[start:i+1]
                if temp == temp[::-1]:
                    dfs(st+[temp], i+1)
        dfs([], 0)
        return res