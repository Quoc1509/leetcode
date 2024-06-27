class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        graph = defaultdict(int)
        for i in edges:
            graph[i[0]] += 1
            if graph[i[0]] == len(edges):
                return i[0]
            graph[i[1]] += 1
            if graph[i[1]] == len(edges):
                return i[1]
            
        # print(graph)
        # for i, e in graph.items():
        #     if e == len(edges):
        #         return i
        return -1
        