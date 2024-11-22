"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        res = [None]
        def dfs1(root):
            if not root: return False
            if root == q:
                return True
            return dfs1(root.left) or dfs1(root.right)
        
        def dfs2(root):
            if not root: return False
            if root == p:
                return True
            return dfs2(root.left) or dfs2(root.right)
        visit = set()

        def dfs3(root):
            if not root:
                return
            if root in visit:
                res[0] = root
                return
            visit.add(root)
            
            dfs3(root.parent)        

        if dfs1(p):
            return p
        if dfs2(q):
            return q
        dfs3(p.parent)
        dfs3(q.parent)
        return res[0]