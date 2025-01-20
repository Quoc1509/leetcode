class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        mp = defaultdict(list)
        M, N = len(mat), len(mat[0])
        row = [0] * M
        col = [0] * N
        for i in range(M):
            for j in range(N):
                mp[mat[i][j]].append(i)
                mp[mat[i][j]].append(j)

        for i in range(len(arr)):
            r, c = mp[arr[i]]
            row[r] += 1
            col[c] += 1
            if row[r] == N:
                return i
            if col[c] == M:
                return i
