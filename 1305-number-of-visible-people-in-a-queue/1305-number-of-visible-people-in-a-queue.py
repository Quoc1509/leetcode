class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        res = [0] * len(heights)
        stack = []
        for i in range(len(heights)-1, -1, -1):
            count = 0
            while stack and heights[stack[-1]] < heights[i]:
                stack.pop()
                count += 1
            if stack:
                res[i] = count + 1
            else:
                res[i] = count
            stack.append(i)
        return res
            