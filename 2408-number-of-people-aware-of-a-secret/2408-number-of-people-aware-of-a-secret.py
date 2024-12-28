class Solution:
    def peopleAwareOfSecret(self, n: int, delay: int, forget: int) -> int:
        N = 10**9+7
        res = [0] * n
        res[0] = 1
        for i in range(n):
            index = i+delay
            while index < i+forget and index < n:
                res[index] += res[i]
                index += 1
        return sum(res[n-forget:])%N
