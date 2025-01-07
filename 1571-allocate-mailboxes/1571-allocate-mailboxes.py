class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        houses.sort()
        dist = defaultdict(int)
        for i in range(len(houses)):
            for j in range(i+1, len(houses)):
                median = (i+j)//2
                for l in range(i, j+1):
                    dist[(i, j)] += abs(houses[median]-houses[l])
        # print(dist)
        @cache
        def dfs(i, mails):
            if i >= len(houses):
                if mails == 0:
                    return 0
                return inf
            if mails == 0:
                return inf 
            temp = inf
            for j in range(i, len(houses)):
                temp = min(temp, dfs(j+1, mails-1)+dist[(i,j)])
            # print(temp, i, mails)
            return temp
        return dfs(0, k)