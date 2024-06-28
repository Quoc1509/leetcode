class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        temp =  []
        graph = defaultdict(int)
        for i in roads:
            graph[i[0]] += 1
            graph[i[1]] += 1
        for i, e in graph.items():
            temp.append([e, i])
        temp.sort(reverse=True)
        print(temp)
        s = [0] * n
        for i in temp:
            s[i[1]] = n
            n -= 1
        res = 0
        for i in roads:
            res += (s[i[0]] + s[i[1]])
        return res