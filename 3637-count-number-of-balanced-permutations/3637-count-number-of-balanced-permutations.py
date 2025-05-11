mod = 10**9+7
def pow(x, n, m):
    res = 1
    a = x
    while n > 0:
        if n & 1:
            res = (res*a) % m
        a = (a * a) % m 
        n >>= 1
    return res
    
fact = [0] * 81
fact[0] = 1
for i in range(1, 81):
    fact[i] = fact[i-1] * i % mod 

in_fact = [0] * 81
in_fact[0] = 1
in_fact[80] = pow(fact[80], mod-2, mod) 
for i in range(79, 0, -1):
    in_fact[i] = (i+1) * in_fact[i+1] % mod

class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        N = len(num)
        total = sum(int(i) for i in num)
        if total % 2 == 1:
            return 0
        total //= 2
        odd = len(num)//2
        count = [0] * 10
        for i in num:
            count[int(i)] += 1
            
        @cache
        def dfs(n, c, s):
            if c < 0 or s > total:
                return 0
            if n == -1:
                if c == 0 and s == total:
                    return (fact[odd] * fact[N-odd])%mod
                return 0
            res = 0
            for no in range(count[n]+1):
                res = (res + dfs(n-1, c-no, s + no*n) * in_fact[no] * in_fact[count[n]-no]) % mod
            return res
        return dfs(9, odd, 0)
             