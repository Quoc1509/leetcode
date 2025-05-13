A = [
    [0,0,0,0,1,0,1,0,0,0],
    [0,0,0,0,0,0,1,0,1,0],
    [0,0,0,0,0,0,0,1,0,1],
    [0,0,0,0,1,0,0,0,1,0],
    [1,0,0,1,0,0,0,0,0,1],
    [0,0,0,0,0,0,0,0,0,0],
    [1,1,0,0,0,0,0,1,0,0],
    [0,0,1,0,0,0,1,0,0,0],
    [0,1,0,1,0,0,0,0,0,0],
    [0,0,1,0,1,0,0,0,0,0]
]
mod = 10**9+7
def mul(A, B):
    res = [[0] * len(B[0]) for _ in range(len(A))]

    for i in range(len(A)):
        for j in range(len(B[0])):
            temp = 0
            for k in range((len(B))):
                temp += A[i][k] * B[k][j]
            res[i][j] = temp % mod
    return res

def pow(x, n):
    if n == 1:
        return x
    res = pow(x, n//2)
    if n % 2 == 1:
        return mul(mul(res, res), x)
    return mul(res, res)

class Solution:
    def knightDialer(self, n: int) -> int:
        if n == 1:
            return 10
        B = [[1] * 10]
        res =  mul(B, pow(A, n-1))
        print(res)
        return sum(res[0]) % mod 
