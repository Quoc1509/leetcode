class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        maxOr = [0]
        for num in nums:
            maxOr[0] |= num

        res = [0]
        def dfs(curOr, ind):

            if curOr == maxOr[0]:
                res[0] += 1
            for i in range(ind, len(nums)):
                dfs(curOr | nums[i], i+1)
        dfs(0, 0)
        return res[0]