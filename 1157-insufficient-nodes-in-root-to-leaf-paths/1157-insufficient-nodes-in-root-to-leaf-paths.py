# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
        def dfs(node, total):
            if not node: return False
            if not node.left and not node.right:
                return True if total+node.val >= limit else False
            

            left = dfs(node.left, total+node.val)
            right = dfs(node.right, total+node.val)
            # print(left, right, node.val, total)
            if not left:
                node.left = None
            if not right:
                node.right = None
            return left or right
        check = dfs(root, 0)
        if not check: return None
        return root