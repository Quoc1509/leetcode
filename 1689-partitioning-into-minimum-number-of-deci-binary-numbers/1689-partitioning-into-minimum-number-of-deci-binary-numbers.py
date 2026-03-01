class Solution:
    def minPartitions(self, n: str) -> int:
        count = 0
        for num in n:
            if count < int(num):
                count += (int(num) - count)
        return count