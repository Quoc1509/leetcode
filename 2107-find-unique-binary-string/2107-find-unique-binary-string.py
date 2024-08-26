class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        temp = set(nums)
        N = len(nums)
        def dfs(s):
            if len(s) == N:
                if s not in temp:        
                    return s
                return None

            a = dfs(s+'0')
            if a: return a
            b = dfs(s+'1')
            if b: return b
            return None
        res = dfs('')
        return res if res else ''