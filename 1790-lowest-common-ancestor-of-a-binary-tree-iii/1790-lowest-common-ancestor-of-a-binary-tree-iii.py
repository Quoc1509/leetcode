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
        root = None
        def findRoot(node):
            nonlocal root
            if not node.parent and not root:
                root = node
                return
            findRoot(node.parent)
        findRoot(q)
        res = None
        def dfs(node):
            nonlocal res
            if not node:
                return False
            l = dfs(node.left)
            r = dfs(node.right)
            
            if (l and r) or ((l or r) and (node == q or node == p)):
                res = node
            if node == p or node == q:
                return True
            return l or r
        dfs(root)
        return res
        
