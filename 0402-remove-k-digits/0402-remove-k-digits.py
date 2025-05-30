class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for n in num:
            while stack and stack[-1] > n and k > 0:
                stack.pop()
                k -= 1

            stack.append(n)
        while stack and k > 0:
            stack.pop()
            k -= 1
        i = 0
        while i < len(stack) and stack[i] == '0':
            i += 1
        if not stack[i:]: 
            return '0'
        return ''.join(stack[i:])