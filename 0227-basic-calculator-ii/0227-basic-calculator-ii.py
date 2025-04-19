class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        i = 0
        def getNumber(i):
            j = i + 1
            while j < len(s) and (s[j].isdigit() or s[j] == " "):
                j += 1
            stack.append(int(s[i:j].strip()))
            return j
        while i < len(s):
            if s[i] == '+' or s[i] == ' ':
                i += 1
                continue
            if s[i].isdigit() or s[i] == '-':
                i = getNumber(i)
            else:
                num1 = stack.pop()
                j = getNumber(i+1)
                num2 = stack.pop()
                if s[i] == '*':
                    stack.append(num1*num2)
                elif s[i] == '/':
                    temp1 = abs(num1)
                    temp2 = abs(num2)
                    num = temp1//temp2
                    if num1*num2 < 0:
                        num = -num
                    stack.append(num)
                i = j
        return sum(stack)
        
