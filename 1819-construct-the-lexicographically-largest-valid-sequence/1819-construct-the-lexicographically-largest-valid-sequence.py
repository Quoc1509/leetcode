class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        N = n*2-1
        res = [0] * N
        used = set()
        def backTracking(idx):
            while idx < N and res[idx] != 0:
                idx += 1
            if len(used) == n:
                return True
            for i in range(n, 0, -1):
                if i in used:
                    continue
                if i==1:
                    res[idx] = i
                    used.add(i)
                    if backTracking(idx+1):
                        return True
                    used.remove(i)
                    res[idx] = 0
                else:
                    if idx + i < N and res[idx+i] == 0:
                        res[idx] = res[idx+i]= i
                        used.add(i)
                        if backTracking(idx+1):
                            return True
                        used.remove(i)
                        res[idx] = res[idx+i] = 0
            return False

        backTracking(0)
        # print(res)
        return res