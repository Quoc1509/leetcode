class Solution:
    def numDecodings(self, s: str) -> int:
        res = [0]
        N = len(s)
        memo = {}
        def dfs(index):
            if index == N:
                return 1
            if index > N:
                return 0
            if index in memo: return memo[index]
            one, two = 0, 0
            if s[index] != "0":
                one = dfs(index+1)
            if s[index] != "0" and int(s[index: index+2]) <= 26:
                two = dfs(index+2)
            memo[index] = (one + two)
            return memo[index]
        
        return dfs(0)
