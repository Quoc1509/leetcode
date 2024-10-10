class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = []
        res = 0
        for i, e in enumerate(nums):
            if not stack or stack[-1][0] > e:
                stack.append((e, i))
            else:
                count = 0
                for j in range(len(stack)-1, -1, -1):
                    if stack[j][0] > e:
                        break
                    count = max(count, i - stack[j][1])
                res = max(res, count)
        return res
