N = 5*10**6
A = [True]*(N+1)
A[0] = A[1] = False
for i in range(2, int(sqrt(N))+1):
    if A[i]:
        for j in range(i*i, N+1, i):
            A[j] = False
class Solution:
    def countPrimes(self, n: int) -> int:
        res = 0
        for i in range(2, n):
            if A[i]:
                res += 1
        return res