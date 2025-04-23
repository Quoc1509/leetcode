class Solution:
    def candy(self, arr: List[int]) -> int:
        N = len(arr)
        left = [1] * N
        for i in range(1, N):
            if arr[i] > arr[i-1]:
                left[i] = left[i-1] + 1
        
        for i in range(N-2, -1, -1):
            if arr[i] > arr[i+1]:
                left[i] = max(left[i+1]+1, left[i])
        res = 0
        return sum(left)