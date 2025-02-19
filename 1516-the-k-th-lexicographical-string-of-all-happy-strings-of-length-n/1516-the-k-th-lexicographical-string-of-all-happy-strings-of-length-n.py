class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        res = ['']
        c = ['a', 'b', 'c']
        count = [k]
        def BT(s):
            
            if len(s) == n:
                count[0] -= 1
                if count[0] == 0:
                    res[0] = s
                    return True
                return False
            for i in range(len(c)):
                if len(s) == 0:
                    if BT(c[i]):
                        return True
                else:
                    if c[i] != s[-1]:
                        # if len(s) == n-1:
                        #     count[0] -= 1
                        if BT(s+c[i]):
                            return True
            return False
        BT('')
        return res[0]
                