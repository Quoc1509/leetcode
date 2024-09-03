class Solution:
    def getLucky(self, s: str, k: int) -> int:
        string = ''
        for i in s:
            temp = str(abs(ord(i)-ord('a'))+1)
            string += temp
        # print(string)
        res = 0
        for _ in range(k):
            res = 0
            for i in string:
                res +=int(i)
            string = str(res)
        return res