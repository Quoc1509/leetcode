class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        temp = set(nums)
        N = len(nums)
        res = ['']
        def dfs(s):
            if len(s) == N:
                if s not in temp: 
                    res[0] = s
                return
        
            dfs(s+'0')
            dfs(s+'1')
        dfs('')
        return res[0]