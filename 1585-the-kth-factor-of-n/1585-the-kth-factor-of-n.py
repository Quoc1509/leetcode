class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        first = []
        N = int(sqrt(n))
        for i in range(1, N+1):
            if n % i == 0:
                first.append(i)
        if k <= len(first):
            return first[k-1]
        if N * N == n:
            k += 1
        if k > 2 * len(first):
            return -1
        k -= len(first)
        k = len(first) - k
        k += 1
        return n // first[k-1]