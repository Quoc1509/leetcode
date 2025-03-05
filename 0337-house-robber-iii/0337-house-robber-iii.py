# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        @cache
        def backTracking(node, allow):
            if not node: return 0
            choose = -inf
            noChoose = backTracking(node.left, 1) + backTracking(node.right, 1)
            if allow:
                
                choose = backTracking(node.left, 0)+backTracking(node.right, 0)+node.val
  
            return max(noChoose, choose)
        return backTracking(root, True)
            