class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3: return False
        left = [nums[0]] * len(nums)
        for i in range(1, len(nums)):
            left[i] = min(left[i-1], nums[i])
        stack = []
        for i in range(len(nums)-1, 0, -1):
            while stack and stack[-1] < nums[i]:
                num = stack.pop()
                if num > left[i-1]:
                    return True
            stack.append(nums[i])
        return False