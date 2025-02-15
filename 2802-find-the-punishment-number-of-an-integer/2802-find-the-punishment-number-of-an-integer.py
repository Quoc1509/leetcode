class Solution:
    def punishmentNumber(self, n: int) -> int:
        res = 0
        def backTracking(i, s, no):
            # print(i, s, no)
            if i >= len(s):
                return no == 0
            
            for j in range(i, len(s)):
                if backTracking(j+1, s, no-int(s[i:j+1])):
                    return True
            return False
            
        for num in range(1, n+1):
            if backTracking(0, str(num*num), num):
                res += (num*num)
        
        return res
