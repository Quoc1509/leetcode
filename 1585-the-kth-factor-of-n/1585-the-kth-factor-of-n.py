class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        first = []
        second = []
        for i in range(1, int(sqrt(n))+1):
            if n % i == 0:
                first.append(i)
                if n//i != i:
                    second.append(n//i)
        print(first, second)
        if k <= len(first):
            return first[k-1]
        elif k-len(first) <= len(second):
            return second[len(second)-(k-len(first))]
        return -1           