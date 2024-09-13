class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        N = len(grid)
        zero = []
        for i in range(N):
            count = 0
            for j in range(N-1, -1, -1):
                if grid[i][j] == 0:
                    count += 1
                else:
                    break
            zero.append(count)
        temp = sorted(zero, reverse=True)
        # print(zero)
        for i in range(N):
            if temp[i] < N-i-1:
                return -1

        res = 0

        for i in range(N):
            if zero[i] >= N-i-1: continue
            j = i+1
            while j < N and zero[j] < N-i-1:
                j += 1
            while j > i:
                zero[j], zero[j-1] = zero[j-1], zero[j]
                j -= 1
                res += 1

        return res