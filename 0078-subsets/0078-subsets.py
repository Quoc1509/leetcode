class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backTracking(i, path):
            if i == len(nums):
                res.append(path[:])
                return
            backTracking(i+1, path)
            backTracking(i+1, path + [nums[i]])
        backTracking(0, [])
        return res