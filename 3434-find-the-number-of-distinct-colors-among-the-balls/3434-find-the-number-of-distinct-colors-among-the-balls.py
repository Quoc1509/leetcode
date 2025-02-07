class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        ball = defaultdict(int)
        color = defaultdict(int)
        res = [] 
        for a, b in queries:
            if a in ball:
                color[ball[a]] -= 1
                if color[ball[a]] == 0:
                    del[color[ball[a]]]
            ball[a] = b
            color[b] += 1
            res.append(len(color))
        # print(res)
        return res