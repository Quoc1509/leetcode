"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node: return None
        q = deque()
        q.append(node)
        visit = {}
        visit[node.val] = Node(node.val)
        while q:
            n = q.popleft()
            cur = visit[n.val]
            for no in n.neighbors:     
                if no.val not in visit:
                    copy = Node(no.val)
                    q.append(no)
                    visit[no.val] = copy

                cur.neighbors.append(visit[no.val])
        return visit[node.val]