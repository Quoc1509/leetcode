class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        if len(s) < k: return s
        stack = []
        i = 0
        while i < len(s):
            j = i+1
            while j < len(s) and s[i] == s[j]:
                j += 1
            if stack and stack[-1][0] == s[i]:
                stack[-1][1] += j-i
            else:
                stack.append([s[i], j-i])
            if stack:
                stack[-1][1] %= k
                if stack[-1][1] == 0:
                    stack.pop()
            i = j
        res = ''
        for a, b in stack:
            res += a*b
        return res