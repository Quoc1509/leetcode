class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []
        temp = [0] * len(s)
        for i, e in enumerate(s):
            if e == '(':
                stack.append(i)
            else:
                if stack:
                    index = stack.pop()
                    temp[i] = 1
                    temp[index] = 1
        res = 0
        count = 0
        for i in range(len(temp)):
            if temp[i] == 0:
                count = 0
            else:
                count += 1
                res = max(res, count)
        return res


