class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res = min(heights) * len(heights)
        heights.append(0)
        stack = []
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                ind = stack.pop()
                res = max(res, heights[ind]*(i-1-(stack[-1] if stack else -1)))
            stack.append(i)
        return res
