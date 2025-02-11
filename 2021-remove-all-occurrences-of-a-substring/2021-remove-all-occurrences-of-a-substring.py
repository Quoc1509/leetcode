class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        N = len(part)
        for c in s:
            stack.append(c)
            if len(stack) >= N:
                temp = ''.join(stack[len(stack)-N:])
                if temp == part:
                    for _ in range(N):
                        stack.pop()
        # print(stack)
        return ''.join(stack)
                    
