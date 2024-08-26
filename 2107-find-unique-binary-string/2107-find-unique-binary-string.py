class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        N = len(nums)
        res = set()
        def dfs(s):
            if len(s) == N:
                res.add(s)
                return
        
            dfs(s+'0')
            dfs(s+'1')
        dfs('')
        for i in nums:
            res.remove(i)
        return list(res)[0]