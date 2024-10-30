class Solution:
    def maxPower(self, stations: List[int], r: int, k: int) -> int:
        N = len(stations)
        le, ri = min(stations), sum(stations) + k
        
        def check(mid):
            cur = sum(stations[:r])
            temp = stations[:]
            num = k
            for i in range(N):
                if i + r < N:
                    cur += temp[i+r]
                if i - r -1 >= 0:
                    cur -= temp[i-r-1]
                if cur < mid:
                    diff = mid - cur
                    temp[min(N-1, i+r)] += diff
                    cur += diff
                    num -= diff
                # print(cur, temp)
                if num < 0:
                    return False
            return True
                    

        while le <= ri:
            m = (le+ri)//2
            if check(m):
                le = m + 1
            else:
                ri = m - 1
        return ri

