class Solution:
    def calculate(self, s: str) -> int:
        operate = []
        nums = []
        num = 0
        def calculate(num1, num2, st):
            if st == '+':
                return (num2+num1)
            elif st == '-':
                return (num2-num1)
            elif st == '*':
                return (num2*num1)
            else:
                return (num2//num1)

        for i in range(len(s)):
            if s[i] == "+" or s[i] == '-' or s[i] == '*' or s[i] == '/':
                if operate and operate[-1] == '*':
                    temp = nums.pop()
                    st = operate.pop()
                    count = calculate(num, temp, st)
                    nums.append(count)
                    
                elif operate and operate[-1] == '/':
                    temp = nums.pop()
                    st = operate.pop()
                    count = calculate(num, temp, st)
                    nums.append(count)
                else:
                    nums.append(num)
                operate.append(s[i])
                num = 0

            elif s[i].isdigit():
                num = num * 10 + int(s[i])
        if operate and (operate[-1] == '*' or operate[-1] == '/'):
            nums.append(calculate(num, nums.pop(), operate.pop()))
        else:
            nums.append(num)
        res = nums[0]
        for i in range(len(operate)):
            res = calculate(nums[i+1], res, operate[i])
        return res
