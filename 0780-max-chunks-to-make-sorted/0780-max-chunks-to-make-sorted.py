class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        res = 0
        count = 0
        total = 0
        for i in range(len(arr)):
            total += arr[i]
            count += i
            if count == total:
                res += 1
                count = 0
                total = 0
        return res