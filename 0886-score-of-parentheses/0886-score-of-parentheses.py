class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        for c in s:
            if c == "(":
                stack.append(0)
            else:
                d = stack.pop()
                d = max(1, d)
                stack[-1] += 2*d
        return stack[0]//2