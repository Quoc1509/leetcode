N = (10**6)
Prime = [True] * (N+1)
Prime[0] = Prime[1] = False
for i in range(2, int((math.sqrt(N)) + 1)):
    if Prime[i]:
        for j in range(i*i, N+1, i):
            Prime[j] = False

class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        distance = inf
        res = [-1, -1]
        pre = -inf
        for i in range(left, right+1):
            if Prime[i]:
                if i - pre < distance:
                    distance = i-pre
                    res = [pre, i]
                pre = i
                
                
        return res
                