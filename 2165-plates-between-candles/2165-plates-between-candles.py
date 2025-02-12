class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        count = 0
        plates = []
        mp = defaultdict(int)
        for i, e in enumerate(s):
            if e == '|':
                mp[i] = count
                plates.append(i)
            else:
                count += 1
        if not plates:
            return [0]*len(queries)
        res = []
        # print(plates, mp)
        for a, b in queries:
            if a == b:
                res.append(0)
                continue
            idx_left = bisect_left(plates, a)
            idx_right = bisect_right(plates, b)
            # print(idx_left, idx_right)
            res.append(max(0, mp[plates[idx_right-1]]-mp[plates[idx_left]]))
        return res