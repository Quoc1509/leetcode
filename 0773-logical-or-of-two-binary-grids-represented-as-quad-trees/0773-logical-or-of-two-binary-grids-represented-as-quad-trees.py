"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def intersect(self, quadTree1: 'Node', quadTree2: 'Node') -> 'Node':
        
        def dfs(node1, node2):
            # if not node1 and not node2: return None
            if not node1: return node2
            if not node2: return node1
            if node1.isLeaf and node2.isLeaf:
                return Node(node1.val|node2.val, 1)
            if node1.isLeaf and node1.val:
                return Node(node1.val, 1)
            if node2.isLeaf and node2.val:
                return Node(node2.val, 1)
            tLeft = dfs(node1.topLeft, node2.topLeft)
            bLeft = dfs(node1.bottomLeft, node2.bottomLeft)
            tRight = dfs(node1.topRight, node2.topRight)
            bRight = dfs(node1.bottomRight, node2.bottomRight)
            if tLeft.isLeaf and bLeft.isLeaf and tRight.isLeaf and bRight.isLeaf and tLeft.val and bLeft.val and tRight.val and bRight.val:
                return Node(1, 1)
            return Node(tLeft.val|bLeft.val|tRight.val|bRight.val, 0, tLeft, tRight, bLeft, bRight)
        res = dfs(quadTree1, quadTree2)
        return res