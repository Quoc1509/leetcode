# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        def dfs(node):
            if not node.left and not node.right:
                return 1, node.val
            
            l, r, lchild, rchild = 0, 0, node.val, node.val
            if node.left:
                l, lchild = dfs(node.left)
            if node.right:
                r, rchild = dfs(node.right)
            if rchild == lchild == node.val:
                return l+r+1, rchild
            else:
                return l+r, -inf
        return dfs(root)[0]
            
            
            