class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        res = []
        graph = defaultdict(list)
        for a, b in sorted(tickets, reverse=True):
            graph[a].append(b)
        
        res = []
        def dfs(node):
            
            while graph[node]:
                no = graph[node].pop()
                dfs(no)
            res.append(node)
        dfs('JFK')
        return res[::-1]