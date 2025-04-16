class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        if not s:
            return 0

        res = []
        stack = []
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                j = stack.pop()
                num = 0
                while res and j < res[-1][0]:
                    k, n = res.pop()
                    num += n
                if num > 0:
                    res.append((j, 2*num)) 
                else:
                    res.append((j, 1))
        total = 0
        for a, b in res:
            total += b
        return total