class Solution:
    def getLucky(self, s: str, k: int) -> int:
        string = ''
        for i in s:
            temp = str(abs(ord(i)-ord('a'))+1)
            string += temp
        # print(string)
        res = 0
        while k != 0:
            res = 0
            for i in string:
                res +=int(i)
            string = str(res)
            k -= 1
        return res