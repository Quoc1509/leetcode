# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def check(node1, node2):
            if not node1 and not node2: return True
            if not node1 or not node2: return False
            if node1.val != node2.val:
                return False
            return check(node1.left, node2.left) and check(node1.right, node2.right)
        
        def dfs(node):
            if not node: return False 
            
            l = dfs(node.left) 
            r = dfs(node.right)
            if (not l and not r) and node.val == subRoot.val:
                return check(node, subRoot)
                
            return l or r
        return dfs(root)