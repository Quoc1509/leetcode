class Solution:
    def maximumSwap(self, num: int) -> int:
        res = num
        num = str(num)
        
        for i in range(len(num)-1):
            for j in range(i+1, len(num)):
                if int(num[i]) < int(num[j]):

                    temp = num[:i] + num[j] + num[i+1: j] + num[i] + num[j+1:]
                    # print(num[i], num[j], temp)
                    res = max(res, int(temp))
                    
        print(res)
        return res