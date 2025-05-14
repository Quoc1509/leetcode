mod = 10**9+7
def mul(A, B):
    res = [[0] * len(B[0]) for _ in range(len(A))]
    
    for i in range(len(A)):
        for j in range(len(B[0])):
            temp = 0
            for k in range(len(B)):
                temp += A[i][k] * B[k][j]
            res[i][j] = temp % mod
    return res

def pow(x, n, mod):
    if n == 1:
        return x
    res = pow(x, n//2, mod)
    if n % 2 == 1:
        return mul(mul(res, res), x)
    return mul(res, res)

class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: List[int]) -> int:
        A = [[0] * 26 for _ in range(26)]
        B = [[0] * 26]
        for i in range(len(nums)):
            for j in range(nums[i]):
                A[i][(i+1+j)%26] += 1
        for c in s:
            i = ord(c) - ord('a')
            B[0][i] += 1
        res = mul(B, pow(A, t, mod))
        ans = sum(res[0])
        return ans % mod