class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph = defaultdict(list)
        for a, b in richer:
            graph[b].append(a)
        res = [-1] * len(quiet)
        @cache
        def dfs(index):
            temp = (quiet[index], index)
            for n in graph[index]:
                ans, pos = dfs(n)
                if temp[0] > ans:
                    temp = (ans, pos)
            res[index] = temp[1]
            return temp

        for i in range(len(quiet)):
            if res[i] == -1:
                dfs(i) 
        return res
