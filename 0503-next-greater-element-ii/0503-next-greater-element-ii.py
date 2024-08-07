class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        res = [-1] * len(nums)
        length = len(nums)
        stack = []
        nums = nums + nums
        for i in range(len(nums)):
            if not stack: 
                stack.append(i)
                continue
            while stack and nums[stack[-1]] < nums[i]:
                res[stack[-1]%length] = nums[i]
                stack.pop()
            stack.append(i)     
           
        return res