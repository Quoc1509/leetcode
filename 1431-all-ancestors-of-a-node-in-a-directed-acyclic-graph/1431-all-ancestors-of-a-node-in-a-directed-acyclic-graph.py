from collections import defaultdict
from typing import List

class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # Step 1: Build the graph
        graph = defaultdict(list)
        for from_node, to_node in edges:
            graph[from_node].append(to_node)

        # Step 2: Initialize the list to store ancestors for each node
        ancestors = [set() for _ in range(n)]
        
        # Step 3: Helper function to perform DFS and update ancestors
        def dfs(node, current_ancestor):
            for neighbor in graph[node]:
                if current_ancestor not in ancestors[neighbor]:
                    ancestors[neighbor].add(current_ancestor)
                    dfs(neighbor, current_ancestor)

        # Step 4: Perform DFS from each node to find all ancestors
        for node in range(n):
            dfs(node, node)

        # Step 5: Sort the ancestors for each node
        answer = [sorted(list(anc)) for anc in ancestors]

        return answer
