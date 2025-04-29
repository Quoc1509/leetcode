class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res = [-1] * len(nums)
        length = len(nums)
        nums = nums + nums
        stack = []
        for i in range(len(nums)):
            while stack and nums[stack[-1]] < nums[i]:
                idx = stack.pop()
                res[idx%length] = nums[i]
            stack.append(i)
        return res