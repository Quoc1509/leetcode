class Solution:
    def largestPalindrome(self, n: int, k: int) -> str:    
        res = [''] * n
        
        po = [0] * n
        mo = 1
        for i in range(n):    
            po[i] = mo
            mo = (mo*10)%k
            
        @cache
        def dp(i, mod):
            if i > (n-1)//2:
                return mod == 0
            mi = -1 if i > 0 else 0
            for num in range(9, mi, -1):
                if i == n-i-1:
                    nmod = (mod + (num*po[i])%k ) % k
                else:
                    nmod = (mod + (num*po[i])%k + (num*po[n-i-1])%k ) % k
                if dp(i+1, nmod):
                    res[i] = str(num)
                    res[n-i-1] = str(num)
                    return True
            return False
        dp(0, 0)
        return ''.join(res)
