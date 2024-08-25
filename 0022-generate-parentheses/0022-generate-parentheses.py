class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(s, o, c):
            if o == n and c == n:
                res.append(s)
                return
            if o > n or c > n: return
            if o > c:
                dfs(s+")", o, c+1)
            
            dfs(s+"(", o+1, c)
        dfs('', 0, 0)
        return res
