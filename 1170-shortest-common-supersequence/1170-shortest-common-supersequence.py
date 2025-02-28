class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        memo = [[-1 for _ in range(len(str2) + 1)] for _ in range(len(str1) + 1)]
        def dp(i1, i2):
            if memo[i1][i2] != -1: 
                return memo[i1][i2]
            if i1 >= len(str1) and i2 >= len(str2):
                return 0
            elif i1 >= len(str1):
                return len(str2[i2:])
            elif i2 >= len(str2):
                return len(str1[i1:])

            
            res = 0 
            if str1[i1] == str2[i2]:
                res = 1+dp(i1+1, i2+1)
            else:
                one = 1 + dp(i1+1, i2)
                two = 1 + dp(i1, i2+1)
                res = one if one < two else two
            memo[i1][i2] = res
            return res
        dp(0, 0)
        i1, i2 = 0, 0
        res = ''
        while i1 < len(str1) and i2 < len(str2):
            if str1[i1] == str2[i2]:
                res += str1[i1]
                i1 += 1
                i2 += 1
            elif dp(i1+1, i2) < dp(i1, i2+1):
                res += str1[i1]
                i1 += 1
            else:
                res += str2[i2]
                i2 += 1
        if i1 < len(str1):
            res += str1[i1:]
        if i2 < len(str2):
            res += str2[i2:]
        return res