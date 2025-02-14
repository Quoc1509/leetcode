class TreeAncestor:

    def __init__(self, n: int, parent: List[int]):
        self.graph = defaultdict(list)
        self.Deep = ceil(log2(n))+1
        self.up = [[-1] * self.Deep for _ in range(n)]
        self.D = [0] * n
        self.makeGraph(parent)
        self.setUp(parent[0], 0)
  
    
    def makeGraph(self, parent):
        for i, e in enumerate(parent):
            self.graph[e].append(i)

    def setUp(self, node, depth):
        for ne in self.graph[node]:
            self.up[ne][0] = node
            for k in range(1, self.Deep):
                if self.up[ne][k-1] == -1:
                    break
                self.up[ne][k] = self.up[self.up[ne][k-1]][k-1]

            self.setUp(ne, depth+1)
        self.D[node] = depth 

    def getKthAncestor(self, node: int, k: int) -> int:
        for i in range(self.Deep):
            if k & (1 << i):
                node = self.up[node][i]
                if node == -1:
                    return -1
        return node


# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)