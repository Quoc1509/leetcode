mod = 10**9+7
@cache
def dfs(c, t):
    if t == 0:
        return 1
    if c < 25:
        return dfs(c + 1, t -1)
    return (dfs(0, t-1) + dfs(1, t-1)) % mod

class Solution:
    def lengthAfterTransformations(self, s: str, t: int) -> int:
        

        res = 0
        for c in s:
            n = ord(c) - ord('a')
            res = (res+dfs(n, t))%mod
        return res