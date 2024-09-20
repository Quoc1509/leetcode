N = (10**6)
Prime = [True] * (N+1)
Prime[0] = Prime[1] = False
for i in range(2, int((math.sqrt(N)) + 1)):
    if Prime[i]:
        for j in range(i*i, N+1, i):
            Prime[j] = False


class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        res= [-1, -1]
        temp, minNum = 0, inf
        for k in range(left, right+1):
            if Prime[k]:
                if temp != 0:
                    if k - temp < minNum:
                        res = [temp, k]
                        minNum = (k - temp)
                temp = k
        return res
                        

                
