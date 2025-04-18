class Solution:
    def countAndSay(self, n: int) -> str:
        res = "1"
        
        for i in range(n-1):
            j = 0
            temp = ""
            while j < len(res):
                k = j + 1
                while k < len(res) and res[k] == res[j]:
                    k += 1
                num = k-j
                temp += str(num) + res[j]
                j = k
            res = temp
        return res
