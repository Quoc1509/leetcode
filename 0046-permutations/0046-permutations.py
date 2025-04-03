class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(visit, path):
            if len(path) == len(nums):
                res.append(path[:])
                return
            for i in range(len(nums)):
                if (1<<i)&visit:
                    continue
                dfs(visit|(1<<i), path+[nums[i]])
        dfs(0, [])
        return res