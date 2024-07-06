class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        count = time // (n-1)
        time = time % (n-1)
        if count % 2 == 0:
            return time + 1
        else:
            return n - time