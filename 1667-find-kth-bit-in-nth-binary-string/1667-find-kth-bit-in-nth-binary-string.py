class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        s = '0'
        def inv(st):          
            sr = ''
            for i in range(len(st)-1, -1, -1):
                if st[i] == '0':
                    sr += '1'
                else:
                    sr += '0'
            return sr

        while len(s) <= k and n > 0:
            temp = inv(s)
            # print('---', temp)
            s = s + '1' + temp
            n -= 1
            # print(s)
        return s[k-1]