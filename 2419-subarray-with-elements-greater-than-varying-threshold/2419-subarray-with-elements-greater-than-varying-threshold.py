class Solution:
    def validSubarraySize(self, nums: List[int], threshold: int) -> int:
        nums.append(-inf)
        stack = []
        res = -inf
        for i in range(len(nums)):
            while stack and nums[stack[-1]] >= nums[i]:
                ind = stack.pop()
                if  nums[ind] > threshold/(i-(stack[-1]+1 if stack else 0)):
                    return i-(stack[-1]+1 if stack else 0)
                    # res = max(res, i-(stack[-1]+1 if stack else 0))
            stack.append(i)
        
        return res if res != -inf else -1
