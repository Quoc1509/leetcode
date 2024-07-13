# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        res = [None]
        def dfs(node):
            if not node: return False
            left = dfs(node.left)
            right = dfs(node.right)
            if left and right: res[0] = node
            if left and (node == q or node == p):
                res[0] = node
            if right and (node  == q or node == p):
                res[0] = node
            # print(left, right)
            if node == q or node == p:    
                # print(left, right)            
                return True
            
            return left or right
        dfs(root)
        return res[0]