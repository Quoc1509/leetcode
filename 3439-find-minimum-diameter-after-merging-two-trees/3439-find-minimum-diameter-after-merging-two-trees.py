class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        
        def Tree(arr):
            mp = defaultdict(set)
            for a, b in arr:
                mp[a].add(b)
                mp[b].add(a)
            return mp
            
        def centerRoot(adj):
            leaves = deque(node for node in adj if len(adj[node]) == 1)
            remaining_nodes = len(adj)
            radius = 0
            while remaining_nodes > 2:
                leaf_count = len(leaves)
                remaining_nodes -= leaf_count
                
                for _ in range(leaf_count):
                    leaf = leaves.popleft()
                    neighbor = adj[leaf].pop()  
                    adj[neighbor].remove(leaf)  
                    
                    if len(adj[neighbor]) == 1:
                        leaves.append(neighbor)
                radius += 1
            return radius if remaining_nodes <= 1 else radius+1, radius*2 if remaining_nodes <= 1 else radius*2+1
        
        mp1 = Tree(edges1)
        mp2 = Tree(edges2)
        rad1, dar1 = centerRoot(mp1)
        rad2, dar2 = centerRoot(mp2)
        res = 0
        res = max(res, dar1, dar2, rad1+rad2+1)
        return res


