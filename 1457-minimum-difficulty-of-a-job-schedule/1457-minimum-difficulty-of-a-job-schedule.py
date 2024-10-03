class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        N = len(jobDifficulty)
        if N < d: return -1
        @cache
        def dfs(i, ma, day):
            if i == N:
                if day == 0:
                    return ma

                else: return inf
            if i + 1 >= N:
                new_max = 0
            else:
                new_max = jobDifficulty[i+1]
            cut = dfs(i+1, new_max, day-1) + max(ma, jobDifficulty[i])
            noCut = dfs(i+1, max(ma, jobDifficulty[i]), day)
            return min(cut, noCut)
        return dfs(0, 0, d)





